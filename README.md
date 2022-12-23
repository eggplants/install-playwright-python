# install-playwright-python

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
