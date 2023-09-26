import queue

class Graph:
  def __init__(self, num_vert):
    # Armazena o número de vértices do grafo.
    self.num_vertices = num_vert
    # Inicializa uma matriz de adjacência com zeros.
    self.matrix = [[0 for _ in range(num_vert)] for _ in range(num_vert)]
    # Inicializa uma lista de adjacência vazia para cada vértice.
    self.list = [[] for _ in range(num_vert)]


  def print(self):
    print(f"\n{self.matrix}\n") # Printa a matriz de adjacência.
    print(f"\n{self.list}\n") # Printa a lista de adjacência.


  def bfs(self, source):
    # Inicializa uma fila para a busca em largura.
    fila = queue.Queue()
    # Coloca o vértice de origem na fila.
    fila.put(source)

    # Inicializa uma lista de distâncias com -1.
    dist = [-1 for _ in range(self.num_vertices)]
    # Inicializa uma lista de vértices anteriores com -1.
    ant = [-1 for _ in range(self.num_vertices)]
    # Inicializa uma lista de visitados como False.
    isVisited = [False for _ in range(self.num_vertices)]
    # Marca o vértice de origem como visitado.
    isVisited[source] = True
    # Define a distância do vértice de origem para ele mesmo como 0.
    dist[source] = 0

    while fila.empty() != True:
      # Remove um vértice da fila e o armazena em 'p'.
      p = fila.get()
      #print(f"\nVertice: {p}\n") # Printa o vértice atual.

      # Itera sobre os vértices adjacentes ao vértice 'p'.
      for v in self.list[p]:
        # Verifica se o vértice 'v' não foi visitado.
        if (isVisited[v] == False):
          # Atualiza a distância até 'v'.
          dist[v] = dist[p] + 1
          # Define o vértice 'p' como o vértice anterior de 'v'.
          ant[v] = p
          # Coloca 'v' na fila para visita futura.
          fila.put(v)
          # Marca 'v' como visitado.
          isVisited[v] = True

    return dist, ant # Retorna as listas de distâncias e vértices anteriores.


    #s: O vértice de origem do caminho. t: O vértice de destino do caminho.
  def print_path(self, s, t, ant):
      #verifica se não há um caminho do vértice 's' até o vértice 't' 
    if ant[t] == -1:
      print("Não há caminho entre os vértices.")
      return
      #inicializa uma lista vazia que será usada para armazenar os vértices no caminho entre s e t.
    path = []
      #loop que percorre os vértices no caminho do vértice t de volta até o vértice de origem s. 
    while t != s:
        #A cada iteração, o vértice t é adicionado à lista path
      path.append(t)
        #o próximo vértice no caminho é obtido usando ant[t].
      t = ant[t]

      #Após o loop, o vértice de origem s é adicionado à lista path.
    path.append(s)
      #A lista path é invertida, para que os vértices sejam listados na ordem correta
    path.reverse()

      # imprimir o caminho entre dois vértices s e t no grafo
    print("\nCaminho entre os vértices:")
    print(" -> ".join(map(str, path)))