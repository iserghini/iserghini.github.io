import pynetbox

NETBOX_URL = 'http://localhost:8000'
TOKEN = '0123456789abcdef0123456789abcdef01234567'

nb = pynetbox.api(url=NETBOX_URL, token=TOKEN)

# Create spines
for i in range(1, 5):
    try:
        create_device = nb.dcim.devices.create(
            name=f"spine{i}",
            device_type=683,  # Mellanox SN2700
            device_role=1,  # Spine
            tenant=1,  # Infrastructure
            site=1,  # US East
            rack=1,  # Rack 100
            position=42-i,
            face="front",
        )
        print(create_device)
    except pynetbox.core.query.RequestError:
        print(f"spine{i} already exits in Netbox - skipping it")

# create leaves
for i in range(1, 9):
    try:
        create_device = nb.dcim.devices.create(
            name=f"leaf{i}",
            device_type=683,  # Mellanox SN2700
            device_role=2,  # Leaf
            tenant=1,  # Infrastructure
            site=1,  # US East
            rack=1,  # Rack 100
            position=32-i,
            face="front",
        )
        print(create_device)
    except pynetbox.core.query.RequestError:
        print(f"leaf{i} already exits in Netbox - skipping it")

# link spines and leaves
leaves = list(nb.dcim.devices.filter(role='leaf', site='us-east'))  # or [device for device in nb.dcim.devices.filter(device_role='leaf')]
spines = list(nb.dcim.devices.filter(role='spine', site='us-east'))

for leaf_num, leaf in enumerate(leaves):
    int_leaf = 28
    print('#' * 32)
    for int_spine, spine in enumerate(spines):
        interface_a = nb.dcim.interfaces.get(device=leaf, name=f'swp{int_leaf + 1}')
        interface_b = nb.dcim.interfaces.get(device=spine, name=f'swp{leaf_num + 1}')
        create_link = nb.dcim.cables.create(
            termination_a_type='dcim.interface',  # string
            termination_a_id=interface_a.id,  # leaf1 swp29/swp30/swp31/swp32
            termination_b_type='dcim.interface',
            termination_b_id=interface_b.id,  # spine1 swp1 / spine2 swp1 / spine3 swp1 / spine4 swp1
        )
        print(leaf, interface_a, '------->', spine, interface_b)
        print(create_link)
        int_leaf += 1
