import unittest
import psycopg2
from unittest.mock import Mock
from connection_pool import ConnectionPool, DBConnection

class TestConnectionPool(unittest.TestCase):
    def setUp(self):
        # create a mock object for the connect function
        connect_mock = Mock()

        # assign the mock connect function as an attribute of the psycopg2 module
        psycopg2.connect = connect_mock

        # create a mock object for the connection
        connection_mock = Mock()

        # assign the mock connection object as the return value of the connect function
        connect_mock.return_value = connection_mock

        # create a mock object for the cursor
        cursor_mock = Mock()

        # assign the mock cursor object as an attribute of the connection mock object
        connection_mock.cursor = cursor_mock

        # patch the psycopg2 module
        self.psycopg2_patch = unittest.mock.patch(psycopg2)
        self.psycopg2_patch.start()

        # create an instance of the ConnectionPool class
        self.pool = ConnectionPool()

    def tearDown(self):
        # stop patching the psycopg2 module
        self.psycopg2_patch.stop()

    def test_connection_pool_is_a_dict(self):
        # test that the connection_pool attribute is a dictionary
        self.assertIsInstance(self.pool.connection_pool, dict)

    def test_connection_pool_has_available_and_used_keys(self):
        # test that the connection_pool dictionary has 'available' and 'used' keys
        self.assertIn('available', self.pool.connection_pool)
        self.assertIn('used', self.pool.connection_pool)

    def test_available_and_used_are_empty_lists(self):
        # test that the 'available' and 'used' keys in the connection_pool dictionary map to empty lists
        self.assertIsInstance(self.pool.connection_pool['available'], list)
        self.assertIsInstance(self.pool.connection_pool['used'], list)
        self.assertEqual(len(self.pool.connection_pool['available']), 0)
        self.assertEqual(len(self.pool.connection_pool['used']), 0)

    def test_connection_is_instance_of_DBConnection(self):
        # test that the connection attribute is an instance of DBConnection
        self.assertIsInstance(self.pool.connection, DBConnection)

if __name__ == '__main__':
    unittest.main()