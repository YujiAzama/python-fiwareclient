from fiwareclient.orion.model.attribute import Attribute
from fiwareclient.orion.model.metadata import Metadata


class Parser(object):

    def dict_to_attribute(self, dict_attr):
        attr_name = list(dict_attr.keys())[0]
        attr_type = dict_attr[attr_name]["type"]
        attr_value = dict_attr[attr_name]["value"]
        metadatas = []
        if dict_attr[attr_name].get("metadata"):
            for metadata in dict_attr[attr_name]["metadata"].keys():
                metadatas.append(
                    Metadata(metadata,
                             dict_attr[attr_name]["metadata"][metadata]["type"],
                             dict_attr[attr_name]["metadata"][metadata]["value"]))
        attr = Attribute(attr_name, attr_type, attr_value, metadatas)
        
        return attr

    def dict_to_metadata(self):
        pass


if __name__ == "__main__":
    dict_attr = {
        "temperture": {
            "value": "25",
            "type": "Number",
            "metadata": {
                "timestamp": {
                    "value": "2018",
                    "type": "Date"
                }
            }
        }
    }

    parser = Parser()
    attribute = parser.dict_to_attribute(dict_attr)
    print(attribute.json())
