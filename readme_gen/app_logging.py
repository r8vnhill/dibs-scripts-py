"""Logging setup helpers for the README generator."""

import logging


def setup_logging(verbose: bool) -> logging.Logger:
    """
    Configure and return the module logger based on verbosity.

    Args:
        verbose (bool): If True, set logging level to DEBUG, else WARNING.

    Returns:
        logging.Logger: Configured logger instance.
    """
    level = logging.DEBUG if verbose else logging.WARNING
    logging.basicConfig(level=level, format="%(message)s")
    return logging.getLogger(__name__)
