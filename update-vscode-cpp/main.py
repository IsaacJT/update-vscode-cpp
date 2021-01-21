#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from typing import Dict, Set
import json
import re
import sys

VSCODE_SETTINGS = os.path.join(os.getcwd(), ".vscode", "c_cpp_properties.json")
CONFIG_FILE = os.path.join(os.getcwd(), ".config")
CONFIG_RE = re.compile(r"^(CONFIG_[A-Z_]+)=(y|m)")


def load_vscode_settings() -> Dict:
    with open(VSCODE_SETTINGS, "r") as f:
        return json.load(f)


def save_vscode_settings(settings: Dict):
    with open(VSCODE_SETTINGS, "w") as f:
        json.dump(settings, f, indent=4)


def load_config() -> Set:
    with open(CONFIG_FILE, "r") as f:
        matches = [CONFIG_RE.match(line) for line in f.readlines()]
        return set([m.group(1) for m in matches if m is not None])


def main():
    config_symbols = load_config()
    current_settings = load_vscode_settings()
    if "configurations" not in current_settings:
        print("No configurations found; please first create a configuration in VSCode")
        sys.exit(-1)
    for config in current_settings["configurations"]:
        if "defines" not in config:
            config["defines"] = []
        current_symbols = set(config["defines"])
        updated_symbols = current_symbols.union(config_symbols)
        print("Added", len(updated_symbols) - len(current_symbols),
              "new symbols to configuration", config["name"])
        config["defines"] = list(updated_symbols)
    save_vscode_settings(current_settings)


if __name__ == "__main__":
    main()
