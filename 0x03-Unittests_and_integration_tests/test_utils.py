#!/usr/bin/env python3
"""A module for testing the utils module.
"""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for testing the `access_nested_map` function.

    This class contains test methods for both the expected output and exception cases of the `access_nested_map` function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """
        Test method for testing the expected output of the `access_nested_map` function.

        Args:
            nested_map (Dict): The nested map to be accessed.
            path (Tuple[str]): The path to the desired value in the nested map.
            expected (Union[Dict, int]): The expected output value.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """
        Test method for testing the exception cases of the `access_nested_map` function.

        Args:
            nested_map (Dict): The nested map to be accessed.
            path (Tuple[str]): The path to the desired value in the nested map.
            exception (Exception): The expected exception type.

        Returns:
            None
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)