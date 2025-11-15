# Introduction to GitHub Actions

GitHub Actions allows projects to run automated tasks whenever code is committed and pushed to GitHub.
This project includes two simple workflow examples to illustrate the basics.
To learn more, research "CI/CD".

## Automation Benefits

Automated workflows help ensure:

- Code is checked for quality
- Documentation is rebuilt and published
- Tests run consistently across environments

GitHub Actions come with GitHub and no extra tools are required.

## Project Workflow 1: Continuous Integration

Located at: `.github/workflows/ci.yml`

This workflow runs automatically on every push. It:

- Sets up Python
- Installs the project using `uv`
- Runs linting
- Runs tests with `pytest`

This ensures the project builds correctly and the code remains reliable.

## Project Workflow 2: Documentation Deployment

Located at: `.github/workflows/deploy-docs.yml`

This workflow:

- Builds project documentation with MkDocs
- Publishes it automatically to **GitHub Pages**

## Working with Actions

To view workflow runs:

- Open your repository on GitHub
- Click **Actions** in the top menu
- Select any workflow run to see logs and details

## Optional/Recommended: README.md badges

We recommend adding these badges to your README.md right after the title.
Change YOURACCOUNT to your GitHub account name, and YOURREPO to your repository name.

[![CI Status](https://github.com/YOURACCOUNT/YOURREPO/actions/workflows/ci.yml/badge.svg)](https://github.com/YOURACCOUNT/YOURREPO/actions/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/docs-mkdocs--material-blue)](https://YOURACCOUNT.github.io/YOURREPO/)


## Local Automation: pre-commit Hooks

GitHub Actions run **after** you push code.
`pre-commit` runs **before** your code is committed, helping catch issues early.

This project includes a `.pre-commit-config.yaml` file with formatting and lint checks.

Install the hooks after creating your virtual environment:

```bash
uv run pre-commit install
```

Update hooks periodically:

```bash
uvx pre-commit autoupdate
```

Run all checks manually:

```bash
uv run pre-commit run --all-files
```

Using both **pre-commit (local)** and **GitHub Actions (remote)** provides a professional-quality workflow.
Together, they help catch issues *before* code reaches the main branch and ensure that the  project remains clean, consistent, and reliable.

Automation takes a little time to learn, but returns significant long-term benefits.
