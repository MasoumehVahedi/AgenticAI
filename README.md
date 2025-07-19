


## 🛠 Installation and Sync Setup

To install [`uv`](https://github.com/astral-sh/uv), a fast Python package manager:

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then, verify installation:

```bash
which uv
uv --version
```

To ensure the binary is accessible, make sure this is in your shell config (e.g., ~/.zshrc or ~/.bash_profile):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Reload your shell:

```bash
source ~/.zshrc  # or source ~/.bash_profile
```

## Syncing Environment with uv sync

Run:

```bash
uv sync
```

This command does the following:

- Reads our pyproject.toml (our project’s dependency specification)

- Uses .python-version to determine the Python version (if available)

- Creates or updates uv.lock with resolved package versions

- Installs all required dependencies into a managed environment

It’s like a faster, smarter replacement for pip install + virtualenv + pip-tools.












