class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

def printNodes(node, depth):
    print("  " * depth + "- " + node.name)
    for child in node.children:
        printNodes(child, depth+1)

book = Node("Book")
chapter1 = Node("Chapter 1")
chapter2 = Node("Chapter 2")
book.children.append(chapter1)
book.children.append(chapter2)
section1_1 = Node("Section 1.1")
section1_2 = Node("Section 1.2")
chapter1.children.append(section1_1)
chapter1.children.append(section1_2)
section2_1 = Node("Section 2.1")
section2_2 = Node("Section 2.2")
chapter2.children.append(section2_1)
chapter2.children.append(section2_2)
subSection1_1_1 = Node("Sub-section 1.1.1")
subSection1_1_2 = Node("Sub-section 1.1.2")
subSection2_2_1 = Node("Sub-section 2.2.1")
subSection2_2_2 = Node("Sub-section 2.2.2")
section1_1.children.append(subSection1_1_2)
section1_1.children.append(subSection1_1_1)
section2_2.children.append(subSection2_2_1)
section2_2.children.append(subSection2_2_2)

printNodes(book, 0)
