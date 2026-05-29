---
name: serpapi-pool
description: "SerpAPI Key Pool — Multi-Key, Round-Robin, 429-Fallback"
version: 1.0.0
category: web-search
requirements:
  - infisical CLI + Login
  - Keys SERPAPI_KEY_1..4 in Infisical
  - SIN-Passwordmanager-Infisical-Bundle
---

# SerpAPI Pool Skill

Multi-Key SerpAPI Pool für Hermes Web-Suche.

## Commands

```bash
# Besten Key holen
python3 ~/.hermes/scripts/serpapi-pool.py

# Pool-Status
python3 ~/.hermes/scripts/serpapi-pool.py status
```

## Abhängigkeit

Braucht `~/.hermes/scripts/infisical-get.py` aus dem Passwordmanager-Bundle.
