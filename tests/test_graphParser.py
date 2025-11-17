from src.graphParser import parseGraph
import networkx as nx
import unittest

class TestgraphParser(unittest.TestCase):
    def testParseGraph(self):
        graph, demands = parseGraph("data/example2.json")
        edges_repr = []
        for line in nx.generate_edgelist(graph, data=True):
            edges_repr.append(str(line))
        assert edges_repr[0] == "A C {'color': 'red', 'capacity': 100, 'price': 5, 'k': 1}"
        assert edges_repr[1] == "A C {'color': 'Bus', 'capacity': 200, 'price': 5, 'k': 2}"
        assert str(demands[0]) == "{'s': 'A', 't': 'E', 'd': 400}"
        
if __name__ == "__main__":
    unittest.main()


