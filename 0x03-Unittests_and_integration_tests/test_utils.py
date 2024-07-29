#!/usr/bin/env python3
"""unit test"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    A test case class for the access_nested_map function.
    """

    @parameterized.expand([
        {"nested_map": {"a": 1}, "path": ("a",), "result": 1},
        {"nested_map": {"a": {"b": 2}}, "path": ("a",), "result": {"b": 2}},
        {"nested_map": {"a": {"b": 2}}, "path": ("a", "b"), "result": 2}
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """
        Test the access_nested_map function.

        Args:
            nested_map (dict): The nested map to access.
            path (tuple): The path to the desired value.
            result: The expected result.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), result)