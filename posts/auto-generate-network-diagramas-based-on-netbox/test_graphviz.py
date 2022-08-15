import graphviz

site = 'us-east'
spines = 4
leafs = 8
servers = 1

dot = graphviz.Graph(engine='dot', format='pdf', node_attr={
    'shape': 'rectangle',
    'bgcolor': 'red',
    })

# [constraint=false] for inter-leaf links

for leaf in range(1, leafs + 1):
    dot.node(f"leaf{leaf}", ordering="in")
    for server in range(1, servers + 1):
        dot.node(f"server{leaf}{server}", ordering="out")
        dot.edge(f"leaf{leaf}", f"server{leaf}{server}")

    for spine in range(1, spines + 1):
        dot.node(f"spine{spine}", ordering="in")
        dot.edge(f"spine{spine}", f"leaf{leaf}")

print(dot.source)

dot.render('diagrams/Diagram-{}'.format(site), view=True)


