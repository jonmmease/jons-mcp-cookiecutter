# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

A FastMCP server that exposes tools through the Model Context Protocol (MCP).

## Requirements

- Python 3.10+

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd {{ cookiecutter.project_slug }}

# Install with uv
uv pip install -e .
```

## Running the Server

```bash
uv run {{ cookiecutter.project_slug }}
```

## Adding to Claude Code

```bash
# Register the MCP server with Claude Code
claude mcp add {{ cookiecutter.project_slug }} -- uv run --directory /path/to/{{ cookiecutter.project_slug }} {{ cookiecutter.project_slug }}
```

## Available Tools

| Tool | Description |
|------|-------------|
| `hello_world` | Returns a friendly greeting (example tool) |

## Development

### Setup

```bash
# Install with dev dependencies
uv pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src

# Run a specific test
uv run pytest tests/test_example.py::test_hello_world_default
```

### Code Quality

```bash
# Type check
uv run mypy src/{{ cookiecutter.pkg_name }}

# Format code
uv run black src tests

# Lint code
uv run ruff check src tests
```

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── src/
│   ├── __init__.py
│   └── {{ cookiecutter.pkg_name }}/
│       ├── __init__.py          # Package exports
│       ├── constants.py         # Configuration constants
│       ├── exceptions.py        # Custom exceptions
│       ├── utils.py             # Utility functions
│       ├── server.py            # FastMCP server setup
│       └── tools/
│           ├── __init__.py      # Tool exports
│           └── example.py       # Example tool
├── tests/
│   ├── conftest.py              # Test fixtures
│   └── test_example.py          # Example tests
├── pyproject.toml               # Project configuration
├── CLAUDE.md                    # AI assistant guidance
└── README.md                    # This file
```

## Adding New Tools

1. Create a new file in `src/{{ cookiecutter.pkg_name }}/tools/` or add to an existing file
2. Write an async function with type hints and a docstring:
   ```python
   async def my_tool(param: str) -> str:
       """Brief description for the MCP tool listing.

       Args:
           param: What this parameter does.

       Returns:
           What the tool returns.
       """
       return f"Result: {param}"
   ```
3. Export from `src/{{ cookiecutter.pkg_name }}/tools/__init__.py`
4. Register in `server.py` with `mcp.tool(my_tool)`

## License

MIT
