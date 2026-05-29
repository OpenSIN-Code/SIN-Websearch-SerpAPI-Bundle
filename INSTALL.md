# SIN-Hermes-Websearch-SerpAPI-Pool-Bundle — Installation

*Multi-Key SerpAPI Pool für Hermes Agent. Rotiert zwischen Keys bei Rate-Limits.*

---

## ⚠️ SCHRITT 0: Passwordmanager installieren (PFLICHT)

Dieses Bundle braucht das Passwordmanager-Bundle für Infisical-Zugriff:

```bash
cd ~/dev/SIN-Passwordmanager-Infisical-Bundle && bash install.sh
~/.hermes/scripts/infisical-list.py
# ✅ SERPAPI_KEY_1..4 müssen sichtbar sein
# ❌ Sonst: Infisical-Login prüfen
```

---

## 1. Voraussetzungen

### 1.1 Infisical CLI + Login

```bash
infisical --version && infisical login status
# ✅ "infisical version x.x.x" + "You are logged in"
# ❌ → `brew install infisical && infisical login`
```

### 1.2 Keys in Infisical prüfen

```bash
~/.hermes/scripts/infisical-list.py
# ✅ SERPAPI_KEY_1..4 vorhanden
# ❌ Fehlende Keys setzen:
#    infisical secrets set SERPAPI_KEY_1=<key> \
#      --projectId fa7758b4-f84c-4297-966e-710056d531ef \
#      --env dev --path / --silent
```

### 1.3 Python 3.9+

```bash
python3 --version
# ✅ "Python 3.9.x" oder höher
```

---

## 2. Repository klonen + installieren

```bash
cd ~/dev
git clone git@github.com:SIN-Hermes-Bundles/SIN-Hermes-Websearch-SerpAPI-Pool-Bundle.git
cd SIN-Hermes-Websearch-SerpAPI-Pool-Bundle
bash install.sh
# ✅ "Installed: ~/.hermes/scripts/serpapi-pool.py"
```

---

## 3. Health-Check

```bash
python3 ~/.hermes/scripts/serpapi-pool.py status
# ✅ Sollte Keys + Status anzeigen
```

---

## 4. Hermes search_backend konfigurieren (WICHTIG!)

Damit Hermes den SerpAPI-Pool auch wirklich für Web-Suche nutzt:

```bash
# In ~/.hermes/config.yaml setzen:
#   search_backend: serpapi
#
# Prüfen ob schon gesetzt:
grep "search_backend" ~/.hermes/config.yaml
# ✅ search_backend: serpapi  ← fertig
# ❌ search_backend: ''       ← muss geändert werden
```

**Zum Setzen (einzeilig):**
```bash
sed -i '' 's/search_backend: '\'\''/search_backend: serpapi/' ~/.hermes/config.yaml
# ✅ search_backend auf serpapi gesetzt
```

**Oder mit `yq` (sauberer):**
```bash
yq eval '.search_backend = "serpapi"' -i ~/.hermes/config.yaml
```

Nach Änderung: Hermes neu starten, dann nutzt er SerpAPI für `web_search`.

---

## 5. Verifikation — Web-Suche ready?

```bash
# 1. SERPAPI_KEY gesetzt?
grep SERPAPI_KEY ~/.hermes/.env
# ✅ SERPAPI_KEY=48f186d4...

# 2. search_backend richtig?
grep search_backend ~/.hermes/config.yaml
# ✅ search_backend: serpapi

# 3. Pool funktioniert?
python3 ~/.hermes/scripts/serpapi-pool.py status
# ✅ Keys gefunden
```

Wenn alle 3 ✅ sind → **Web-Suche ist bereit**. Dein Agent kann `web_search` nutzen.

---

## 6. Nutzung

```bash
# Besten Key holen (round-robin, auto-fallback bei 429):
python3 ~/.hermes/scripts/serpapi-pool.py

# Pool-Status anzeigen:
python3 ~/.hermes/scripts/serpapi-pool.py status
```

---

## 7. Fehlerbehebung

| Problem | Ursache | Lösung |
|---------|---------|--------|
| `infisical: command not found` | CLI fehlt | `brew install infisical` |
| `infisical-list.py: No such file` | Passwordmanager fehlt | Schritt 0 ausführen |
| Keys nicht gefunden | Nicht in Infisical | `infisical secrets set ...` |
| serpapi-pool.py nicht gefunden | Install nicht ausgeführt | `bash install.sh` |
| Web-Suche nutzt nicht SerpAPI | `search_backend` falsch | `sed -i '' 's/search_backend: .../search_backend: serpapi/' ~/.hermes/config.yaml` |
| `web_search` schlägt fehl | `SERPAPI_KEY` nicht in `.env` | `python3 ~/.hermes/scripts/serpapi-pool.py setup` |

---

*Stand: 2026-05-29 | v1.0.0 | 4 Keys | Infisical SSOT*
