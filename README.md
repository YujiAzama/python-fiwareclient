# FIWARE Client for Python

## Install

```bash
$ git clone http://github.com/YujiAzama/python-fiwareclient.git && cd python-fiwareclient
$ pip3 install -r requirements.txt
$ sudo python3 setup.py install
```

## Usage

### Use as a Python library

```python
# Create client
client = OrionClient(host='localhost', fs='', fsp='/')

# List entities
entities = client.entities_list()

# filtering by queries
entities = client.entities_list(payload={"q": "plantingTemperatureMin<30", "type": "Vegetable"})

# Create Attribute
attr = Attribute("temp", "number", "15.5")

# Update Attribute
client.update_entity('room1', [attr])

# Get Attribute value
value = client.attribute_data_get('room1', 'temp')
```

### CLI

```bash
$ fiware entity-list
```

If you have remote orion host, you specify host name as environment variable.

```bash
$ export ORION_HOST=orion-host
$ export ORION_PORT=1028
$ fiware entity-list
```

or

```bash
$ ORION_HOST=orion-host fiware entity-list
```
