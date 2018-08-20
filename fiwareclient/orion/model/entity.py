from fiwareclient.orion.model.attribute import Attribute
from fiwareclient.orion.model.metadata import Metadata

class Entity(object):
    def __init__(self, entity_id, entity_type):
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.attributes = []

    def add_attribute(self, attr):
        self.attributes.append(attr)

    def get_attributes_json(self):
        attributes = {}
        for attr in self.attributes:
            attributes.update(attr.json())

        return attributes

    def json(self):
        entity = {
            "id": self.entity_id,
            "type": self.entity_type}
        for attr in self.attributes:
            entity.update(attr.json())
        return entity


if __name__ == "__main__":
    metadata1 = Metadata("timestamp", "date", "2018/10/01 12:48.010")
    metadata2 = Metadata("unit", "string", "degree")

    attr = Attribute("temp", "num", "28.5", [metadata1, metadata2])

    entity = Entity("sensor1", "Sensor")
    entity.add_attribute(attr)
    print(entity.json())
