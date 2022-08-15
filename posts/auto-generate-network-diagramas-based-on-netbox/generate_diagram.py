import graphviz
import pynetbox

NETBOX_URL = 'http://localhost:8000'
TOKEN = '0123456789abcdef0123456789abcdef01234567'
nb = pynetbox.api(url=NETBOX_URL, token=TOKEN)

def find_connections(nb, device, site):
    """
    Given a device, it finds all its connections and returns a dictionary
    with the mapping {'queried_device_interface': (connected_device_name, connected_device_interface)
    """
    interfaces = list(nb.dcim.interfaces.filter(device=device, site=site))
    result = {}
    for interface in interfaces:
        connected_device_interface = interface.connected_endpoint
        if connected_device_interface is not None:
            connected_device_name = interface.connected_endpoint.device
            result[f'{interface}'] = (connected_device_name, connected_device_interface)
    return result


if __name__ == '__main__':
    diagram_name = 'US East Data Centre Diagram'
    leaves = list(nb.dcim.devices.filter(role='leaf', site='us-east'))
    spines = list(nb.dcim.devices.filter(role='spine', site='us-east'))

    # Create a graph object - the output format is also selected here
    dot = graphviz.Graph(engine='dot', format='pdf', node_attr={
        'shape': 'rectangle',
    })

    # Create all nodes (spine and leaf devices)
    for spine in spines:
        dot.node(f'{spine}', ordering="out")
    for leaf in leaves:
        dot.node(f'{leaf}', ordering="in")

    # Create all edges (make the connections between spines and leaves)
    for spine in spines:
        spine_connections = find_connections(nb, spine, 'us-east')
        for connection in spine_connections:
            leaf_name = spine_connections[connection][0]
            leaf_interface = spine_connections[connection][1]
            # dot.edge(f'{spine}', f'{leaf_name}', label=f'{leaf_interface}')
            dot.edge(f'{spine}', f'{leaf_name}')

    # Print the graph description in DOT language
    print(dot.source)
    dot.render(f'diagrams/{diagram_name}', view=True)  # save the files in the local dir, inside the "diagrams" dir
