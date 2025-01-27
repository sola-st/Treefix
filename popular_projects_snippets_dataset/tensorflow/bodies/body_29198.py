# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest_test.py
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

with self.assertRaisesRegex(TypeError, "callable"):
    nest.map_structure("bad", structure1_plus1)

with self.assertRaisesRegex(ValueError, "same nested structure"):
    nest.map_structure(lambda x, y: None, 3, (3,))

with self.assertRaisesRegex(TypeError, "same sequence type"):
    nest.map_structure(lambda x, y: None, ((3, 4), 5), {"a": (3, 4), "b": 5})

with self.assertRaisesRegex(ValueError, "same nested structure"):
    nest.map_structure(lambda x, y: None, ((3, 4), 5), (3, (4, 5)))

with self.assertRaisesRegex(ValueError, "same nested structure"):
    nest.map_structure(lambda x, y: None, ((3, 4), 5), (3, (4, 5)),
                       check_types=False)

with self.assertRaisesRegex(ValueError, "Only valid keyword argument"):
    nest.map_structure(lambda x: None, structure1, foo="a")

with self.assertRaisesRegex(ValueError, "Only valid keyword argument"):
    nest.map_structure(lambda x: None, structure1, check_types=False, foo="a")
