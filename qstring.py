"""Build and parse query strings without pulling in a framework."""
from __future__ import annotations

from urllib.parse import parse_qsl, urlencode


def parse_query(text: str) -> dict[str, list[str]]:
    raw = (text or "").strip()
    if raw.startswith("?"):
        raw = raw[1:]
    out: dict[str, list[str]] = {}
    for key, value in parse_qsl(raw, keep_blank_values=True, strict_parsing=False):
        out.setdefault(key, []).append(value)
    return out


def build_query(data: dict[str, str | list[str]]) -> str:
    pairs: list[tuple[str, str]] = []
    for key, value in data.items():
        if isinstance(value, list):
            pairs.extend((key, item) for item in value)
        else:
            pairs.append((key, value))
    return urlencode(pairs)
