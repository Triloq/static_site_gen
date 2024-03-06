import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        html1 = HTMLNode()
        html2 = HTMLNode()
        self.assertEqual(html1.props_to_html(), html2.props_to_html())
        html3 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        html4 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(html3.props_to_html(), html4.props_to_html())
        self.assertNotEqual(html4.props_to_html(), html1.props_to_html())

if __name__ == '__main__':
    unittest.main()