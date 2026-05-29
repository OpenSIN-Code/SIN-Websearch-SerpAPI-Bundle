# SIN-Hermes-Websearch-SerpAPI-Pool-Bundle

**Multi-Key SerpAPI Pool für Hermes Web-Suche.**

Rotiert automatisch zwischen mehreren SerpAPI-Keys um Rate-Limits zu umgehen.

## Installation

```bash
git clone git@github.com:SIN-Hermes-Bundles/SIN-Hermes-Websearch-SerpAPI-Pool-Bundle.git ~/SIN-Hermes-Websearch-SerpAPI-Pool-Bundle
cd ~/SIN-Hermes-Websearch-SerpAPI-Pool-Bundle && bash install.sh
```

## Funktionsweise

```
Hermes Web-Suche → serpapi-pool.js → SERPAPI_KEY_1 (100/100)
                                   → SERPAPI_KEY_2 (45/100)
                                   → SERPAPI_KEY_3 (0/100)  ← genommen!
```

## Keys aus Infisical

Keys werden aus Infisical geladen (via Passwordmanager-Bundle).
Fallback: `~/.hermes/.env` → `SERPAPI_KEY_1`, `SERPAPI_KEY_2`, ...
