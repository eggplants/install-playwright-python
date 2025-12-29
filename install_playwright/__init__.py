""".. include:: ../README.md"""  # noqa: D415

from __future__ import annotations

import importlib.metadata
import subprocess
from os import EX_OK
from typing import TYPE_CHECKING

from playwright._impl._driver import compute_driver_executable, get_driver_env

if TYPE_CHECKING:
    from playwright.async_api import BrowserType as AsyncBrowserType
    from playwright.sync_api import BrowserType as SyncBrowserType

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"


def install(
    browser_type: SyncBrowserType | AsyncBrowserType,
    *,
    with_deps: bool = False,
    only_shell: bool = False,
) -> bool:
    """Install playwright and deps if needed.

    Args:
        browser_type (SyncBrowserType | AsyncBrowserType): `BrowserType` object. Example: `p.chrome`
        with_deps (bool, optional): install with dependencies. Defaults to `False`.
        only_shell (bool, optional): install only browser shell. Defaults to `False`.

    Returns:
        bool: succeeded or failed
    """
    driver_executable, driver_cli = compute_driver_executable()
    args = [driver_executable, driver_cli, "install", browser_type.name]

    if with_deps:
        args.append("--with-deps")

    if only_shell:
        args.append("--only-shell")

    proc = subprocess.run(  # noqa: S603
        args,
        env=get_driver_env(),
        capture_output=True,
        text=True,
        check=False,
    )

    return proc.returncode == EX_OK


def uninstall(
    *,
    all_browsers: bool = False,
) -> bool:
    """Uninstall playwright browsers.

    Args:
        all_browsers (bool, optional): uninstall all browsers. Defaults to `False`.

    Returns:
        bool: succeeded or failed
    """
    driver_executable, driver_cli = compute_driver_executable()
    args = [driver_executable, driver_cli, "uninstall"]

    if all_browsers:
        args.append("--all")

    proc = subprocess.run(  # noqa: S603
        args,
        env=get_driver_env(),
        capture_output=True,
        text=True,
        check=False,
    )

    return proc.returncode == EX_OK


__all__ = ("install", "uninstall")
