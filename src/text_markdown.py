import unittest
from markdown import *

class TestMarkdown(unittest.TestCase):
    def test_eq(self):
        text1 = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        text2 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"

        self.assertEqual(Extract_Markdown_Images(text1), [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")])
        self.assertEqual(Extract_Markdown_Links(text2), [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])
        print('hupp')