from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text=None, text_type=None, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes_list = []
        for node in old_nodes:
            if type(node) != type(TextNode()):
                new_nodes_list.append(node)
                continue
            split_text = node.text.split(delimiter, node.text.count(delimiter))
            if len(split_text) != 1 and len(split_text) % 2 == 0:
                raise Exception('Invalid Markdown Syntax')
            for i in range(0,len(split_text)):
                if i % 2 == 0:
                    if split_text[i] != '':
                        tmp = TextNode(split_text[i], text_type_text)
                else:
                    tmp = TextNode(split_text[i], text_type, node.url)
                new_nodes_list.append(tmp)
                print(new_nodes_list)
        for node in new_nodes_list:
            if type(node) == type(TextNode()):
                print(node)

    def __eq__(self, text_node):
        return (self.text == text_node.text) \
            and (self.text_type == text_node.text_type) \
            and (self.url == text_node.url) 
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
    def text_node_to_html_node(text_node):
        if text_node.text_type == text_type_text:
            return LeafNode(None, text_node.text)
        if text_node.text_type == text_type_bold:
            return LeafNode("b", text_node.text)
        if text_node.text_type == text_type_italic:
            return LeafNode("i", text_node.text)
        if text_node.text_type == text_type_code:
            return LeafNode("code", text_node.text)
        if text_node.text_type == text_type_link:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        if text_node.text_type == text_type_image:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        raise ValueError(f"Invalid text type: {text_node.text_type}")