import unittest

from htmlnode import *


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

if __name__ == '__main__':
    unittest.main()