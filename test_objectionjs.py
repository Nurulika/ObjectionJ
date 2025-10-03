# test_objectionjs.py
"""
Tests for ObjectionJS module.
"""

import unittest
from objectionjs import ObjectionJS

class TestObjectionJS(unittest.TestCase):
    """Test cases for ObjectionJS class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ObjectionJS()
        self.assertIsInstance(instance, ObjectionJS)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ObjectionJS()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
