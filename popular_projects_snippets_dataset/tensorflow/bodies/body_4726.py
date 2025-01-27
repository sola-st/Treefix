# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils_test.py
Point = collections.namedtuple("Point", ["x", "y"])
point1 = Point(x=0, y=2)
point2 = Point(x=1, y=3)
wrapped1 = wrapt.ObjectProxy(point1)
wrapped2 = wrapt.ObjectProxy(point2)
result = distribute_utils.regroup([wrapped1, wrapped2])
self.assertEqual(result.x.values, (0, 1))
self.assertEqual(result.y.values, (2, 3))
