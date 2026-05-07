import networkx as nx
import matplotlib.pyplot as plt


class Visualizer:
    def plot(self, obj, route):
        if not route: return

        G = nx.Graph()
        # Add edges for all distances defined in CSV
        for i, loc1 in enumerate(obj.locations):
            for loc2 in obj.locations[i + 1:]:
                d = obj.distances.at[loc1, loc2]
                if d > 0: G.add_edge(loc1, loc2, weight=d)

        # Generate (x, y) coordinates for nodes
        pos = nx.spring_layout(G, seed=42)

        plt.figure(figsize=(12, 8))
        plt.axis('on')  # Show X and Y axes
        plt.grid(True, linestyle='--', alpha=0.5)

        # Draw the cities
        nx.draw_networkx_nodes(G, pos, node_color='orange', node_size=2500)
        nx.draw_networkx_edges(G, pos, edge_color='black', alpha=0.1)

        # Labels with X/Y values
        labels = {n: f"{n}\n({pos[n][0]:.2f}, {pos[n][1]:.2f})" for n in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=9, font_weight='bold')

        # Highlight the Route in Red
        path_edges = [(route[i], route[i + 1]) for i in range(len(route) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=4)

        plt.title("Transport Route Map with Coordinates")
        plt.xlabel("X Position")
        plt.ylabel("Y Position")
        plt.show()