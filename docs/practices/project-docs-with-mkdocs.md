# Creating Project Documentation with MkDocs

MkDocs is a lightweight, fast documentation generator that converts Markdown files into a clean, professional documentation website.
This project illustrates all the required pieces and how they work together.

To enable:

From your GitHub project repo, click "Settings" tab (far right), and / Pages / Build and deployment / Set Source to `GitHub Actions`.

## 1. Adding MkDocs and Theme to a Project

MkDocs and its extensions are listed in `pyproject.toml` under the **docs** optional group.
These are installed when we run `uv sync --extra dev --extra docs --upgrade`.

## 2. Project Structure

By convention, MkDocs uses a top-level `docs/` folder for Markdown pages and a root-level `mkdocs.yml` file for configuration.

- **`docs/`** - all Markdown pages live here
- **`mkdocs.yml`** - defines site name, links, navigation, and theme settings

## 3. Example `mkdocs.yml` Configuration

At the top of the provided `mkdocs.yml`, update it to reference **your** GitHub username and repo name (and then delete the TODO entries).

```yaml
# mkdocs.yml
# Configuration file for MkDocs (Automated project documentation generator)

# TODO: Change denisecase to your GitHub username (use CTRL F to find all instances)
# TODO: Change smart-sales-example to your repository name (use CTRL F to find all instances)
# TODO: Update site_description
# TODO: Update site_author

site_name: Professional Analytics Project
site_url: https://denisecase.github.io/smart-sales-example/
repo_url: https://github.com/denisecase/smart-sales-example
site_description: Professional Python project demonstrating industry best practices
site_author: Denise Case
docs_dir: docs
site_dir: site
```

Then edit the **nav** section at the end to show the pages you want included:

```yaml
nav:
  - Home: index.md
  - API: api.md

  - Project Guides:
      - (Optional) Finalize Warehouse: guide/finalize-datawarehouse.md
      - Reporting with Power BI: guide/reporting-with-powerbi.md
      - Reporting with Spark: guide/reporting-with-spark.md

  - Installs:
      - Power BI: installs/install-powerbi.md
      - Spark: installs/install-spark.md
      - uv: installs/install-uv.md
      - DuckDB: installs/working-with-duckdb.md
      - SQLite: installs/working-with-sqlite.md

  - Professional Practices:
      - GH Actions: practices/intro-github-actions.md
      - MkDocs: practices/project-docs-with-mkdocs.md

  - Reference:
      - Star Schema: reference/star-schema.md
```

Delete, add, or reorganize pages as you like.
For a minimal project site, you might keep just:

```yaml
nav:
  - Home: index.md
  - API: api.md
```

## 4. Creating Documentation Pages

Each page is a standard Markdown file.
Use sections, examples, and headings to structure content.

**IMPORTANT:**
The provided `api.md` page automatically documents Python code by reading docstrings and signatures through `mkdocstrings`.
This gives your project professional-grade API documentation without extra work.

## 5. After Changes, Build and Preview

Build and preview documentation:

```shell
uv run mkdocs build --strict
uv run mkdocs serve
```

- The **build** step shows errors and inconsistencies (missing pages, bad links, formatting issues).
- The **serve** step launches a local preview server with live reload.

## 6. Automatic Deployment (to GitHub Pages)

This project includes a GitHub Action (.github\workflows\deploy-docs.yml) that automatically builds and deploys documentation to GitHub Pages on every push.

The project site will be available at <https://<your-username>.github.io/<your-repo-name>/>

For example, this example project documentation is available at <https://denisecase.github.io/smart-sales-example/>.

## 7. Optional/Recommended: Link to Docs on Home Page

We recommend using the GitHub Repository **About** box to link to your documentation.
Click the gear icon and check the box to use your Use your GitHub Pages website.
Add a short description and topics for a professional touch.

[About](../images/RepoAbout.png)
