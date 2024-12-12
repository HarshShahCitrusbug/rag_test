from docx import Document


def get_text_from_docx(path: str) -> str:
    """
    Extracts and returns the text content from a DOCX file.

    This function opens a DOCX file specified by the `path`, reads its paragraphs,
    and returns a string containing the text of those paragraphs, separated by newlines.
    Empty paragraphs are ignored.

    :param path: Path to the DOCX file.
    :return: A string with the combined text of all non-empty paragraphs in the document.
    """
    document = Document(path)
    return "\n".join([data.text for data in document.paragraphs if data.text.strip() != ""])


def convert_text_into_chunks(text: str, chunk_size=1000) -> list:
    """
    Splits a given text into chunks of a specified maximum size.

    This function takes a text string and divides it into smaller chunks, 
    each with a maximum length specified by `chunk_size`. The text is split 
    into paragraphs, and paragraphs are grouped into chunks without exceeding 
    the specified size. This is useful for processing large texts in 
    manageable pieces.

    :param text: The input text to be split into chunks.
    :param chunk_size: The maximum size of each chunk, default is 1000.
    :return: A list of text chunks, each with a size up to `chunk_size`.
    """
    paragraphs = text.split('\n')
    chunks = []
    current_chunk = []
    current_chunk_length = 0

    for paragraph in paragraphs:
        if current_chunk_length + len(paragraph) <= chunk_size:
            current_chunk.append(paragraph)
            current_chunk_length += len(paragraph)
        else:
            chunks.append("\n".join(current_chunk))
            current_chunk = [paragraph]
            current_chunk_length = len(paragraph)

    if current_chunk:  # Add the last chunk if it's not empty
        chunks.append("\n".join(current_chunk))

    return chunks
