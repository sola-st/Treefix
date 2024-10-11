# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_combinations_test.py
c1 = combinations.combine(mode=["graph", "eager"])
c2 = combinations.combine(optimizer=["adam", "gd"])
c3 = combinations.combine(distribution=["d1", "d2"])
c4 = combinations.times(c3, c1, c2)
self.assertEqual([
    OrderedDict([("distribution", "d1"), ("mode", "graph"),
                 ("optimizer", "adam")]),
    OrderedDict([("distribution", "d1"), ("mode", "graph"),
                 ("optimizer", "gd")]),
    OrderedDict([("distribution", "d1"), ("mode", "eager"),
                 ("optimizer", "adam")]),
    OrderedDict([("distribution", "d1"), ("mode", "eager"),
                 ("optimizer", "gd")]),
    OrderedDict([("distribution", "d2"), ("mode", "graph"),
                 ("optimizer", "adam")]),
    OrderedDict([("distribution", "d2"), ("mode", "graph"),
                 ("optimizer", "gd")]),
    OrderedDict([("distribution", "d2"), ("mode", "eager"),
                 ("optimizer", "adam")]),
    OrderedDict([("distribution", "d2"), ("mode", "eager"),
                 ("optimizer", "gd")])
], c4)
self.assertEqual(
    combinations.combine(
        mode=["graph", "eager"],
        optimizer=["adam", "gd"],
        distribution=["d1", "d2"]), c4)
