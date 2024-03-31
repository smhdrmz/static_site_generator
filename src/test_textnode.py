import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_none_url(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_eq_dif_type(self):
            node = TextNode("This is a text node", "italic", None)
            node2 = TextNode("This is a text node", "bold", None)
            self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()