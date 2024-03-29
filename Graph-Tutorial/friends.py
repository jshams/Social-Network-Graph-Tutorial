from graph import Graph

if __name__ == '__main__':
    friends_graph = Graph('friends.txt')
    print('GRAPH OF MY FRIENDS')
    print(f'Number of edges : {friends_graph.edge_count}')
    print(f'Number of vertices : {friends_graph.vertex_count}')
    print(f'Verticies : {", ".join(friends_graph.get_vertices())}')
    bailey_to_dan = friends_graph.find_shortest_path('Bailey', 'Daniel')
    print(
        f'Shortest path from Bailey to Daniel : {" -> ".join(bailey_to_dan)}')
    print(f'Number of edges from Bailey to Daniel : {len(bailey_to_dan) - 1}')
    print(f'Random clique : {", ".join(list(friends_graph.clique()))}')
    print(f'Diameter of friends : {friends_graph.diameter()}')
