# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
a = array_ops.placeholder(np.float32, shape=(2, 3))

c = xla.pad(
    a,
    padding_value=7,
    padding_low=[2, 1],
    padding_high=[1, 2],
    padding_interior=[1, 4])

self.assertEqual(c.shape, tensor_shape.TensorShape([6, 14]))

c = xla.pad(
    a,
    padding_value=7,
    padding_low=[2, -2],
    padding_high=[1, -2],
    padding_interior=[1, 2])

self.assertEqual(c.shape, tensor_shape.TensorShape([6, 3]))

c = xla.pad(
    array_ops.placeholder(np.float32, shape=(None, 2)),
    padding_value=7,
    padding_low=[0, 1],
    padding_high=[0, 2],
    padding_interior=[0, 4])
self.assertEqual(c.shape.as_list(), [None, 9])

# 0-sized input dimension and interior padding
c = xla.pad(
    array_ops.placeholder(np.float32, shape=(2, 0)),
    padding_value=7,
    padding_low=[2, 1],
    padding_high=[1, 1],
    padding_interior=[1, 2])

self.assertEqual(c.shape, tensor_shape.TensorShape([6, 2]))

with self.assertRaisesRegex(
    ValueError, 'padding_value input must be scalar, found rank 1 '):
    xla.pad(
        a,
        padding_value=[0, 1],
        padding_low=[0, 0],
        padding_high=[0, 0],
        padding_interior=[0, 0])

with self.assertRaisesRegex(ValueError,
                            'padding_low must be a 1D tensor of size 2 '):
    xla.pad(
        a,
        padding_value=7,
        padding_low=[0, 0, 0],
        padding_high=[0, 0],
        padding_interior=[0, 0])

with self.assertRaisesRegex(ValueError,
                            'padding_high must be a 1D tensor of size 2 '):
    xla.pad(
        a,
        padding_value=7,
        padding_low=[0, 0],
        padding_high=[0, 0, 0],
        padding_interior=[0, 0])

with self.assertRaisesRegex(
    ValueError, 'padding_interior must be a 1D tensor of size 2 '):
    xla.pad(
        a,
        padding_value=7,
        padding_low=[0, 0],
        padding_high=[0, 0],
        padding_interior=[0])

with self.assertRaisesRegex(
    ValueError,
    'padding_interior must contain only non-negative values, found -2 '):
    xla.pad(
        a,
        padding_value=7,
        padding_low=[0, 0],
        padding_high=[0, 0],
        padding_interior=[-2, 0])

with self.assertRaisesRegex(
    ValueError, 'resulting padded dimension has negative size -1 '):
    xla.pad(
        a,
        padding_value=7,
        padding_low=[-3, 0],
        padding_high=[0, 0],
        padding_interior=[0, 0])
