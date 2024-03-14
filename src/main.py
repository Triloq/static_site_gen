
from textnode import TextNode
from htmlnode import *

def main():
    
    obj = {"href": "https://www.google.com", "target": "_blank"}
    
    
    thing = TextNode(text='Well `shoot`, dangit', text_type='link')
    thing2 = TextNode(text='`Shoot` ````*well*, thanks', text_type='link')
    thing3 = LeafNode()
    hold = TextNode.split_nodes_delimiter([thing, thing2, thing3], '`', "code")
    

main()