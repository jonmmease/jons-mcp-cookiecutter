"""FastMCP server for {{ cookiecutter.project_name }}."""

import argparse
import logging
import os
import signal
import sys
from typing import Any

from fastmcp import FastMCP

from .tools import hello_world

# Configure logging
logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Create FastMCP server instance
mcp = FastMCP(
    name="{{ cookiecutter.project_slug }}",
    instructions="""
{{ cookiecutter.description }}

## Available Tools

| Tool | Purpose |
|------|---------|
| hello_world | Example tool that returns a greeting |

## Getting Started

Call hello_world with a name to test the server is working.
""",
)

# Register tools
mcp.tool(hello_world)


# Signal handling for graceful shutdown
def signal_handler(signum: int, frame: Any) -> None:
    """Handle shutdown signals."""
    logger.info(f"Received signal {signum}, shutting down...")
    sys.exit(0)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="{{ cookiecutter.description }}"
    )
    parser.add_argument(
        "project_path",
        nargs="?",
        help="Path to the project (defaults to current directory)",
    )
    args = parser.parse_args()

    if args.project_path:
        logger.info(f"Starting server with project path: {args.project_path}")
    else:
        logger.info("Starting server with current directory")

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    mcp.run()


if __name__ == "__main__":
    main()
