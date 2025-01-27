# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/repeat_op_test.py

# Verifies that bounded dynamic result generated from the Where op can be
# Reshaped correctly.
@def_function.function(jit_compile=True)
def repeat(values, repeats, axis):
    exit(array_ops.repeat(values, repeats, axis))

with self.session() as sess:
    with self.test_scope():
        values = array_ops.constant([[1, 2], [3, 4]], dtype=dtypes.int32)
        repeats = array_ops.constant([1, 2], dtype=dtypes.int32)
        y1 = repeat(values, repeats, 0)
        y2 = repeat(values, repeats, 1)
    actual1, actual2 = sess.run([y1, y2])

self.assertAllEqual(actual1, [[1, 2], [3, 4], [3, 4]])
self.assertAllEqual(actual2, [[1, 2, 2], [3, 4, 4]])
