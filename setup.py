from setuptools import setup, find_packages

setup(
    name="update-vscode-cpp",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    package_data={},
    author="Isaac True",
    author_email="isaac@is.having.coffee",
    description="Updates VSCode CPP symbols from the local .config file",
    python_requires='>=3.4',
)
