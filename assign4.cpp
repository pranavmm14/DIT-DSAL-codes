/*  Assignment No. 4
Beginning with an empty binary search tree, Construct binary searchtree by inserting the values
in the order given. After constructing a binary tree –
i. Insert new node
ii. Find number of nodes in longest path
iii. Minimum data value found in the tree
iv. Change a tree so that the roles of the left and right pointers are swapped atevery node
v. Search a value*/

#include <iostream>
using namespace std;

// Definition of a binary search tree node
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// Function to insert a new node in a binary search tree
TreeNode *insert(TreeNode *root, int val)
{
    if (root == NULL)
    {
        return new TreeNode(val);
    }
    if (val < root->val)
    {
        root->left = insert(root->left, val);
    }
    else
    {
        root->right = insert(root->right, val);
    }
    return root;
}

// Function to find the number of nodes in the longest path in a binary search tree
int longestPath(TreeNode *root)
{
    if (root == NULL)
    {
        return 0;
    }
    return 1 + max(longestPath(root->left), longestPath(root->right));
}

// Function to find the minimum data value in a binary search tree
int minimum(TreeNode *root)
{
    while (root->left != NULL)
    {
        root = root->left;
    }
    return root->val;
}

// Function to swap the left and right pointers at every node in a binary search tree
void swapLeftRight(TreeNode *root)
{
    if (root == NULL)
    {
        return;
    }
    swap(root->left, root->right);
    swapLeftRight(root->left);
    swapLeftRight(root->right);
}

// Function to search for a value in a binary search tree
bool search(TreeNode *root, int val)
{
    if (root == NULL)
    {
        return false;
    }
    if (root->val == val)
    {
        return true;
    }
    if (val < root->val)
    {
        return search(root->left, val);
    }
    else
    {
        return search(root->right, val);
    }
}

// Function to print the inorder traversal of a binary search tree
void inorder(TreeNode *root)
{
    if (root == NULL)
    {
        return;
    }
    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);
}

int main()
{
    TreeNode *root = NULL;
    int arr[] = {5, 3, 7, 1, 9, 4, 6, 2, 8};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Construct binary search tree by inserting the values in the given order
    for (int i = 0; i < n; i++)
    {
        root = insert(root, arr[i]);
    }

    // Insert new node with value 10
    root = insert(root, 10);

    // Find number of nodes in longest path
    cout << "Number of nodes in longest path: " << longestPath(root) << endl;

    // Find minimum data value in the tree
    cout << "Minimum data value: " << minimum(root) << endl;

    // Swap the left and right pointers at every node
    swapLeftRight(root);

    // Search for a value
    int val = 7;
    if (search(root, val))
    {
        cout << val << " found in tree." << endl;
    }
    else
    {
        cout << val << " not found in tree." << endl;
    }

    // Print the inorder traversal of the binary search tree
    inorder(root);

    cout << "Code by Pranav Mehendale" << endl;

    return 0;
}
