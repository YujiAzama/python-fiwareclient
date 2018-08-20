import argparse
import pprint

from prettytable import PrettyTable

from fiwareclient.orion.v2.client import OrionClient


class FiwareContextBrokerShell(object):

    def __init__(self, parser=None):
        self.parser = self.build_parser(parser=parser)

    def build_parser(self, parser=None):
        cb_
        if parser:
            parser = parser.add_(help='orion command')
            parser.add_argument('resource', help='resource')
        return cb_parser

    def get(self):
        entities = self.oc.get_entities()
        table = PrettyTable(['Entity ID', 'Entity Type', 'Attributes'])
        table.align['Attributes'] = 'l'
        for entity in entities:
            table.add_row([entity.pop('id'), entity.pop('type'), pprint.pformat(entity, depth=2, width=40, indent=2)])
        print(table)

    def run(self):
        self.oc = OrionClient(args.fs, args.fsp)
        if args.resource == 'entity' and args.command == 'list':
            self.get()


if __name__ == '__main__':
    fcbs = FiwareContextBrokerShell()
    fcbs.get()
