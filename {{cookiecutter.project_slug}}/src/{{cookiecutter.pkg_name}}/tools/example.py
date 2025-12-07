"""Example MCP tool for {{ cookiecutter.project_name }}."""


async def hello_world(name: str = "World") -> str:
    """Return a friendly greeting.

    This is an example tool that demonstrates the basic pattern for
    creating MCP tools with FastMCP. The docstring here becomes the
    tool's description in the MCP protocol.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        A greeting message.
    """
    return f"Hello, {name}! Your MCP server is working."
