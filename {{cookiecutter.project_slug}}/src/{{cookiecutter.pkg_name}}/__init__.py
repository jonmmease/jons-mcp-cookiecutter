"""{{ cookiecutter.project_name }}."""

from .server import main, mcp
from .tools import hello_world

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "main",
    "mcp",
    "hello_world",
]
