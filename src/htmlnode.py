
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