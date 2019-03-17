import requests
import json
from pprint import pprint

from fiwareclient.orion.model.attribute import Attribute
from fiwareclient.orion.model.entity import Entity
from fiwareclient.orion.model.metadata import Metadata


class OrionClient(object):

    def __init__(self, host="localhost", port=1026,
                 tls=False, fs="", fsp=""):
        schema = "https://" if tls else "http://"
        self.base_url = schema + host + ":" + str(port) + "/v2"
        self.headers = {
            'Fiware-Service': fs,
            'Fiware-ServicePath': fsp
        }

    def entities_list(self):
        url = self.base_url + '/entities'
        response = requests.get(url, headers=self.headers)
        entities = []
        for entity in response.json():
            entities.append(self._dict_to_entity_object(entity))

        return entities

    def entity_show(self, entity_id):
        url = self.base_url + '/entities/' + entity_id
        response = requests.get(url, headers=self.headers)
        return self._dict_to_entity_object(response.json())

    def entity_create(self, entity_id, entity_type, attributes):
        entity = Entity(entity_id, entity_type)
        for attribute in attributes:
            entity.add_attribute(attribute)
        url = self.base_url + '/entities'
        header = {'Content-Type': 'application/json',
                  'Accept': 'application/json'}
        header.update(self.headers)
        response = requests.post(url, headers=header,
                                 data=json.dumps(entity.json()))

    def update_entity(self, entity_id, attrs):
        body = {}
        url = self.base_url + '/entities/' + entity_id + '/attrs'
        header = {'Content-Type': 'application/json'}
        for attr in attrs:
            body.update(attr.json())
        header.update(self.headers)
        response = requests.patch(url, headers=header,
                                  data=json.dumps(body))

    def entity_delete(self, entity_id):
        url = self.base_url + '/entities/' + entity_id
        response = requests.delete(url, headers=self.headers)

    def attribute_data_update(self, entity_id, attr_name, attr_value):
        url = (self.base_url + '/entities/' + entity_id
               + '/attrs/' + attr_name + '/value')
        header = {'Content-Type': 'text/plain'}
        header.update(self.headers)
        response = requests.put(url, headers=header,
                                  data=str(attr_value))

    def attribute_data_get(self, entity_id, attribute_name):
        url = self.base_url + '/entities/' + entity_id + '/attrs/' \
                  + attribute_name + '/value'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def _dict_to_entity_object(self, entity_dict):
        entity = Entity(entity_dict.pop("id"),
                        entity_dict.pop("type"))

        for attr_name in entity_dict:
            metadatas = []
            metadata_dict = entity_dict[attr_name].get("metadata")
            for metadata in metadata_dict:
                metadatas.append(
                    Metadata(metadata,
                             metadata_dict[metadata]["type"],
                             metadata_dict[metadata]["value"]
                ))

            attr = Attribute(attr_name,
                             entity_dict[attr_name].pop("type"),
                             entity_dict[attr_name].pop("value"),
                             metadatas)

            entity.add_attribute(attr)

        return entity


if __name__ == '__main__':
    client = OrionClient(host='118.27.13.26', fs='test', fsp='/test')
    entities = client.entities_list()
    #for entity in entities:
    #    pprint(entity.json())

    #entity = client.entity_show("sensor1")
    #print(entity.attributes[0].metadata.metadata)

    attr = Attribute("temp", "number", "15.5")
    #client.entity_create("room1", "Room", [attr])

    #client.attribute_data_update('room1', 'temp', 20)
    client.update_entity('room1', [attr])
    value = client.attribute_data_get('room1', 'temp')
    print(value)
