# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_combinations_test.py
c1 = combinations.combine(mode=["graph"], loss=["callable", "tensor"])
c2 = combinations.combine(mode=["eager"], loss=["callable"])
c3 = combinations.combine(distribution=["d1", "d2"])
c4 = combinations.times(c3, c1 + c2)
self.assertEqual([
    OrderedDict([("distribution", "d1"), ("loss", "callable"),
                 ("mode", "graph")]),
    OrderedDict([("distribution", "d1"), ("loss", "tensor"),
                 ("mode", "graph")]),
    OrderedDict([("distribution", "d1"), ("loss", "callable"),
                 ("mode", "eager")]),
    OrderedDict([("distribution", "d2"), ("loss", "callable"),
                 ("mode", "graph")]),
    OrderedDict([("distribution", "d2"), ("loss", "tensor"),
                 ("mode", "graph")]),
    OrderedDict([("distribution", "d2"), ("loss", "callable"),
                 ("mode", "eager")])
], c4)
