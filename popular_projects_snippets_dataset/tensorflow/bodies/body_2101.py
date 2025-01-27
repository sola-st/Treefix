# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
dtype = np.uint64
initial_state = array_ops.placeholder(np.uint64, shape=(2,))
shape = (2, 3)
res = xla.rng_bit_generator(algorithm, initial_state, shape, dtype=dtype)

self.assertEqual(res[0].shape, initial_state.shape)
self.assertEqual(res[1].shape, shape)

# The initial_state has unknown dimension size
initial_state = array_ops.placeholder(np.uint64, shape=(None,))
shape = (2, 3)
res = xla.rng_bit_generator(algorithm, initial_state, shape, dtype=dtype)

self.assertEqual(res[0].shape.as_list(), initial_state.shape.as_list())
self.assertEqual(res[1].shape, shape)

# The initial_state has unknown rank
initial_state = array_ops.placeholder(np.uint64, shape=None)
shape = (2, 3)
res = xla.rng_bit_generator(algorithm, initial_state, shape, dtype=dtype)

self.assertEqual(res[0].shape.as_list(), [None])
self.assertEqual(res[1].shape, shape)

# The output shape has unknown dimension
initial_state = array_ops.placeholder(np.uint64, shape=(None,))
shape = (None, 3)
with self.assertRaisesRegex(TypeError,
                            'Failed to convert elements .* to Tensor'):
    res = xla.rng_bit_generator(algorithm, initial_state, shape, dtype=dtype)
