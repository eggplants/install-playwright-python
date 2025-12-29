# install-playwright-python

[![PyPI version](
  <https://badge.fury.io/py/install-playwright.svg>
  )](
  <https://badge.fury.io/py/install-playwright>
) [![CI](
  <https://github.com/eggplants/install-playwright-python/actions/workflows/ci.yml/badge.svg>
  )](
  <https://github.com/eggplants/install-playwright-python/actions/workflows/ci.yml>
)

Execute [`playwright install`](https://playwright.dev/python/docs/cli) from Python.

## Install

```bash
pip install install-playwright
```

## Example

```python
from install_playwright import install
```

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    install(p.chromium)
    browser = p.chromium.launch()
    # ...
```

```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        install(p.chromium)
        browser = await p.chromium.launch()
        # ...
```

## License

MIT
