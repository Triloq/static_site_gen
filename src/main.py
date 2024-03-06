
from textnode import TextNode
from htmlnode import HTMLNode

def main():
    
    obj = {"href": "https://www.google.com", "target": "_blank"}
    
    test = HTMLNode()
    print(test.props_to_html())
    

main()