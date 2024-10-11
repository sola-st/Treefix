# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/concat_ops_test.py
# Random dims of rank 5
shape = np.random.randint(1, 5, size=5)
# Random number of tensors, but always > 1.
num_tensors = np.random.randint(2, 10)
# Random dim to concat on
concat_dim = np.random.randint(5)
params = {}
if dtype == dtypes.bfloat16:
    dtype_feed = dtypes.float32
else:
    dtype_feed = dtype
with self.session():
    p = []
    for i in np.arange(num_tensors):
        input_shape = shape
        input_shape[concat_dim] = np.random.randint(1, 5)
        placeholder = array_ops.placeholder(dtype_feed, shape=input_shape)
        p.append(placeholder)

        t = dtype_feed.as_numpy_dtype
        params[placeholder] = np.random.rand(*input_shape).astype(t)

    if dtype != dtype_feed:
        concat_inputs = [math_ops.cast(p_i, dtype) for p_i in p]
    else:
        concat_inputs = p
    with self.test_scope():
        c = array_ops.concat(concat_inputs, concat_dim)
        if dtype != dtype_feed:
            c = math_ops.cast(c, dtype_feed)
    result = c.eval(feed_dict=params)

self.assertEqual(result.shape, c.get_shape())
cur_offset = 0

for i in np.arange(num_tensors):
    # The index into the result is the ':' along all dimensions
    # except the concat_dim. slice(0, size) is used for ':', and
    # a list of slices is used to index into result.
    ind = [slice(0, params[p[i]].shape[j]) for j in np.arange(5)]
    ind[concat_dim] = slice(cur_offset,
                            cur_offset + params[p[i]].shape[concat_dim])
    cur_offset += params[p[i]].shape[concat_dim]
    if dtype == dtype_feed:
        self.assertAllEqual(result[tuple(ind)], params[p[i]])
    else:
        self.assertAllClose(result[tuple(ind)], params[p[i]], 0.01)
