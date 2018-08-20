import sys
import logging

from cliff.app import App
from cliff.commandmanager import CommandManager


class FiwareShell(App):

    def __init__(self):
        super(FiwareShell, self).__init__(
                description='Fiware Client',
                version='0.1.0',
                command_manager=CommandManager('fiwareclient.command'),
        )


def main(argv=sys.argv[1:]):
    fiware_shell = FiwareShell()
    return fiware_shell.run(argv)
