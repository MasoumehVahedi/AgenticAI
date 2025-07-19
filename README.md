


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


## 🔐 Set Up OpenAI API Key 

We can integrate this project with the OpenAI API.

### 1. Create/Open an OpenAI Account
Go to [https://platform.openai.com](https://platform.openai.com) and:
- Sign up or log in
- Navigate to **Settings → Billing** and top up your account (minimum $5)

### 2. Generate an API Key
- Go to **API Keys** in the settings menu
- Click **Create new secret key**
- Name it (any name)
- Choose **Default Project**
- Leave **All permissions** selected
- Click **Create Secret Key**

⚠️ **Important:** Copy our key immediately — we won't see it again!

Avoid pasting our key into editors that auto-format characters (like Microsoft Word or Notepad), which could break the key.

### 3. Store It in a `.env` File

Create a file called `.env` (note the leading dot) in our project root and add:

```env
OPENAI_API_KEY=your-key-here
```









