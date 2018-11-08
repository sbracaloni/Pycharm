from os.path import dirname, join

from my_lib.loader.specific.json_loader import load_json
from my_lib.loader.specific.yaml_loader import load_yaml
from my_lib.loader.txt_loader import load_text


def display_content(file_name: str):
    if file_name.endswith('.txt'):
        print('Text file:')
        txt_content = load_text(file_name)
        print(txt_content)
    elif file_name.endswith('.json'):
        print('Json file:')
        json_content = load_json(file_name)
        print(json_content)
    elif file_name.endswith('.yml'):
        print('Json file:')
        yaml_content = load_yaml(file_name)
        print(yaml_content)


if __name__ == '__main__':
    current_path = dirname(__file__)

    file_1 = join(current_path, '..', 'data', 'file.txt')
    display_content(file_1)

    file_2 = join(current_path, '..', 'data', 'file.specific')
    display_content(file_2)
