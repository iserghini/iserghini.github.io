from pyvis.network import Network

net = Network()
# Add Spines
net.add_node(1, label="CNS1")
net.add_node(2, label="CNS2")

# Add leaves
net.add_node(3, label="CNL1")
net.add_node(4, label="CNL2")
net.add_node(5, label="CNL3")
net.add_node(6, label="CNL4")


# Add links
net.add_edges([(1, 3),
              (1, 4),
              (1, 5),
              (1, 6),
              (2, 3),
              (2, 4),
              (2, 5),
              (2, 6)])

net.repulsion(node_distance=100, spring_length=200)
net.show('nodes.html')