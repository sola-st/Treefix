# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
# Shallow tree ends at scalar.
input_tree = [[[2, 2], [3, 3]], [[4, 9], [5, 5]]]
shallow_tree = [[True, True], [False, True]]
flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_input_tree, [[2, 2], [3, 3], [4, 9], [5, 5]])
self.assertEqual(flattened_shallow_tree, [True, True, False, True])

# Shallow tree ends at string.
input_tree = [[("a", 1), [("b", 2), [("c", 3), [("d", 4)]]]]]
shallow_tree = [["level_1", ["level_2", ["level_3", ["level_4"]]]]]
input_tree_flattened_as_shallow_tree = nest.flatten_up_to(shallow_tree,
                                                          input_tree)
input_tree_flattened = nest.flatten(input_tree)
self.assertEqual(input_tree_flattened_as_shallow_tree,
                 [("a", 1), ("b", 2), ("c", 3), ("d", 4)])
self.assertEqual(input_tree_flattened, ["a", 1, "b", 2, "c", 3, "d", 4])

# Make sure dicts are correctly flattened, yielding values, not keys.
input_tree = {"a": 1, "b": {"c": 2}, "d": [3, (4, 5)]}
shallow_tree = {"a": 0, "b": 0, "d": [0, 0]}
input_tree_flattened_as_shallow_tree = nest.flatten_up_to(shallow_tree,
                                                          input_tree)
self.assertEqual(input_tree_flattened_as_shallow_tree,
                 [1, {"c": 2}, 3, (4, 5)])

# Namedtuples.
ab_tuple = NestTest.ABTuple
input_tree = ab_tuple(a=[0, 1], b=2)
shallow_tree = ab_tuple(a=0, b=1)
input_tree_flattened_as_shallow_tree = nest.flatten_up_to(shallow_tree,
                                                          input_tree)
self.assertEqual(input_tree_flattened_as_shallow_tree,
                 [[0, 1], 2])

# Nested dicts, OrderedDicts and namedtuples.
input_tree = collections.OrderedDict(
    [("a", ab_tuple(a=[0, {"b": 1}], b=2)),
     ("c", {"d": 3, "e": collections.OrderedDict([("f", 4)])})])
shallow_tree = input_tree
input_tree_flattened_as_shallow_tree = nest.flatten_up_to(shallow_tree,
                                                          input_tree)
self.assertEqual(input_tree_flattened_as_shallow_tree, [0, 1, 2, 3, 4])
shallow_tree = collections.OrderedDict([("a", 0), ("c", {"d": 3, "e": 1})])
input_tree_flattened_as_shallow_tree = nest.flatten_up_to(shallow_tree,
                                                          input_tree)
self.assertEqual(input_tree_flattened_as_shallow_tree,
                 [ab_tuple(a=[0, {"b": 1}], b=2),
                  3,
                  collections.OrderedDict([("f", 4)])])
shallow_tree = collections.OrderedDict([("a", 0), ("c", 0)])
input_tree_flattened_as_shallow_tree = nest.flatten_up_to(shallow_tree,
                                                          input_tree)
self.assertEqual(input_tree_flattened_as_shallow_tree,
                 [ab_tuple(a=[0, {"b": 1}], b=2),
                  {"d": 3, "e": collections.OrderedDict([("f", 4)])}])

## Shallow non-list edge-case.
# Using iterable elements.
input_tree = ["input_tree"]
shallow_tree = "shallow_tree"
flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_input_tree, [input_tree])
self.assertEqual(flattened_shallow_tree, [shallow_tree])

input_tree = ["input_tree_0", "input_tree_1"]
shallow_tree = "shallow_tree"
flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_input_tree, [input_tree])
self.assertEqual(flattened_shallow_tree, [shallow_tree])

# Using non-iterable elements.
input_tree = [0]
shallow_tree = 9
flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_input_tree, [input_tree])
self.assertEqual(flattened_shallow_tree, [shallow_tree])

input_tree = [0, 1]
shallow_tree = 9
flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_input_tree, [input_tree])
self.assertEqual(flattened_shallow_tree, [shallow_tree])

## Both non-list edge-case.
# Using iterable elements.
input_tree = "input_tree"
shallow_tree = "shallow_tree"
flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_input_tree, [input_tree])
self.assertEqual(flattened_shallow_tree, [shallow_tree])

# Using non-iterable elements.
input_tree = 0
shallow_tree = 0
flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_input_tree, [input_tree])
self.assertEqual(flattened_shallow_tree, [shallow_tree])

## Input non-list edge-case.
# Using iterable elements.
input_tree = "input_tree"
shallow_tree = ["shallow_tree"]
expected_message = ("If shallow structure is a sequence, input must also "
                    "be a sequence. Input has type: <(type|class) 'str'>.")
with self.assertRaisesRegex(TypeError, expected_message):
    flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_shallow_tree, shallow_tree)

input_tree = "input_tree"
shallow_tree = ["shallow_tree_9", "shallow_tree_8"]
with self.assertRaisesRegex(TypeError, expected_message):
    flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_shallow_tree, shallow_tree)

# Using non-iterable elements.
input_tree = 0
shallow_tree = [9]
expected_message = ("If shallow structure is a sequence, input must also "
                    "be a sequence. Input has type: <(type|class) 'int'>.")
with self.assertRaisesRegex(TypeError, expected_message):
    flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_shallow_tree, shallow_tree)

input_tree = 0
shallow_tree = [9, 8]
with self.assertRaisesRegex(TypeError, expected_message):
    flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_shallow_tree, shallow_tree)

input_tree = [(1,), (2,), 3]
shallow_tree = [(1,), (2,)]
expected_message = nest._STRUCTURES_HAVE_MISMATCHING_LENGTHS.format(
    input_length=len(input_tree), shallow_length=len(shallow_tree))
with self.assertRaisesRegex(ValueError, expected_message):  # pylint: disable=g-error-prone-assert-raises
    nest.assert_shallow_structure(shallow_tree, input_tree)
