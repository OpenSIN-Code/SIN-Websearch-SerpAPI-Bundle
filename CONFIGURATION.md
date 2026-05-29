# Configuration Guide

## Overview

The SerpAPI Pool Bundle manages 4 SerpAPI keys for web search with round-robin and 429 fallback.

## Configuration

### ~/.hermes/config.yaml

```yaml
# Search configuration
search:
  backend: serpapi
  
# SerpAPI Pool
serpapi:
  keys:
    - ${SERPAPI_KEY_1}
    - ${SERPAPI_KEY_2}
    - ${SERPAPI_KEY_3}
    - ${SERPAPI_KEY_4}
  rotate_interval: 900
  max_retries: 3
```

## Key Management

### Setup

```bash
# Run setup
~/.hermes/scripts/serpapi-pool.py setup

# Check status
~/.hermes/scripts/serpapi-pool.py status
```

### Manual Key Rotation

```bash
# Rotate to next key
~/.hermes/scripts/serpapi-pool.py rotate

# Check current key
~/.hermes/scripts/serpapi-pool.py current
```

## Pool Configuration

### Round-Robin

```python
# In serpapi-pool.py
KEYS = [
    os.getenv("SERPAPI_KEY_1"),
    os.getenv("SERPAPI_KEY_2"),
    os.getenv("SERPAPI_KEY_3"),
    os.getenv("SERPAPI_KEY_4"),
]

CURRENT_INDEX = 0
ROTATE_INTERVAL = 900  # seconds
```

### 429 Fallback

```python
# On 429 error:
# 1. Switch to next key
# 2. Retry request
# 3. If all keys fail, wait 60s
```

## Advanced Configuration

### Custom Key Count

```bash
# Edit pool script
nano ~/.hermes/scripts/serpapi-pool.py

# Add more keys
KEYS = [
    os.getenv("SERPAPI_KEY_1"),
    os.getenv("SERPAPI_KEY_2"),
    # Add more...
]
```

### Auto-Rotation

```bash
# Cron job
*/15 * * * * ~/.hermes/scripts/serpapi-pool.py rotate
```

## Environment Variables

```bash
export SERPAPI_KEY_1="your-key-1"
export SERPAPI_KEY_2="your-key-2"
export SERPAPI_KEY_3="your-key-3"
export SERPAPI_KEY_4="your-key-4"
```

## Troubleshooting

### Keys not working

```bash
# Test key
curl "https://serpapi.com/search?q=test&api_key=$SERPAPI_KEY_1"

# Check pool status
~/.hermes/scripts/serpapi-pool.py status
```

### 429 errors

```bash
# Check key usage
~/.hermes/scripts/serpapi-pool.py usage

# Manual rotation
~/.hermes/scripts/serpapi-pool.py rotate
```

---
*Last updated: 2026-05-30*
