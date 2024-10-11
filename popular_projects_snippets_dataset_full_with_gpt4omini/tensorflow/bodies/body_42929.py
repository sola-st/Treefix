# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
scalar_traverse_input = [3, 4, (1, 2, [0]), [5, 6], {"a": (7,)}, []]
scalar_traverse_r = nest.get_traverse_shallow_structure(
    lambda s: not isinstance(s, tuple),
    scalar_traverse_input)
self.assertEqual(scalar_traverse_r,
                 [True, True, False, [True, True], {"a": False}, []])
nest.assert_shallow_structure(scalar_traverse_r,
                              scalar_traverse_input)

structure_traverse_input = [(1, [2]), ([1], 2)]
structure_traverse_r = nest.get_traverse_shallow_structure(
    lambda s: (True, False) if isinstance(s, tuple) else True,
    structure_traverse_input)
self.assertEqual(structure_traverse_r,
                 [(True, False), ([True], False)])
nest.assert_shallow_structure(structure_traverse_r,
                              structure_traverse_input)

with self.assertRaisesRegex(TypeError, "returned structure"):
    nest.get_traverse_shallow_structure(lambda _: [True], 0)

with self.assertRaisesRegex(TypeError, "returned a non-bool scalar"):
    nest.get_traverse_shallow_structure(lambda _: 1, [1])

with self.assertRaisesRegex(TypeError,
                            "didn't return a depth=1 structure of bools"):
    nest.get_traverse_shallow_structure(lambda _: [1], [1])
