class Graph:
    def __init__(self, num_vertices):
        # Inicializa a classe Graph com um número específico de vértices
        self.num_vertices = num_vertices

        # Cria uma matriz de adjacência (representação em matriz) e uma lista de adjacência (representação em lista)
        # Ambas são inicializadas com zeros/vazias
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        # Adiciona uma aresta entre os vértices u e v, indicando uma conexão direta
        # Verifica se u e v estão dentro dos limites do número de vértices
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            # Define a entrada correspondente na matriz de adjacência como 1 (indicando uma aresta)
            self.matrix[u][v] = 1
            self.matrix[v][u] = 1  # Se for um grafo não direcionado, define também a entrada inversa
            # Adiciona v à lista de adjacência de u e vice-versa (para grafos não direcionados)
            self.list[u].append(v)
            self.list[v].append(u)

    def print_graph(self):
        # Imprime a representação do grafo em Matriz de Adjacência e Lista de Adjacência
        print("Matriz de Adjacência:")
        for row in self.matrix:
            print(row)
        
        print("\nLista de Adjacência:")
        for vertex, neighbors in enumerate(self.list):
            print(f"Vértice {vertex}: {neighbors}")

    def dfs(self, start_vertex):
        # Executa a busca em profundidade (DFS) a partir de um vértice de início especificado
        visited = set()  # Conjunto para rastrear os vértices visitados
        stack = []  # Pilha para armazenar os vértices a serem explorados

        stack.append(start_vertex)  # Inicialmente, empilhamos o vértice de início

        while stack:
            vertex = stack.pop()  # Retira o vértice do topo da pilha

            if vertex not in visited:
                print(vertex, end=' ')  # Imprime o vértice visitado
                visited.add(vertex)  # Marca o vértice como visitado

            # Empilha todos os vértices adjacentes não visitados (em ordem reversa para manter a ordem correta)
            for neighbor in reversed(self.list[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
