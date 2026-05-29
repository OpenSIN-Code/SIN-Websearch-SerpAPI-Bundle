"""SerpAPI web search provider with automatic key-pool rotation.

Calls ``~/.hermes/scripts/serpapi-pool.py`` to obtain the best API key
(least-used key across the pool) before each request.

Config keys::

    web:
      search_backend: "serpapi"

The key pool is managed by ``serpapi-pool.py`` which discovers keys from
both ``~/.hermes/.env`` and Infisical (EU region).
"""

from __future__ import annotations

import json
import logging
import os
from typing import Any, Dict, List

from agent.web_search_provider import WebSearchProvider

logger = logging.getLogger(__name__)

POOL_SCRIPT = os.path.expanduser("~/.hermes/scripts/serpapi-pool.py")


def _get_api_key() -> str:
    """Get the best SerpAPI key from the pool (least-used, auto-rotates).

    Falls back to ``SERPAPI_KEY`` env var if the pool script is missing.
    """
    if os.path.exists(POOL_SCRIPT):
        import subprocess

        result = subprocess.run(
            ["python3", POOL_SCRIPT],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        logger.warning("serpapi-pool.py failed: %s", result.stderr.strip())

    # Fallback to single key in env
    return os.getenv("SERPAPI_KEY", "")


def _serpapi_search(query: str, limit: int) -> Dict[str, Any]:
    """Execute a SerpAPI search and return normalized results."""
    import httpx

    api_key = _get_api_key()
    if not api_key:
        raise ValueError(
            "No SerpAPI key available. Set SERPAPI_KEY in ~/.hermes/.env "
            "or configure Infisical secrets."
        )

    params = {
        "q": query,
        "num": min(limit, 20),
        "api_key": api_key,
        "engine": "google",
        "gl": "de",        # Germany results
        "hl": "de",        # German language
    }

    logger.info("SerpAPI search: '%s' (limit=%d)", query, limit)
    response = httpx.get(
        "https://serpapi.com/search",
        params=params,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def _normalize_serpapi_results(response: Dict[str, Any]) -> Dict[str, Any]:
    """Map SerpAPI organic results to ``{success, data: {web: [...]}}``."""
    web_results = []
    organic = response.get("organic_results", [])
    for i, result in enumerate(organic):
        web_results.append(
            {
                "title": result.get("title", ""),
                "url": result.get("link", ""),
                "description": result.get("snippet", ""),
                "position": result.get("position", i + 1),
            }
        )
    return {"success": True, "data": {"web": web_results}}


class SerpAPIWebSearchProvider(WebSearchProvider):
    """SerpAPI search provider with key-pool rotation."""

    @property
    def name(self) -> str:
        return "serpapi"

    @property
    def display_name(self) -> str:
        return "SerpAPI (Key Pool)"

    def is_available(self) -> bool:
        """Return True when at least one SerpAPI key can be found."""
        key = _get_api_key()
        return bool(key and len(key) > 5)

    def supports_search(self) -> bool:
        return True

    def supports_extract(self) -> bool:
        return False  # SerpAPI search-only

    def supports_crawl(self) -> bool:
        return False

    def search(self, query: str, limit: int = 5) -> Dict[str, Any]:
        """Execute a SerpAPI organic search."""
        try:
            from tools.interrupt import is_interrupted

            if is_interrupted():
                return {"success": False, "error": "Interrupted"}

            raw = _serpapi_search(query, limit)
            return _normalize_serpapi_results(raw)
        except ValueError as exc:
            return {"success": False, "error": str(exc)}
        except Exception as exc:  # noqa: BLE001 — includes httpx errors
            logger.warning("SerpAPI search error: %s", exc)
            return {"success": False, "error": f"SerpAPI search failed: {exc}"}

    def get_setup_schema(self) -> Dict[str, Any]:
        return {
            "name": "SerpAPI (Key Pool)",
            "badge": "paid",
            "tag": "Google search with automatic key rotation across multiple API keys.",
            "env_vars": [
                {
                    "key": "SERPAPI_KEY",
                    "prompt": "SerpAPI key (or omit to use Infisical pool)",
                    "url": "https://serpapi.com/manage-api-key",
                },
            ],
        }
