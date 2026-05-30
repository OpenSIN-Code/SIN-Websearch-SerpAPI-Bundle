# SIN-Hermes-Websearch-SerpAPI-Pool-Bundle

[![GitNexus](https://img.shields.io/badge/GitNexus-knowledge%20graph-8B5CF6)](.gitnexus/)

**Multi-Key SerpAPI Pool für Hermes Web-Suche.** Rotiert automatisch zwischen 4 SerpAPI-Keys um Rate-Limits zu umgehen.

**[📖 Installationsanleitung](INSTALL.md)**

## Quick Start

```bash
# 1. Passwordmanager installieren (Basis für Infisical):
cd ~/dev/SIN-Passwordmanager-Infisical-Bundle && bash install.sh

# 2. SerpAPI Pool installieren:
cd ~/dev/SIN-Hermes-Websearch-SerpAPI-Pool-Bundle && bash install.sh

# 3. Testen:
python3 ~/.hermes/scripts/serpapi-pool.py status
```

## Voraussetzungen

- Infisical CLI (`brew install infisical`) + Login
- 4 Keys `SERPAPI_KEY_1..4` in Infisical (Projekt: `fa7758b4-...`)
- [SIN-Passwordmanager-Infisical-Bundle](https://github.com/SIN-Hermes-Bundles/SIN-Passwordmanager-Infisical-Bundle) installiert

## Agent-Prompt (Copy & Paste)

```
Installiere SerpAPI-Pool-Bundle auf diesem Mac (3 Schritte):
1. cd ~/dev/SIN-Passwordmanager-Infisical-Bundle && bash install.sh
2. cd ~/dev/SIN-Hermes-Websearch-SerpAPI-Pool-Bundle && bash install.sh
3. sed -i '' "s/search_backend: ''/search_backend: serpapi/" ~/.hermes/config.yaml
4. grep SERPAPI_KEY ~/.hermes/.env  # ✅ Muss Key zeigen
5. grep search_backend ~/.hermes/config.yaml  # ✅ Muss serpapi zeigen
```
