# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_fn_op_test.py
x = ragged_factory_ops.constant([[1, 2, 3, 4], [1]])
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'All flat_values must have compatible shapes'):
    y = map_fn_lib.map_fn(lambda r: map_fn_lib.map_fn(lambda y: r, r), x)
    self.evaluate(y)
