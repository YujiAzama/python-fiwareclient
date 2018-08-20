from fiwareclient.orion.model.metadata import Metadata


class Attribute(object):
    def __init__(self, attr_name, attr_type, attr_value, metadata=[]):
        self.attr_name = attr_name
        self.attr_type = attr_type
        self.attr_value = attr_value
        self.metadata = metadata

    def json(self):
        attr = {self.attr_name: {
                    "type": self.attr_type,
                    "value": self.attr_value}}
        if len(self.metadata):
            attr[self.attr_name].update({"metadata": self.metadata_formatter(self.metadata)})

        return attr

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
