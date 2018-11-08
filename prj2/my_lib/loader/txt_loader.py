def load_text(file_name: str) -> str:
    """
        Open the file then return its content as string
    """
    with open(file_name, 'r') as fd:
        return fd.read()
