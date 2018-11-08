from plugin.base import Plugin

class WhatIsYourNamePlugin(Plugin):
    def run(self) -> str:
        name = input('what is your name?')
        print(f'Hi {name}')

