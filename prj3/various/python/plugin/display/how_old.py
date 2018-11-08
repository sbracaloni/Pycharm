from plugin.base import Plugin


class HowOldAreYouPlugin(Plugin):
    def run(self) -> str:
        age = input('How old are you?')
        print(f'You are {age}')
