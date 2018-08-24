from pprint import pformat
import json

from cliff.command import Command
from cliff.lister import Lister

from fiwareclient.orion.model.attribute import Attribute
from fiwareclient.orion.model.metadata import Metadata
from fiwareclient.orion.v2.client import OrionClient
from fiwareclient.lib.config import Config
from fiwareclient.lib.parser import Parser


class EntityList(Lister):
    "Orion Entity List"

    def get_parser(self, prog_name):
        parser = super(EntityList, self).get_parser(prog_name)

        parser.add_argument('-fs', default="", help='FIWARE Service')
        parser.add_argument('-fsp', default="", help='FIWARE Service Path')

        return parser

    def take_action(self, parsed_args):
        result = self.list_entities(parsed_args)

        return result

    def list_entities(self, parsed_args):
        config = Config()
        oc = OrionClient(host=config.orion.host,
                         port=config.orion.port,
                         fs=parsed_args.fs,
                         fsp=parsed_args.fsp)
        entities = oc.entities_list()
        return (('Entity ID', 'Entity Type', 'Attributes'),
                ((entity.entity_id,
                  entity.entity_type,
                  pformat(entity.get_attributes_json(),
                          depth=None,
                          width=80,
                          indent=1)) for entity in entities)
               )


class EntityCreate(Command):
    "Orion Entity Create"

    def get_parser(self, prog_name):
        parser = super(EntityCreate, self).get_parser(prog_name)
        parser.add_argument('entity_id', help="Entity ID")
        parser.add_argument('entity_type', help="Entity Type")
        parser.add_argument('attributes', help="Attribute")
        parser.add_argument('-fs', default="", help='FIWARE Service')
        parser.add_argument('-fsp', default="", help='FIWARE Service Path')

        return parser

    def take_action(self, parsed_args):
        result = self.create_entity(parsed_args)
        return result

    def create_entity(self, parsed_args):
        attributes = self.parse_attributes(parsed_args.attributes)
        config = Config()
        oc = OrionClient(host=config.orion.host,
                         port=config.orion.port,
                         fs=parsed_args.fs,
                         fsp=parsed_args.fsp)
        oc.entity_create(parsed_args.entity_id,
                         parsed_args.entity_type,
                         attributes)

    def parse_attributes(self, attrs_json):
        parsed_list = []
        attrs_dict = json.loads(attrs_json)
        for attr_name, v in attrs_dict.items():
            parser = Parser()
            attribute = parser.dict_to_attribute({attr_name: v})
            parsed_list.append(attribute)
        return parsed_list

    def parse_metadata(self, metadata_dict):
        metadata = Metadata()
        for metadata_name in metadata_dict:
            metadata.add_metadata(metadata_name,
                                  metadata_dict[metadata_name]["type"],
                                  metadata_dict[metadata_name]["value"])
        return metadata


class EntityDelete(Command):
    "Orion Entity Delete"

    def get_parser(self, prog_name):
        parser = super(EntityDelete, self). get_parser(prog_name)
        parser.add_argument('entity_id', help="Entity ID")
        parser.add_argument('-fs', help="FIWARE Service")
        parser.add_argument('-fsp', help="FIWARE Service Path")

        return parser

    def take_action(self, parsed_args):
        result = self.delete_entity(parsed_args)
        return result

    def delete_entity(self, parsed_args):
        config = Config()
        oc = OrionClient(host=config.orion.host,
                         port=config.orion.port,
                         fs=parsed_args.fs,
                         fsp=parsed_args.fsp)
        entities = oc.entity_delete(parsed_args.entity_id)
