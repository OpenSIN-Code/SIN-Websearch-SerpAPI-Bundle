"SerpAPI web search plugin (search-only, key-pool auto-rotation)."

from __future__ import annotations

from plugins.web.serpapi.provider import SerpAPIWebSearchProvider


def register(ctx) -> None:
    """Register the SerpAPI provider with the plugin context."""
    ctx.register_web_search_provider(SerpAPIWebSearchProvider())
