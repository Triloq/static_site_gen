
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag            # HTML tag name (e.g. 'p', 'a', 'h1')
        self.value = value        # value in the tag (e.g. text)
        self.children = children  # list of HTMLNode objects representing 
                                  # children of this node
        self.props = props        # dict of key-value pairs representing 
                                  # attributes of HTML tag

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        prop_str = ''
        if self.props is not None:
            for item in self.props:
                prop_str += f' {item}={self.props[item]}'
        return prop_str
    
    def __repr__(self):
        print(f'tag={self.tag} value={self.value} children={self.children} props={self.props}')


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError('No value.')
        if self.tag is None:
            return self.value
        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        for k, v in self.props.items():
            if self.tag == 'img':
                return f'<{self.tag} {k}="{v}">{self.props['alt']}</{self.tag}>'
            return f'<{self.tag} {k}="{v}">{self.value}</{self.tag}>'


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag.")
        if self.children is None:
            raise ValueError("No children.")
        html_line = f'<{self.tag}'
        if self.props is not None:
            for k, v in self.props.items():
                html_line += f' {k}="{v}"'
        html_line += '>'
        for child in self.children:
            html_line += child.to_html()
        html_line += f'</{self.tag}>'
        return html_line
        
