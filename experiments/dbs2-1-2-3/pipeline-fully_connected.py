import chain as simulator
import time

n0 = simulator.Node(0)
n0.start()

simulator.queues[0].put((0, 0, -1)) # Peer, chunk, splitter
simulator.queues[0].put((1, 0, -1)) # Peer, chunk, splitter

n1 = simulator.Node(1)
n0.add_neighbor(1)
n1.add_neighbor(0)
n1.start()

simulator.queues[0].put((2, 1, -1)) # Peer, chunk, splitter
simulator.queues[0].put((3, 1, -1)) # Peer, chunk, splitter

n2 = simulator.Node(2)
n0.add_neighbor(2)
n1.add_neighbor(2)
n2.add_neighbor(0)
n2.add_neighbor(1)
print('Node 0: neighbors = ', n0.get_neighbors())
print('Node 1: neighbors = ', n1.get_neighbors())
print('Node 2: neighbors = ', n2.get_neighbors())
n2.start()

simulator.queues[0].put((4, 2, -1)) # Peer, chunk, splitter
simulator.queues[0].put((5, 2, -1)) # Peer, chunk, splitter

