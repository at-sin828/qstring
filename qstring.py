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


def without_key(data: dict[str, list[str]], key: str) -> dict[str, list[str]]:
    return {name: list(values) for name, values in data.items() if name != key}


def has_key(data: dict[str, list[str]], key: str) -> bool:
    return key in data


def key_names(data: dict[str, list[str]]) -> list[str]:
    return list(data)


def value_count(data: dict[str, list[str]], key: str) -> int:
    return len(data.get(key) or [])


def first_value(data: dict[str, list[str]], key: str, default: str = "") -> str:
    values = data.get(key) or []
    return values[0] if values else default
