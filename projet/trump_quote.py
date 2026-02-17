#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Fetch a random Trump quote from the What Does Trump Think API."""

import json
import sys
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

API_URL = "https://api.whatdoestrumpthink.com/api/v1/quotes/random"


def fetch_random_quote() -> str:
    try:
        with urlopen(API_URL, timeout=10) as response:
            payload = response.read().decode("utf-8")
    except HTTPError as exc:
        raise RuntimeError(f"HTTP error {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error: {exc.reason}") from exc

    try:
        data = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise RuntimeError("Invalid JSON response") from exc

    if "message" not in data:
        raise RuntimeError("Unexpected API response format")

    return data["message"]


def main() -> int:
    try:
        quote = fetch_random_quote()
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(quote)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
