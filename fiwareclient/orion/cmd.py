from pprint import pformat
import json

from cliff.command import Command
from cliff.lister import Lister

from fiwareclient.orion.model.attribute import Attribute
from fiwareclient.orion.model.metadata import Metadata
from fiwareclient.orion.v2.client import OrionClient


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
        oc = OrionClient(fs=parsed_args.fs, fsp=parsed_args.fsp)
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
        parser.add_argument('attributes', help="Attributes")
        parser.add_argument('-fs', default="", help='FIWARE Service')
        parser.add_argument('-fsp', default="", help='FIWARE Service Path')

        return parser

    def take_action(self, parsed_args):
        print("test")
        result = self.create_entity(parsed_args)
        return result

    def create_entity(self, parsed_args):
        attributes = self.parse_attributes(parsed_args.attributes)
        print(attributes)
        #oc = OrionClient(fs=parsed_args.fs, fsp=parsed_args.fsp)
        #oc.entity_create(parsed_args.entity_id,
        #                 parsed_args.entity_type,
        #                 attributes)

    def parse_attributes(self, attrs_json):
        parsed_list = []
        attrs_dict = json.loads(attrs_json)
        for attr_name in attrs_dict:
            metadata = None
            if attrs_dict[attr_name].get('metadata'):
                metadata = self.parse_metadata(
                               attrs_dict[attr_name].get('metadata')
                           )
            attribute = Attribute(attr_name, attrs_json[attr_name],
                                  attrs_json[attr_name].attr_type,
                                  attrs_json[attr_name].attr_value,
                                  metadata)
            print(attribute.json())
            parsed_list.append(attribute)
        #for attr_name in attrs.keys():
        #    metadata_obj = Metadata()
        #    for metadata in attrs[attr_name]["metadata"]:
        #        metadata_obj.add_metadata(attrs[attr_name]["metadata"]["name"],
        #                                  attrs[attr_name]["metadata"]["type"],
        #                                  attrs[attr_name]["metadata"]["value"])
        #    attribute = Attribute(attr_name, attrs[attr_name]["type"], attrs[attr_name]["value"], metadata)
        #    attrs_list.append(attribute)
        return parsed_list

    def parse_metadata(self, metadata_dict):
        metadata = Metadata()
        for metadata_name in metadata_dict:
            metadata.add_metadata(metadata_name,
                                  metadata_dict[metadata_name]["type"],
                                  metadata_dict[metadata_name]["value"])
        return metadata
