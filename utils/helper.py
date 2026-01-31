# -*- coding: utf-8 -*-

def save_html_to_file(html_content: str, filename: str) -> None:
    """
    Save HTML content into a file.

    Args:
        html_content (str): Raw HTML string.
        filename (str): Output file path ending with .html
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)


