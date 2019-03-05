from fiwareclient.orion.model.attribute import Attribute
from fiwareclient.orion.model.metadata import Metadata

class Entity(object):
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.attributes = []

    def add_attribute(self, attr):
        self.attributes.append(attr)

    def get_attribute(self, name):
        result = ""
        for attr in self.attributes:
            if attr.name == name:
                result = attr
        return result

    def get_attributes_json(self):
        attributes = {}
        for attr in self.attributes:
            attributes.update(attr.json())

        return attributes

    def json(self):
        entity = {
            "id": self.id,
            "type": self.type}
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
    print(entity.id)
    print(entity.type)
    print(entity.attributes[0].name)
