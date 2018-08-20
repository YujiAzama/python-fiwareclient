class Metadata(object):
    def __init__(self, metadata_name, metadata_type, metadata_value):
        self.metadata_name = metadata_name
        self.metadata_type = metadata_type
        self.metadata_value = metadata_value

    def json(self):
        return {"metadata": {
                    self.metadata_name: {
                        self.metadata_value,
                        self.metadata_type}}}


if __name__ == '__main__':
    metadata1 = Metadata("timestamp", "date", "2018/10/01 12:48.010")
    metadata2 = Metadata("unit", "string", "degree")
    print(metadata1.json())
    print(metadata2.json())
