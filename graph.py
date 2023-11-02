from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for next_vertex in graph[start] - visited:
        dfs(graph, next_vertex, visited)
    return visited

def has_cycle(graph):
    visited = set()

    for vertex in graph:
        if vertex not in visited:
            if dfs_cycle(graph, vertex, visited, -1):
                return True
    return False

def dfs_cycle(graph, vertex, visited, parent):
    visited.add(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            if dfs_cycle(graph, neighbor, visited, vertex):
                return True
        elif parent != neighbor:
            return True
    return False

def shortest_path(graph, start, end):
    visited = {start: None}
    queue = deque([start])

    while queue:
        current_vertex = queue.popleft()
        if current_vertex == end:
            path = []
            while current_vertex:
                path.append(current_vertex)
                current_vertex = visited[current_vertex]
            return path[::-1]

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited[neighbor] = current_vertex
                queue.append(neighbor)
    return None

def topological_sort(graph):
    visited = set()
    stack = []

    for vertex in graph:
        if vertex not in visited:
            dfs_topo(graph, vertex, visited, stack)

    return stack[::-1]

def dfs_topo(graph, vertex, visited, stack):
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_topo(graph, neighbor, visited, stack)
    stack.append(vertex)


def has_cycle_directed(graph):
    white, gray, black = set(graph), set(), set()

    while white:
        vertex = next(iter(white))
        if dfs_cycle_directed(graph, vertex, white, gray, black):
            return True
    return False


def dfs_cycle_directed(graph, vertex, white, gray, black):
    white.discard(vertex)
    gray.add(vertex)

    for neighbor in graph.get(vertex, ()):
        if neighbor in black:
            continue
        if neighbor in gray:
            return True
        if dfs_cycle_directed(graph, neighbor, white, gray, black):
            return True

    gray.remove(vertex)
    black.add(vertex)
    return False

import heapq

def dijkstra(graph, start):
    shortest_path = {vertex: float('infinity') for vertex in graph}
    shortest_path[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > shortest_path[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_path

def connected_components(graph):
    visited = set()
    components = []

    for vertex in graph:
        if vertex not in visited:
            current_component = set()
            dfs(graph, vertex, visited, current_component)
            components.append(current_component)

    return components

def dfs(graph, vertex, visited, current_component):
    visited.add(vertex)
    current_component.add(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, current_component)

import heapq

def prim(graph, start):
    visited = set([start])
    edges = [
        (cost, start, to)
        for to, cost in graph[start].items()
    ]
    heapq.heapify(edges)

    spanning_tree = []
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            spanning_tree.append((frm, to, cost))

            for to_next, cost2 in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost2, to, to_next))

    return spanning_tree

def path_exists(graph, start, end):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex == end:
            return True
        visited.add(vertex)
        stack.extend(graph[vertex] - visited)

    return False
import unittest

class TestGraphFunctions(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'A': {'B', 'C'},
            'B': {'A', 'D', 'E'},
            'C': {'A', 'F'},
            'D': {'B'},
            'E': {'B', 'F'},
            'F': {'C', 'E'}
        }

        self.directed_graph_with_cycle = {
            'A': {'B'},
            'B': {'C'},
            'C': {'A'}
        }

        self.weighted_graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }

    def test_bfs(self):
        # Redirecting the standard output to capture the printed vertices
        from io import StringIO
        import sys
        backup = sys.stdout
        sys.stdout = StringIO()
        bfs(self.graph, 'A')
        output = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = backup

        self.assertEqual(output.strip(), "A B C D E F")

    def test_dfs(self):
        # Redirecting the standard output to capture the printed vertices
        from io import StringIO
        import sys
        backup = sys.stdout
        sys.stdout = StringIO()
        dfs(self.graph, 'A')
        output = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = backup

        # DFS can have different valid outputs based on traversal, so checking for one of the possible correct outputs
        self.assertIn(output.strip(), ["A B D E F C", "A C F E B D"])

    def test_has_cycle(self):
        self.assertFalse(has_cycle(self.graph))
        self.assertTrue(has_cycle(self.directed_graph_with_cycle))

    def test_shortest_path(self):
        self.assertEqual(shortest_path(self.graph, 'A', 'D'), ['A', 'B', 'D'])

    def test_topological_sort(self):
        # Not all graphs can be topologically sorted (needs to be a DAG)
        # Just as a dummy test for the provided graph
        self.assertRaises(Exception, topological_sort, self.graph)

    def test_has_cycle_directed(self):
        self.assertTrue(has_cycle_directed(self.directed_graph_with_cycle))

    def test_dijkstra(self):
        self.assertEqual(dijkstra(self.weighted_graph, 'A'), {'A': 0, 'B': 1, 'C': 3, 'D': 4})

    def test_connected_components(self):
        self.assertEqual(len(connected_components(self.graph)), 1)

    def test_prim(self):
        mst = prim(self.weighted_graph, 'A')
        total_weight = sum(weight for _, _, weight in mst)
        self.assertEqual(total_weight, 4)  # 1(A-B) + 2(B-C) + 1(C-D) = 4

    def test_path_exists(self):
        self.assertTrue(path_exists(self.graph, 'A', 'F'))
        self.assertFalse(path_exists(self.graph, 'A', 'Z'))  # Vertex 'Z' does not exist in the graph

if __name__ == "__main__":
    unittest.main()
