# install-playwright-python

[![PyPI version](
  <https://badge.fury.io/py/install-playwright.svg>
  )](
  <https://badge.fury.io/py/install-playwright>
) [![Maintainability](
  <https://qlty.sh/badges/5fcd7b4f-782d-4b27-99ef-4f5c6eae678b/maintainability.svg>
  )](
  <https://qlty.sh/gh/eggplants/projects/install-playwright-python>
) [![pre-commit.ci status](
  <https://results.pre-commit.ci/badge/github/eggplants/install-playwright-python/master.svg>
  )](
  <https://results.pre-commit.ci/latest/github/eggplants/install-playwright-python/master>
) [![Maintainability](
  <https://qlty.sh/badges/5fcd7b4f-782d-4b27-99ef-4f5c6eae678b/maintainability.svg>
  )](
  <https://qlty.sh/gh/eggplants/projects/install-playwright-python>
) [![Test](
  <https://github.com/eggplants/install-playwright-python/actions/workflows/test.yml/badge.svg>
  )](
  <https://github.com/eggplants/install-playwright-python/actions/workflows/test.yml>
)

Execute [`playwright install`](https://playwright.dev/python/docs/cli) from Python.

```python
from install_playwright import install
```

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    install(p.chrome)
    browser = p.chrome.launch()
    # ...
```

```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        install(p.chrome)
        browser = await p.chrome.launch()
        # ...
```

## Install

```bash
pip install install-playwright
```

## License

MIT
