from graph import Graph


def load_graph(fileName):
  file = open(fileName, 'r')
  num_vert = int(file.readline())

  graph = Graph(num_vert)

  linha = 0
  for line in file:
    line.strip()
    numeros = line.split("\t")
    coluna = 0
    for i in numeros:
      if (coluna == graph.num_vertices):
        break

      graph.matrix[linha][coluna] = int(i)
      if (graph.matrix[linha][coluna] > 0):
        graph.list[linha].append(coluna)

      coluna += 1

    linha += 1

  return graph

gr = load_graph("pcv10.txt")
gr.print()
dist, ant = gr.bfs(2)
print(f"\n{dist}\n")
print(f"\n{ant}\n")
gr.print_path(2, 8, ant)
