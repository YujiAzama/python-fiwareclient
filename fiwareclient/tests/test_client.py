from fiwareclient.orion.v2.client import OrionClient
from fiwareclient.orion.model.entity import Entity

import unittest
from unittest import mock


class MockResponse(object):
    def __init__(self, data, status_code):
        self.data = data
        self.status_code = status_code

    def json(self):
        return self.data


def mocked_requests_get(*args, **kwargs):
    return MockResponse([{"id": "Room01", "type": "Room"}], 200)


class TestOrionClient(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_entities_list(self, mock_get):
        oc = OrionClient()
        data = oc.entities_list()
        entity = data[0]
        self.assertEqual(entity.json(), {"id": "Room01", "type": "Room"})
