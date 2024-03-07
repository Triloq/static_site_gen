import unittest

from htmlnode import *
from textnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        html1 = HTMLNode()
        html2 = HTMLNode()
        self.assertEqual(html1.props_to_html(), html2.props_to_html())
        html3 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        html4 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(html3.props_to_html(), html4.props_to_html())
        self.assertNotEqual(html4.props_to_html(), html1.props_to_html())

        leaf1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf1.to_html(), "<p>This is a paragraph of text.</p>")
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf2.to_html(), '<a href="https://www.google.com">Click me!</a>')

        parent1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            parent1.to_html(), 
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
        parent2 = ParentNode(
            "p",
            [
                LeafNode("h1", "In the Beginning"),
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "There wasn't a lot."),
                        LeafNode("b", "But then there was!"),
                        LeafNode("a", "Click here to see", {"href": "www.god.com"})
                    ],
                ),
                ParentNode(
                    "p",
                    [
                        LeafNode("a", "Do not click here, though.", {"href": "www.satan.com"})
                    ]
                )
            
            ],
            {"href": "www.heaven.com"}
        )
        self.assertEqual(
            parent2.to_html(),
            '<p href="www.heaven.com"><h1>In the Beginning</h1><p>There wasn\'t' \
            ' a lot.<b>But then there was!</b><a href="www.god.com">' \
            'Click here to see</a></p><p><a href="www.satan.com">' \
            'Do not click here, though.</a></p></p>'
            
        )

        to_leaf1 = TextNode(text='Testing text type', text_type='text')
        to_leaf1 = TextNode.text_node_to_html_node(to_leaf1)
        to_leaf2 = TextNode(text='Testing bold type', text_type='bold')
        to_leaf2 = TextNode.text_node_to_html_node(to_leaf2)
        to_leaf3 = TextNode(text='Testing italic type', text_type='italic')
        to_leaf3 = TextNode.text_node_to_html_node(to_leaf3)
        to_leaf4 = TextNode(text='Testing code type', text_type='code')
        to_leaf4 = TextNode.text_node_to_html_node(to_leaf4)
        to_leaf5 = TextNode(text='Testing link type', text_type='link', url='www.testing.com')
        to_leaf5 = TextNode.text_node_to_html_node(to_leaf5)
        to_leaf6 = TextNode(text='Testing image type', text_type='image', url='www.testing.com')
        to_leaf6 = TextNode.text_node_to_html_node(to_leaf6)
        self.assertEqual(to_leaf1.to_html(), 'Testing text type')
        self.assertEqual(to_leaf2.to_html(), '<b>Testing bold type</b>')
        self.assertEqual(to_leaf3.to_html(), '<i>Testing italic type</i>')
        self.assertEqual(to_leaf4.to_html(), '<code>Testing code type</code>')
        self.assertEqual(to_leaf5.to_html(), '<a href="www.testing.com">Testing link type</a>')
        self.assertEqual(to_leaf6.to_html(), '<img src="www.testing.com">Testing image type</img>')

if __name__ == '__main__':
    unittest.main()