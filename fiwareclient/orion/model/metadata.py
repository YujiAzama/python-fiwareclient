class Metadata(object):
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

    def json(self):
        return {
                "metadata": {
                    self.name: {
                        self.value,
                        self.type
                    }
                }
            }


if __name__ == '__main__':
    metadata1 = Metadata("timestamp", "date", "2018/10/01 12:48.010")
    metadata2 = Metadata("unit", "string", "degree")
    print(metadata1.json())
    print(metadata2.json())
