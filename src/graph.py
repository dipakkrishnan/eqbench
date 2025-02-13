import networkx as nx
import matplotlib.pyplot as plt


class CoTGraph:

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id: int, reasoning: str, embedding: list[float]):
        self.graph.add_node(node_id, reasoning=reasoning, embedding=embedding)

    def add_edge(self, from_node: int, to_node: int, weight: float):
        self.graph.add_edge(from_node, to_node, weight=weight)

    def visualize(self):
        pos = nx.spring_layout(self.graph)
        node_labels = {node: self.graph.nodes[node]['reasoning'] for node in self.graph.nodes}
        edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in self.graph.edges(data=True)}
        
        fig, ax = plt.subplots()
        nx.draw(self.graph, pos, with_labels=True, node_color="lightblue", edge_color="gray", ax=ax)
        nx.draw_networkx_labels(self.graph, pos, node_labels, font_size=10, ax=ax)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_size=9, ax=ax)
        plt.show()

    def __repr__(self):
        return f"CoT Graph with {len(self.graph.nodes)} nodes and {len(self.graph.edges)} edges."

