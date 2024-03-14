import re

def Extract_Markdown_Images(text):

    alt_text = re.findall(r"!\[(.*?)\]", text)
    link_text = re.findall(r"\((.*?)\)", text)
    return list(zip(alt_text, link_text))

def Extract_Markdown_Links(text):
    
    anchor_text = re.findall(r"\[(.*?)\]", text)
    url_text = re.findall(r"\((.*?)\)", text)
    return list(zip(anchor_text, url_text))