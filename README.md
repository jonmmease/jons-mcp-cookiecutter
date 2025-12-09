# Python MCP Server Cookiecutter Template

This repository contains a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating Python-based MCP (Model Context Protocol) servers using FastMCP.

## Using This Template

### Option 1: Using uvx (Recommended)

The easiest way to use this template is with `uvx`, which runs cookiecutter without requiring a permanent installation:

```bash
# From a GitHub repository
uvx cookiecutter gh:jonmmease/jons-mcp-cookiecutter

# Or from a local clone
uvx cookiecutter /path/to/jons-mcp-cookiecutter
```

### Option 2: Install cookiecutter with uv

```bash
# Install cookiecutter as a tool
uv tool install cookiecutter

# Then run it
cookiecutter gh:YOUR_USERNAME/jons-mcp-cookiecutter
```

### Option 3: Using pip/pipx

```bash
# With pipx (recommended for CLI tools)
pipx install cookiecutter
cookiecutter gh:YOUR_USERNAME/jons-mcp-cookiecutter

# Or with pip
pip install cookiecutter
cookiecutter gh:YOUR_USERNAME/jons-mcp-cookiecutter
```

## Template Variables

When you run cookiecutter, you'll be prompted for these values:

| Variable | Description | Example |
|----------|-------------|---------|
| `project_name` | Human-readable project name | "My MCP Server" |
| `project_slug` | URL/directory-friendly name (auto-derived) | "my-mcp-server" |
| `pkg_name` | Python package name (auto-derived) | "my_mcp_server" |
| `description` | Brief project description | "An MCP server for..." |
| `author` | Your name | "Jane Doe" |
| `author_email` | Your email | "jane@example.com" |

The `project_slug` and `pkg_name` are automatically derived from `project_name`:
- `project_slug`: lowercase with hyphens (used for directory name, CLI command)
- `pkg_name`: lowercase with underscores (used for Python imports)

## After Generation

Once your project is created:

```bash
# Navigate to the new project
cd my-mcp-server

# Install dependencies
uv pip install -e ".[dev]"

# Run the server
uv run my-mcp-server

# Run tests
uv run pytest
```

### Adding to Claude Code

```bash
cd my-mcp-server
claude mcp add my-mcp-server -- uv run --project "$(pwd)" my-mcp-server
```

## What's Included

The generated project includes:

- **FastMCP server setup** with example tool
- **Project structure** following Python best practices (`src/` layout)
- **Test scaffold** with pytest and fixtures
- **Development tooling** configs (black, ruff, mypy, pytest)
- **CLAUDE.md** for AI assistant guidance
- **README.md** with usage instructions

## Customizing the Template

To modify this template:

1. Clone this repository
2. Edit files in `{{cookiecutter.project_slug}}/`
3. Use `{{ cookiecutter.variable_name }}` for template variables
4. Update `cookiecutter.json` to add/modify variables

## Template Structure

```
jons-mcp-cookiecutter/
├── README.md                    # This file (not copied to output)
├── cookiecutter.json            # Template variable definitions
└── {{cookiecutter.project_slug}}/   # Template directory
    ├── .gitignore
    ├── CLAUDE.md
    ├── README.md
    ├── pyproject.toml
    ├── src/
    │   ├── __init__.py
    │   └── {{cookiecutter.pkg_name}}/
    │       ├── __init__.py
    │       ├── constants.py
    │       ├── exceptions.py
    │       ├── server.py
    │       ├── utils.py
    │       └── tools/
    │           ├── __init__.py
    │           └── example.py
    └── tests/
        ├── __init__.py
        ├── conftest.py
        └── test_example.py
```

## License

MIT
