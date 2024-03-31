from textnode import TextNode
from htmlnode import HTMLNode

node = TextNode("This is a text node", "bold", "https://www.boot.dev")

print(node)

node2 = HTMLNode("p", "this is a text", None, None)
print(node2.props_to_html())