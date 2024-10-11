# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
structure = ((3, 4), 5, (6, 7, (9, 10), 8))
flat = ["a", "b", "c", "d", "e", "f", "g", "h"]
self.assertEqual(nest.flatten(structure), [3, 4, 5, 6, 7, 9, 10, 8])
self.assertEqual(
    nest.pack_sequence_as(structure, flat), (("a", "b"), "c",
                                             ("d", "e", ("f", "g"), "h")))
structure = (NestTest.PointXY(x=4, y=2),
             ((NestTest.PointXY(x=1, y=0),),))
flat = [4, 2, 1, 0]
self.assertEqual(nest.flatten(structure), flat)
restructured_from_flat = nest.pack_sequence_as(structure, flat)
self.assertEqual(restructured_from_flat, structure)
self.assertEqual(restructured_from_flat[0].x, 4)
self.assertEqual(restructured_from_flat[0].y, 2)
self.assertEqual(restructured_from_flat[1][0][0].x, 1)
self.assertEqual(restructured_from_flat[1][0][0].y, 0)

self.assertEqual([5], nest.flatten(5))
self.assertEqual([np.array([5])], nest.flatten(np.array([5])))

self.assertEqual("a", nest.pack_sequence_as(5, ["a"]))
self.assertEqual(
    np.array([5]), nest.pack_sequence_as("scalar", [np.array([5])]))

with self.assertRaisesRegex(ValueError, self.unsafe_map_pattern):
    nest.pack_sequence_as("scalar", [4, 5])

with self.assertRaisesRegex(TypeError, self.bad_pack_pattern):
    nest.pack_sequence_as([4, 5], "bad_sequence")

with self.assertRaises(ValueError):
    nest.pack_sequence_as([5, 6, [7, 8]], ["a", "b", "c"])
