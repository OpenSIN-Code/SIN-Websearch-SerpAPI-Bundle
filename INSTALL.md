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

## 4. Nutzung

```bash
# Besten Key holen (round-robin, auto-fallback bei 429):
python3 ~/.hermes/scripts/serpapi-pool.py

# Pool-Status anzeigen:
python3 ~/.hermes/scripts/serpapi-pool.py status
```

---

## 5. Fehlerbehebung

| Problem | Ursache | Lösung |
|---------|---------|--------|
| `infisical: command not found` | CLI fehlt | `brew install infisical` |
| `infisical-list.py: No such file` | Passwordmanager fehlt | Schritt 0 ausführen |
| Keys nicht gefunden | Nicht in Infisical | `infisical secrets set ...` |
| serpapi-pool.py nicht gefunden | Install nicht ausgeführt | `bash install.sh` |

---

*Stand: 2026-05-29 | v1.0.0 | 4 Keys | Infisical SSOT*
