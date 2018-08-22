import os


class Config(object):
    def __init__(self):
        self.orion = OrionConfig()


class OrionConfig(object):
    def __init__(self):
        self.host = os.getenv("ORION_HOST", "localhost")
        self.port = os.getenv("ORION_PORT", 1026)
