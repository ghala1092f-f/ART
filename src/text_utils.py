"""Utilities for cleaning text names."""


def clean_name(raw):
    """Collapse whitespace and convert a name to title case."""
    return " ".join(raw.split()).title()
