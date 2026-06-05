# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial SIN-Code-Bundle integration (ceo-audit workflow v3)
- OpenCode MCP server registration under `OpenSIN-Code/SIN-Websearch-SerpAPI-Bundle`
- Repository-level `SIN_GITHUB_FALLBACK_TOKEN` secret for the App commenter fallback
- Multi-Key SerpAPI pool for Hermes web search — auto-rotates across 4 SerpAPI keys
- Bypasses rate-limits by spreading queries across keys with cooldown
- GitNexus-indexed for blast-radius aware refactoring
- Installation: see [INSTALL.md](./INSTALL.md)
- Companion to the SIN-Hermes-V15-Patches and SIN-Hermes-Provider-Bundle stacks

### Security
- All commits verified via `git-immortal-commit` (annotated tags)
- API keys sourced from Infisical via SIN-Passwordmanager-Infisical-Bundle (never in repo)
