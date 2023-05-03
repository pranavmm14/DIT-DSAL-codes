/*Assignment -6

Title:
Represent a given graph using adjacency matrix/list to perform 
DFS and using adjacency list to perform BFS. Use the map of the 
area around the college as the graph. Identify the prominent land 
marks as nodes and perform DFS and BFS on that.*/

#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

// function to perform DFS
void DFS(int vertex, vector<vector<int>> graph, vector<bool>& visited) {
    visited[vertex] = true;
    cout << vertex << " ";

    for (int i = 0; i < graph[vertex].size(); i++) {
        if (!visited[graph[vertex][i]]) {
            DFS(graph[vertex][i], graph, visited);
        }
    }
}

// function to perform BFS
void BFS(int vertex, vector<vector<int>> graph, vector<bool>& visited) {
    queue<int> q;
    q.push(vertex);
    visited[vertex] = true;

    while (!q.empty()) {
        int currVertex = q.front();
        q.pop();
        cout << currVertex << " ";

        for (int i = 0; i < graph[currVertex].size(); i++) {
            int adjacentVertex = graph[currVertex][i];
            if (!visited[adjacentVertex]) {
                visited[adjacentVertex] = true;
                q.push(adjacentVertex);
            }
        }
    }
}

int main() {
    // create a map of the area around the college
    map<string, int> landmarks;
    landmarks["A"] = 0;
    landmarks["B"] = 1;
    landmarks["C"] = 5;
    landmarks["D"] = 3;
    landmarks["E"] = 4;

    // create the adjacency matrix
    vector<vector<int>> adjacencyMatrix = {
        {0, 1, 1, 0, 0},
        {1, 0, 0, 1, 0},
        {1, 0, 1, 1, 1},
        {0, 1, 1, 0, 0},
        {1, 0, 1, 0, 0}
    };

    // create the adjacency list
    vector<vector<int>> adjacencyList(adjacencyMatrix.size());
    for (int i = 0; i < adjacencyMatrix.size(); i++) {
        for (int j = 0; j < adjacencyMatrix[i].size(); j++) {
            if (adjacencyMatrix[i][j] == 1) {
                adjacencyList[i].push_back(j);
            }
        }
    }

    // perform DFS using adjacency matrix
    vector<bool> visited(adjacencyMatrix.size(), false);
    cout << "DFS using adjacency matrix: ";
    DFS(0, adjacencyMatrix, visited);
    cout << endl;

    // perform BFS using adjacency list
    visited = vector<bool>(adjacencyList.size(), false);
    cout << "BFS using adjacency list: ";
    BFS(0, adjacencyList, visited);
    cout << endl;

    return 0;
}
