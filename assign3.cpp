#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Node
{
public:
    string name;
    vector<Node *> children;

    Node(string name)
    {
        this->name = name;
    }
};

void printNodes(Node *node, int depth)
{
    for (int i = 0; i < depth; i++)
    {
        cout << "  ";
    }
    cout << "- " << node->name << endl;
    for (Node *child : node->children)
    {
        printNodes(child, depth + 1);
    }
}

int main()
{
    // Create the tree structure
    Node *book = new Node("Book");
    Node *chapter1 = new Node("Chapter 1");
    Node *chapter2 = new Node("Chapter 2");
    book->children.push_back(chapter1);
    book->children.push_back(chapter2);
    Node *section1_1 = new Node("Section 1.1");
    Node *section1_2 = new Node("Section 1.2");
    chapter1->children.push_back(section1_1);
    chapter1->children.push_back(section1_2);
    Node *section2_1 = new Node("Section 2.1");
    chapter2->children.push_back(section2_1);
    Node *section2_2 = new Node("Section 2.2");
    chapter2->children.push_back(section2_2);
    Node *subSection1_1_1 = new Node("Sub-section 1.1.1");
    section1_1->children.push_back(subSection1_1_1);
    Node *subSection1_1_2 = new Node("Sub-section 1.1.2");
    section1_1->children.push_back(subSection1_1_2);
    Node *subSection2_2_1 = new Node("Sub-section 2.2.1");
    section2_2->children.push_back(subSection2_2_1);
    Node *subSection2_2_2 = new Node("Sub-section 2.2.2");
    section2_2->children.push_back(subSection2_2_2);

    // Print the nodes of the tree
    printNodes(book, 0);

    return 0;
}
