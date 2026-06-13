# Archive: SIN-Websearch-SerpAPI-Bundle

This repository is **archived** and has been superseded by the unified `sin-websearch` binary in `OpenSIN-Code/web_search_bundle`.

## What it was

A Python-based SerpAPI key-pool bundle for the Hermes web search backend. It rotated automatically between multiple SerpAPI keys to avoid rate limits.

## What replaced it

- `sin-websearch` (Go binary) in `OpenSIN-Code/web_search_bundle`.
- Includes a built-in API key pool with rotation and 429 fallback.
- Exposes `websearch_search`, `websearch_pulse`, `websearch_resolve`, and more via MCP and HTTP API.

## Why it was archived

The unified Go binary consolidates the SerpAPI pool, caching, history, and all search engines in a single self-contained executable.

## Migration

| Old (Python bundle) | New (Go binary) |
| --- | --- |
| `serpapi-pool.py` | `internal/pool/` in `web_search_bundle` |
| Hermes `search_backend: serpapi` | `sin-websearch search` or `websearch_search` MCP tool |
| Infisical key loading | `internal/secrets/` (Infisical / env) |

## Read-only

No new issues, PRs, or releases are accepted. This repo remains available for historical reference.

See the active repository: https://github.com/OpenSIN-Code/web_search_bundle
