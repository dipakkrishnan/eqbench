import networkx as nx
import matplotlib.pyplot as plt


class CoTGraph:

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id: int, reasoning: str, embedding: list[float]):
        self.graph.add_node(node_id, reasoning=reasoning, embedding=embedding)

    def add_edge(self, from_node: int, to_node: int, weight: float):
        self.graph.add_edge(from_node, to_node, weight=weight)

    def visualize(self, figsize=(12,8), node_size=2000, font_size=8, edge_width=2):
        plt.figure(figsize=figsize)
        
        # Use hierarchical layout for directional flow
        pos = nx.kamada_kawai_layout(self.graph)
        
        # Draw nodes
        nx.draw_networkx_nodes(self.graph, pos,
                             node_color='lightblue',
                             node_size=node_size,
                             alpha=0.7,
                             edgecolors='darkblue')
        
        # Draw edges with arrows
        nx.draw_networkx_edges(self.graph, pos,
                             edge_color='gray',
                             width=edge_width,
                             arrowsize=20,
                             alpha=0.6)
        
        # Add node labels (reasoning text)
        node_labels = {node: self.graph.nodes[node]['reasoning'] for node in self.graph.nodes}
        nx.draw_networkx_labels(self.graph, pos,
                              labels=node_labels,
                              font_size=font_size,
                              font_weight='bold',
                              font_family='sans-serif',
                              bbox=dict(facecolor='white', 
                                      edgecolor='none',
                                      alpha=0.7,
                                      pad=4.0))
        
        # Add edge weights as labels
        edge_labels = {(u,v): f"{d['weight']:.2f}" for u,v,d in self.graph.edges(data=True)}
        nx.draw_networkx_edge_labels(self.graph, pos,
                                   edge_labels=edge_labels,
                                   font_size=font_size)
        
        plt.title("Chain of Thought Graph", pad=20, size=14)
        plt.axis('off')
        plt.tight_layout()
        plt.show()

    def __repr__(self):
        return f"CoT Graph with {len(self.graph.nodes)} nodes and {len(self.graph.edges)} edges."

