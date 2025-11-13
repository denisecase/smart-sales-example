# 2. Set Up Project (Once per Project)

> Keep track of how long this takes, and if you encounter any issues and how you resolve them.
> Estimated time: about an hour

## Overview

We initialize Python project using modern tools:

- **Local project virtual environment (.venv)** to keep the project separate and reusable.
- **Pre-commit hooks** to catch common issues early.
- **Version control with Git** to track evolving project code like we do at work.
- **Dependency management with uv** - Fast, reliable tool replacing pip/conda in modern workplaces

Each step below illustrates how professional analysts initialize a new analytics project.

## Step 2.1. Copy This Repository on GitHub

1. Log in to **GitHub** in your browser.
2. Go to <https://github.com/denisecase/pro-analytics-02-starter>.
3. Click the green **Use this template** button → choose **Create a new repository**.
4. **Name your repository**
   - Use **all lowercase** and **dashes** between words.
   - Example: `data-project-01` or `ml-penguins`
5. Set visibility to **Public**.
6. Click **Create repository**.

## Step 2.2 Enable GitHub Pages (Recommended)

Before leaving GitHub, set up your repository to host your code documentation automatically.

1. In your new repository, click the **Settings** tab (top right).
2. In the left sidebar, select **Pages**.
3. Under **Source**, choose **GitHub Actions**.
4. Click the **Code** tab to return to the regular view.

GitHub will automatically build and publish your documentation when you push changes.

---

## Step 2.3. Clone Your Repo to Your Computer and Open In VS Code

1. Open VS Code
2. Press `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`)
3. Type "clone" and select "Git: Clone"
4. Paste your repository URL from GitHub
5. When asked where to save, navigate to your Repos folder:
   - Windows: `C:\Repos`
   - Mac/Linux: `~/Repos` (in your home folder)
6. Click "Select Repository Location"
7. When VS Code asks "Open Repository?" - click "Open"

<details>
<summary>Alternative: Clone using terminal</summary>

Copy your repository URL from GitHub's address bar.

**Windows (PowerShell):**

```powershell
cd C:\Repos
git clone YOUR_REPOSITORY_URL_HERE
cd your-repository-name
code .
```

**macOS / Linux:**

```bash
cd ~/Repos
git clone YOUR_REPOSITORY_URL_HERE
cd your-repository-name
code .
```

Replace `YOUR_REPOSITORY_URL_HERE` with your actual URL and `your-repository-name` with the name you chose in Step 2.1.

</details>

---

## Step 2.4. Install Recommended VS Code Extensions

When you first open this project, VS Code will prompt you to install recommended extensions. Click "Install All" to get Python support, Jupyter notebooks, linting, formatting, and Git integration. See `.vscode/extensions.json` for the complete list.

---

## Step 2.5. Set Up Virtual Environment (.venv)

Using your VS Code terminal, run the following commands to:

1. Create a local virtual environment using `uv venv`.
2. Pin a Python version. Version 3.12 is recommended for speed, stability, and current compatibility.
3. Install optional tools (for dev and docs) and update packages.
4. Install pre-commit so checks run automatically on each commit.
5. Verify the python version installed is 3.12 (not 3.13 or 3.14).
6. Finally, activate your environment (operating system specific).

```bash
uv venv
uv python pin 3.12
uv sync --extra dev --extra docs --upgrade
uv run pre-commit install
uv run python --version
```

**Windows (PowerShell):**

```bash
.\.venv\Scripts\activate
```

**macOS / Linux / WSL:**

```bash
source .venv/bin/activate
```

---

## Step 2.6. Git add-commit-push

Open a terminal in VS Code (PowerShell, zsh, or bash).

IMPORTANT: Replace the commit message with a clear and descriptive note about what you added or changed.
Wrap the commit message in double quotes.

```shell
git add .
git commit -m "Initialize from pro-analytics-02-starter (no local edits)"
git push -u origin main
```

We can then use `git push` for later commits.

NOTE: This will trigger the GitHub Actions workflow and publish your documentation via GitHub Pages.
This should verify things worked as provided.
If anything fails, let us know in the associated discussion.

---

## Step 2.7. Personalize Project Files

After verifying that the starter project works correctly, start to customize it.

1. Open `pyproject.toml` and update the `authors` field with your name.
2. Delete the TODO comment after making the change.
3. Open `mkdocs.yml` and update ALL of the following:
   - `site_name`: set a clear project name (e.g., `Professional Analytics Project`)
   - `site_url`: `https://YOUR_GITHUB_USERNAME.github.io/your-repository-name/`
   - `repo_url`: `https://github.com/YOUR_GITHUB_USERNAME/your-repository-name`
   - `site_description`: short sentence about your project
   - `site_author`: **your name**
4. (Optional) Use **Edit / Find** to search for `denisecase` and replace with your GitHub account name. Then search for `pro-analytics-02-starter` and replace with your repository name (which should use dashes).
5. Recommended: Use the menu **File / Autosave** to turn on automatic saving OR save all your changes (`Ctrl+S` on Windows / `Cmd+S` on Mac).

This will establish this as your project and personalize the associated documentation site, which will be automatically published by GitHub Actions.

---

## Step 2.8. Git add-commit-push

Open a terminal in VS Code (PowerShell, zsh, or bash).

```shell
git add .
git commit -m "Personalize pyproject authors and mkdocs site settings"
git push
```

Optional: Click the **Actions** tab to watch the build process in real time. Click the **Code** tab to return.

After the actions complete, your documentation site should be available at <https://YOUR_GITHUB_USERNAME.github.io/your-repository-name/>.
