import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_node("1",level=3)
G.add_node("2",level=2)
G.add_node("3",level=3)
G.add_node("4",level=2)
G.add_node("5",level=2)


G.add_edge("1","2",weight="2")
G.add_edge("2","3",weight=3)
G.add_edge("4","3",weight=6)
G.add_edge("1","5",weight=4)
G.add_edge("5","4",weight=5)
G.add_edge("1","3",weight=1)


print (nx.info(G))
nx.draw(G,with_labels=True)

plt.show()