#!/usr/bin/env python3
"""SerpAPI Key Pool — rotiert automatisch zwischen mehreren Keys."""

import os, json, time, subprocess

POOL_FILE = os.path.expanduser("~/.hermes/serpapi_pool.json")

def load_pool():
    if os.path.exists(POOL_FILE):
        with open(POOL_FILE) as f:
            return json.load(f)
    return {"keys": []}

def save_pool(pool):
    with open(POOL_FILE, "w") as f:
        json.dump(pool, f, indent=2)

def discover_keys():
    """Find all SERPAPI keys from .env and Infisical."""
    keys = []

    # From .env
    env_path = os.path.expanduser("~/.hermes/.env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith("SERPAPI_KEY") and "=" in line:
                    val = line.split("=", 1)[1]
                    if len(val) > 5:
                        keys.append(val)

    # From Infisical
    try:
        result = subprocess.run(
            ["infisical", "secrets", "--output", "json", "--env", "dev"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            secrets = data if isinstance(data, list) else data.get("secrets", [])
            for s in secrets:
                key_name = s.get("secretKey", s.get("key", ""))
                if "SERPAPI" in key_name.upper():
                    keys.append(s.get("secretValue", ""))
    except Exception:
        pass

    return list(set(keys))  # deduplicate

def get_best_key():
    """Select key with most remaining quota."""
    pool = load_pool()
    keys = pool.get("keys", [])

    if not keys:
        discovered = discover_keys()
        if not discovered:
            return None
        pool["keys"] = [{"key": k, "used": 0} for k in discovered]
        save_pool(pool)
        keys = pool["keys"]

    # Sort by usage (least used first)
    keys.sort(key=lambda x: x.get("used", 0))
    best = keys[0]
    best["used"] = best.get("used", 0) + 1
    best["last_used"] = time.time()
    save_pool(pool)
    return best["key"]

def status():
    pool = load_pool()
    print("SerpAPI Key Pool Status:\n")
    for i, k in enumerate(pool.get("keys", [])):
        print("  Key %d: used %d times" % (i+1, k.get("used", 0)))
    print("\n  Total keys: %d" % len(pool.get("keys", [])))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "status":
        status()
    else:
        key = get_best_key()
        if key:
            print(key)
        else:
            print("NO_KEYS_FOUND")
            sys.exit(1)
