
from textnode import TextNode
from htmlnode import *

def main():
    
    obj = {"href": "https://www.google.com", "target": "_blank"}
    
    # for k, v in obj.items():
    #     print(f'{k}={v}')

    # node = ParentNode(
    #     "p",
    #     [
    #         LeafNode("b", "Bold text"),
    #         LeafNode(None, "Normal text"),
    #         LeafNode("i", "italic text"),
    #         LeafNode(None, "Normal text"),
    #         ParentNode("p",
    #         [
    #             LeafNode("a", "link", {"href": "www.google.com"}),
    #             LeafNode(None, "Second text"),
    #             LeafNode("i", "Second Italics text"),
    #             LeafNode(None, "Second text"),
    #         ],
    #     )
    #     ],
    #     {"href": "www.bagels.com"}
    # )
    # print(node.to_html())




main()