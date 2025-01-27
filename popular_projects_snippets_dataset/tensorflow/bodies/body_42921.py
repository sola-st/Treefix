# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
structure1 = (((1, 2), 3), 4, (5, 6))
structure2 = (((7, 8), 9), 10, (11, 12))
structure1_plus1 = nest.map_structure(lambda x: x + 1, structure1)
nest.assert_same_structure(structure1, structure1_plus1)
self.assertAllEqual(
    [2, 3, 4, 5, 6, 7],
    nest.flatten(structure1_plus1))
structure1_plus_structure2 = nest.map_structure(
    lambda x, y: x + y, structure1, structure2)
self.assertEqual(
    (((1 + 7, 2 + 8), 3 + 9), 4 + 10, (5 + 11, 6 + 12)),
    structure1_plus_structure2)

self.assertEqual(3, nest.map_structure(lambda x: x - 1, 4))

self.assertEqual(7, nest.map_structure(lambda x, y: x + y, 3, 4))

structure3 = collections.defaultdict(list)
structure3["a"] = [1, 2, 3, 4]
structure3["b"] = [2, 3, 4, 5]

expected_structure3 = collections.defaultdict(list)
expected_structure3["a"] = [2, 3, 4, 5]
expected_structure3["b"] = [3, 4, 5, 6]
self.assertEqual(expected_structure3,
                 nest.map_structure(lambda x: x + 1, structure3))

# Empty structures
self.assertEqual((), nest.map_structure(lambda x: x + 1, ()))
self.assertEqual([], nest.map_structure(lambda x: x + 1, []))
self.assertEqual({}, nest.map_structure(lambda x: x + 1, {}))
self.assertEqual(NestTest.EmptyNT(), nest.map_structure(lambda x: x + 1,
                                                        NestTest.EmptyNT()))

# This is checking actual equality of types, empty list != empty tuple
self.assertNotEqual((), nest.map_structure(lambda x: x + 1, []))

with self.assertRaisesRegex(TypeError, "callable"):
    nest.map_structure("bad", structure1_plus1)

with self.assertRaisesRegex(ValueError, "at least one structure"):
    nest.map_structure(lambda x: x)

with self.assertRaisesRegex(ValueError, "same number of elements"):
    nest.map_structure(lambda x, y: None, (3, 4), (3, 4, 5))

with self.assertRaisesRegex(ValueError, "same nested structure"):
    nest.map_structure(lambda x, y: None, 3, (3,))

with self.assertRaisesRegex(TypeError, "same sequence type"):
    nest.map_structure(lambda x, y: None, ((3, 4), 5), [(3, 4), 5])

with self.assertRaisesRegex(ValueError, "same nested structure"):
    nest.map_structure(lambda x, y: None, ((3, 4), 5), (3, (4, 5)))

structure1_list = [[[1, 2], 3], 4, [5, 6]]
with self.assertRaisesRegex(TypeError, "same sequence type"):
    nest.map_structure(lambda x, y: None, structure1, structure1_list)

nest.map_structure(lambda x, y: None, structure1, structure1_list,
                   check_types=False)

with self.assertRaisesRegex(ValueError, "same nested structure"):
    nest.map_structure(lambda x, y: None, ((3, 4), 5), (3, (4, 5)),
                       check_types=False)

with self.assertRaisesRegex(ValueError, "Only valid keyword argument.*foo"):
    nest.map_structure(lambda x: None, structure1, foo="a")

with self.assertRaisesRegex(ValueError, "Only valid keyword argument.*foo"):
    nest.map_structure(lambda x: None, structure1, check_types=False, foo="a")
