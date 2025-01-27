# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest_test.py
input_tree = (((2, 2), (3, 3)), ((4, 9), (5, 5)))
shallow_tree = ((True, True), (False, True))
flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_input_tree, [(2, 2), (3, 3), (4, 9), (5, 5)])
self.assertEqual(flattened_shallow_tree, [True, True, False, True])

input_tree = ((("a", 1), (("b", 2), (("c", 3), (("d", 4))))))
shallow_tree = (("level_1", ("level_2", ("level_3", ("level_4")))))
input_tree_flattened_as_shallow_tree = nest.flatten_up_to(shallow_tree,
                                                          input_tree)
input_tree_flattened = nest.flatten(input_tree)
self.assertEqual(input_tree_flattened_as_shallow_tree,
                 [("a", 1), ("b", 2), ("c", 3), ("d", 4)])
self.assertEqual(input_tree_flattened, ["a", 1, "b", 2, "c", 3, "d", 4])

## Shallow non-list edge-case.
# Using iterable elements.
input_tree = ["input_tree"]
shallow_tree = "shallow_tree"
flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_input_tree, [input_tree])
self.assertEqual(flattened_shallow_tree, [shallow_tree])

input_tree = ("input_tree_0", "input_tree_1")
shallow_tree = "shallow_tree"
flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_input_tree, [input_tree])
self.assertEqual(flattened_shallow_tree, [shallow_tree])

# Using non-iterable elements.
input_tree = (0,)
shallow_tree = 9
flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_input_tree, [input_tree])
self.assertEqual(flattened_shallow_tree, [shallow_tree])

input_tree = (0, 1)
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
shallow_tree = ("shallow_tree",)
expected_message = ("If shallow structure is a sequence, input must also "
                    "be a sequence. Input has type: 'str'.")
with self.assertRaisesRegex(TypeError, expected_message):
    flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_shallow_tree, list(shallow_tree))

input_tree = "input_tree"
shallow_tree = ("shallow_tree_9", "shallow_tree_8")
with self.assertRaisesRegex(TypeError, expected_message):
    flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_shallow_tree, list(shallow_tree))

# Using non-iterable elements.
input_tree = 0
shallow_tree = (9,)
expected_message = ("If shallow structure is a sequence, input must also "
                    "be a sequence. Input has type: 'int'.")
with self.assertRaisesRegex(TypeError, expected_message):
    flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_shallow_tree, list(shallow_tree))

input_tree = 0
shallow_tree = (9, 8)
with self.assertRaisesRegex(TypeError, expected_message):
    flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_shallow_tree, list(shallow_tree))

# Using dict.
input_tree = {"a": ((2, 2), (3, 3)), "b": ((4, 9), (5, 5))}
shallow_tree = {"a": (True, True), "b": (False, True)}
flattened_input_tree = nest.flatten_up_to(shallow_tree, input_tree)
flattened_shallow_tree = nest.flatten_up_to(shallow_tree, shallow_tree)
self.assertEqual(flattened_input_tree, [(2, 2), (3, 3), (4, 9), (5, 5)])
self.assertEqual(flattened_shallow_tree, [True, True, False, True])
