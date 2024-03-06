

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def eq(self, text_node):
        return self.text == text_node.text
    
    def repr(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'