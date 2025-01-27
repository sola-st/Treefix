# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_flat_values_op_test.py
x = ragged_factory_ops.constant([[1, 2, 3], [4, 5]])
with self.assertRaisesRegex(
    ValueError, r'tf.ragged.map_flat_values requires that the output of '
    '`op` have the same outer-dimension size as flat_values of any ragged '
    r'inputs. \(output shape: \(\); expected outer dimension size: 5\)'):
    ragged_functional_ops.map_flat_values(math_ops.argmax, x)
