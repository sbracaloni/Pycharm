from typing import List

from plugin.base import Plugin
from plugin.display.how_old import HowOldAreYouPlugin
from plugin.display.name import WhatIsYourNamePlugin

from my_lib.helper import print_hello, print_goodbye


class TalkUser:
    def __init__(self, plugins: List[Plugin]):
        self.plugins = plugins

    def run(self):
        print_hello()

        for plugin in self.plugins:
            plugin.run()

        print_goodbye()


if __name__ == '__main__':
    plugins = [
        HowOldAreYouPlugin(),
        WhatIsYourNamePlugin()
    ]
    TalkUser(plugins).run()
