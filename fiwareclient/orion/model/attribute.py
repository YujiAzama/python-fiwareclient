from fiwareclient.orion.model.metadata import Metadata


class Attribute(object):
    def __init__(self, name, type, value, metadata=[]):
        self.name = name
        self.type = type
        self.value = value
        self.metadata = metadata

    def json(self):
        attr = {
            self.name: {
                "type": self.type,
                "value": self.value
            }
        }
        if len(self.metadata):
            attr[self.name].update({"metadata": self.metadata_formatter(self.metadata)})

        return attr

    def get_metadata(self, name):
        result = ""
        for meta in self.metadata:
            if meta.name == name:
                result = meta
        return result

    def metadata_formatter(self, metadatas):
        formatted_metadata = {}
        for metadata in metadatas:
            formatted_metadata.update(
                {
                    metadata.metadata_name: {
                        "value": metadata.metadata_value,
                        "type": metadata.metadata_type
                    }
                }
            )
        return formatted_metadata


if __name__ == "__main__":
    metadata1 = Metadata("unit", "string", "degree")
    metadata2 = Metadata("timestamp", "date", "2018/10/01 12:48.010")
    metadatas = [metadata1, metadata2]
    attr = Attribute("temp", "num", "28.5", metadatas)
    print(attr.json())
    print(attr.name)
    print(attr.value)
    print(attr.type)
