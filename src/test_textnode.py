
import unittest

from textnode import TextNode
from htmlnode import *


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

        thing = TextNode(text='Well `shoot`, dangit', text_type='link')
        thing2 = TextNode(text='`Shoot` ````*well*, thanks', text_type='link')
        thing3 = LeafNode()
        hold = TextNode.split_nodes_delimiter([thing, thing2, thing3], '`', "code")
        self.assertEqual(len(hold), 7)

        thing4 = TextNode(text='', text_type='text')
        hold2 = TextNode.split_nodes_delimiter([thing4],'**', 'bold')
        self.assertEqual(hold2, [])

        thing5 = TextNode(text=' the way **forward** is back', text_type='bold')
        thing6 = TextNode(text='No, the *other* way', text_type='italic')
        hold3 = TextNode.split_nodes_delimiter([thing5, thing6], '**', 'bold')
        hold4 = TextNode.split_nodes_delimiter([thing5, thing6], '*', text_type='italic')


if __name__ == "__main__":
    unittest.main()
