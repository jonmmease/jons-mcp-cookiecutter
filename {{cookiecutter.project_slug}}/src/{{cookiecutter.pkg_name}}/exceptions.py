"""Exceptions for {{ cookiecutter.project_name }}."""


class ServerError(Exception):
    """Base exception for server errors.

    Attributes:
        message: Human-readable error description
        is_retryable: Whether the error might succeed on retry
    """

    def __init__(
        self,
        message: str,
        is_retryable: bool = False,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.is_retryable = is_retryable

    def __str__(self) -> str:
        return self.message


class NotInitializedError(Exception):
    """Raised when the server is not properly initialized."""

    pass
