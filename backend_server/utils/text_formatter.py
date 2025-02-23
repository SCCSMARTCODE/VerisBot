import textwrap
import re

def format_response(text: str, width: int = 80) -> str:
    """
    Formats the chatbot's generated text for a consistent and professional frontend display.

    This function performs the following steps:
      1. Strips leading and trailing whitespace.
      2. Normalizes newlines by reducing multiple blank lines to a standard double newline.
      3. Detects and preserves bullet lists or numbered lists, wrapping each line appropriately.
      4. Wraps each paragraph to a specified width for readability.

    Args:
        text (str): The raw generated text from the model.
        width (int, optional): The maximum line width. Defaults to 80.

    Returns:
        str: The formatted text.
    """
    text = text.strip()
    text = re.sub(r'\n\s*\n+', '\n\n', text)

    paragraphs = text.split("\n\n")
    formatted_paragraphs = []

    for paragraph in paragraphs:
        if re.match(r'^(\d+\.|\-|\*)\s+', paragraph):
            lines = paragraph.split('\n')
            formatted_lines = []
            for line in lines:
                match = re.match(r'^(\d+\.|\-|\*)\s+(.*)', line)
                if match:
                    bullet, content = match.groups()
                    wrapped_content = textwrap.fill(
                        content,
                        width=width,
                        subsequent_indent=" " * (len(bullet) + 1)
                    )
                    formatted_line = f"{bullet} {wrapped_content}"
                    formatted_lines.append(formatted_line)
                else:
                    formatted_lines.append(line)
            formatted_paragraphs.append("\n".join(formatted_lines))
        else:
            formatted_paragraphs.append(textwrap.fill(paragraph, width=width))

    formatted_text = "\n\n".join(formatted_paragraphs)
    return formatted_text