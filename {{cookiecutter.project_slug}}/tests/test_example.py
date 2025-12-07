"""Tests for example tools."""

import pytest

from {{ cookiecutter.pkg_name }}.tools import hello_world


@pytest.mark.asyncio
async def test_hello_world_default() -> None:
    """Test hello_world with default argument."""
    result = await hello_world()
    assert result == "Hello, World! Your MCP server is working."


@pytest.mark.asyncio
async def test_hello_world_with_name(sample_name: str) -> None:
    """Test hello_world with a custom name."""
    result = await hello_world(sample_name)
    assert sample_name in result
    assert "Hello" in result
    assert "MCP server is working" in result


@pytest.mark.asyncio
async def test_hello_world_empty_name() -> None:
    """Test hello_world with empty string."""
    result = await hello_world("")
    assert result == "Hello, ! Your MCP server is working."
