import yaml


def load_yaml(file_name: str) -> dict:
    """
        Load the file as Json then return the content as a dict
    """
    with open(file_name, 'r') as fd:
        return yaml.load(fd)
