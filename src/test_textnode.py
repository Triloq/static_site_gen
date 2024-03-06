
import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        node3 = TextNode("Fruits taste better than veges", "italics", "www.bro.com")
        node4 = TextNode("Fruits taste better than veges", "italics", "www.bro.com")
        self.assertEqual(node3, node4)
        node5 = TextNode("This isn't right", "bold")
        node6 = TextNode("This is right", "bold")
        self.assertNotEqual(node5, node6)
        node7 = TextNode("This is a text node", "bold")
        node8 = TextNode("This is a text node", "italics")
        self.assertNotEqual(node7, node8)


if __name__ == "__main__":
    unittest.main()
