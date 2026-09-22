"""Text utilities."""


def clean_name(raw):
    """Clean and standardize a person's name."""
    return " ".join(raw.split()).title()
