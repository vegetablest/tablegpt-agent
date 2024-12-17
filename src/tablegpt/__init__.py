from __future__ import annotations

import sys
import warnings
from pathlib import Path

possible_installation_locations = filter(lambda x: "site-packages" in x, sys.path)


def _find_tablegpt_ipykernel_profile_dir(path):
    possible_installation_location = Path(path).parents[2]
    possible_profile_dir = Path(possible_installation_location, "share", "ipykernel", "profile", "tablegpt")

    _startup_folder = Path(possible_profile_dir, "startup")
    try:
        if next(_startup_folder.glob(r"*-udfs.py")):
            return str(possible_profile_dir)
    except StopIteration:
        return None


try:
    DEFAULT_TABLEGPT_IPYKERNEL_PROFILE_DIR: str | None = next(
        filter(_find_tablegpt_ipykernel_profile_dir, possible_installation_locations)
    )

except StopIteration:
    # Means not found.
    msg = """Unable to find tablegpt ipykernel. If you need to use a local kernel,
please use `pip install -U tablegpt-agent[local]` to install the necessary dependencies.
For more issues, please submit an issue to us https://github.com/tablegpt/tablegpt-agent/issues."""
    warnings.warn(msg, stacklevel=2)
    DEFAULT_TABLEGPT_IPYKERNEL_PROFILE_DIR = None
