# test_rabbitqueue.py
"""
Tests for RabbitQueue module.
"""

import unittest
from rabbitqueue import RabbitQueue

class TestRabbitQueue(unittest.TestCase):
    """Test cases for RabbitQueue class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RabbitQueue()
        self.assertIsInstance(instance, RabbitQueue)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RabbitQueue()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
