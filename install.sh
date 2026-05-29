#!/bin/bash
set -e
echo "SIN-Hermes-Websearch-SerpAPI-Pool-Bundle"
BUNDLE="$HOME/.hermes/bundles/serpapi-pool"
mkdir -p "$BUNDLE" "$HOME/.hermes/scripts"
cp scripts/serpapi-pool.py "$HOME/.hermes/scripts/"
chmod +x "$HOME/.hermes/scripts/serpapi-pool.py"
echo "Installed: ~/.hermes/scripts/serpapi-pool.py"
echo ""

# Auto-Setup: SERPAPI_KEY in .env schreiben
if command -v python3 &>/dev/null; then
  echo "→ Running setup (writing SERPAPI_KEY to ~/.hermes/.env)..."
  python3 "$HOME/.hermes/scripts/serpapi-pool.py" setup 2>/dev/null && \
    echo "✅ SERPAPI_KEY in ~/.hermes/.env gesetzt" || \
    echo "⚠️  Setup fehlgeschlagen — Infisical-Login prüfen"
fi

echo ""
echo "Usage:"
echo "  python3 ~/.hermes/scripts/serpapi-pool.py         # get best key"
echo "  python3 ~/.hermes/scripts/serpapi-pool.py status  # show pool"
echo ""
echo "WICHTIG — Hermes search_backend konfigurieren:"
echo "  In ~/.hermes/config.yaml setzen:"
echo "    search_backend: serpapi"
