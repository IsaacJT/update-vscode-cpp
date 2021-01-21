# update-vscode-cpp

Updates VSCode CPP symbols from the local .config file.

Helpful for loading the current configuration for the Linux kernel into VSCode so that all symbols are automatically activated.

## Usage

Use pip to install:

    pip3 install --user .

Run in a folder containing both a `.config` and `.vscode/c_cpp_properties.json` file:

    python3 -m update-vscode-cpp.main
