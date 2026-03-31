from textnode import TextNode, TextType

if __name__ == '__main__':
    node = TextNode('This is some text', TextType.BOLD, 'http://example.com')
    print(node)
