import json


def load_json(file_name: str) -> dict:
    """
        Load the file as Json then return the content as a dict
    """
    with open(file_name, 'r') as fd:
        return json.load(fd)
