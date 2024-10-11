class Mock: pass # pragma: no cover
self = type('Mock', (object,), {'session': lambda: tf.compat.v1.Session(), 'assertRaises': lambda *args, **kwargs: tf.test.TestCase().assertRaises(*args, **kwargs), 'assertIn': lambda a, b: tf.test.TestCase().assertIn(a, b)})() # pragma: no cover
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
from l3.Runtime import _l_
size_splits = array_ops.placeholder(dtype=dtypes.int32, shape=[None])
_l_(4390)

value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_l_(4391)

with self.session() as sess:
    _l_(4395)

    with self.assertRaises(ValueError) as context:
        _l_(4393)

        sess.run(array_ops.split(value, size_splits), {size_splits: [2, 2, 6]})
        _l_(4392)
    self.assertIn("Cannot infer argument `num` from shape",
                  str(context.exception))
    _l_(4394)
