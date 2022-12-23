# install-playwright-python

[![PyPI version](
  https://badge.fury.io/py/install-playwright.svg
  )](
  https://badge.fury.io/py/install-playwright
) [![Maintainability](
  https://api.codeclimate.com/v1/badges/75293ef4c40e3382cfe8/maintainability
  )](
  https://codeclimate.com/github/eggplants/install-playwright-python/maintainability
) [![pre-commit.ci status](
  https://results.pre-commit.ci/badge/github/eggplants/install-playwright-python/master.svg
  )](
  https://results.pre-commit.ci/latest/github/eggplants/install-playwright-python/master
) [![Test Coverage](
  https://api.codeclimate.com/v1/badges/75293ef4c40e3382cfe8/test_coverage
  )](
  https://codeclimate.com/github/eggplants/install-playwright-python/test_coverage
) [![Test](
  https://github.com/eggplants/install-playwright-python/actions/workflows/test.yml/badge.svg
  )](
  https://github.com/eggplants/install-playwright-python/actions/workflows/test.yml
)

Execute `playwright install` from Python.

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
