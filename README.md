# FIWARE Client for Python

## Install

```bash
$ git clone http://github.com/YujiAzama/python-fiwareclient.git && cd python-fiwareclient
$ pip3 install -r requirements.txt
$ sudo python3 setup.py install
```

## Usage

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
