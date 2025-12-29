from __future__ import annotations

import pytest
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

from install_playwright import install, uninstall


def test_install_sync() -> None:
    with sync_playwright() as p:
        res = install(p.chromium)
        assert res is True


def test_install_sync_with_deps() -> None:
    with sync_playwright() as p:
        res = install(p.chromium, with_deps=True)
        assert res is True


@pytest.mark.asyncio
async def test_install_async() -> None:
    async with async_playwright() as p:
        res = install(p.chromium)
        assert res is True


@pytest.mark.asyncio
async def test_install_async_with_deps() -> None:
    async with async_playwright() as p:
        res = install(p.chromium, with_deps=True)
        assert res is True


@pytest.mark.asyncio
async def test_install_async_only_shell() -> None:
    async with async_playwright() as p:
        res = install(p.chromium, only_shell=True)
        assert res is True


def test_uninstall() -> None:
    res = uninstall()
    assert res is True


async def test_uninstall_all() -> None:
    res = uninstall(all_browsers=True)
    assert res is True
