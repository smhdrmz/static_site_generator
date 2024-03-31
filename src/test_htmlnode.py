import unittest
from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):

    def test_prop_to_html(self):
        node = HTMLNode("p", "this is a text", None, None)
        self.assertEqual(node)



if __name__ == "__main__":
    unittest.main()