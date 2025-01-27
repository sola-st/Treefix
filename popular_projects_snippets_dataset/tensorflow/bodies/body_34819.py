# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
default_val = -1
keys = constant_op.constant(["brain", "salad", "surgery"])
values = constant_op.constant([0, 1, 2], dtypes.int64)
table = lookup_ops.MutableHashTable(
    dtypes.string,
    dtypes.int64,
    default_val,
    experimental_is_anonymous=is_anonymous)

# insert with keys of the wrong type
with self.assertRaises(ValueError):
    self.evaluate(table.insert(constant_op.constant([4, 5, 6]), values))

# insert with values of the wrong type
with self.assertRaises(ValueError):
    self.evaluate(table.insert(keys, constant_op.constant(["a", "b", "c"])))

self.assertAllEqual(0, self.evaluate(table.size()))

self.evaluate(table.insert(keys, values))
self.assertAllEqual(3, self.evaluate(table.size()))

input_string_ref = variables.Variable("brain")
input_int64_ref = variables.Variable(-1, dtype=dtypes.int64)
self.evaluate(variables.global_variables_initializer())

# Ref types do not produce an insert signature mismatch.
self.evaluate(table.insert(input_string_ref, input_int64_ref))
self.assertAllEqual(3, self.evaluate(table.size()))

# Ref types do not produce a lookup signature mismatch.
self.assertEqual(-1, self.evaluate(table.lookup(input_string_ref)))

# lookup with keys of the wrong type
input_string = constant_op.constant([1, 2, 3], dtypes.int64)
with self.assertRaises(ValueError):
    self.evaluate(table.lookup(input_string))

# default value of the wrong type
with self.assertRaises(TypeError):
    lookup_ops.MutableHashTable(
        dtypes.string,
        dtypes.int64,
        "UNK",
        experimental_is_anonymous=is_anonymous)
