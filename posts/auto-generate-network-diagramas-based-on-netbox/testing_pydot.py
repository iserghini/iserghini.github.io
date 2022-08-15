import pydot

DC = "LON2"
graph = pydot.Dot(DC, graph_type="graph")
spines = 4
leafs = 8

for leaf in range(1, leafs + 1):
    graph.add_node(pydot.Node("CNL{}-M23-LON2-UK".format(leaf), shape="rectangle"))
    for spine in range(1, spines + 1):
        graph.add_node(pydot.Node("CNS{}-M23-LON2-UK".format(spine), shape="rectangle"))
        graph.add_edge(pydot.Edge("CNS{}-M23-LON2-UK".format(spine), "CNL{}-M23-LON2-UK".format(leaf), color="black"))


# Create file diagram
graph.set_size('"150,150!"')
print(graph)
graph.write_png("out.png")

#import pydot
#graph = pydot.Dot(graph_type='graph')
#graph.add_edge(pydot.Edge("1", "2"))
#graph.add_edge(pydot.Edge("1", "3"))
#
#graph.write_png("out.png")