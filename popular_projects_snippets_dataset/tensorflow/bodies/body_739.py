# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/concat_ops_test.py
if "CPU" in self.device:
    self.skipTest("This test can time out on CPU, so we will just allow "
                  "other backends to catch this specific error.")
with self.session():
    with self.test_scope():
        for concat_dim in range(2):
            params = {}
            p = []
            shape = np.array([7, 13])
            num_tensors = 1001
            for i in np.arange(num_tensors):
                input_shape = shape
                placeholder = array_ops.placeholder(
                    dtypes.float32, shape=input_shape)
                p.append(placeholder)
                params[placeholder] = np.random.rand(*input_shape).astype(
                    np.float32)

            concat_inputs = p
            c = array_ops.concat(concat_inputs, concat_dim)
            result = c.eval(feed_dict=params)

            self.assertEqual(result.shape, c.get_shape())
            cur_offset = 0

            for i in np.arange(num_tensors):
                # The index into the result is the ':' along all dimensions
                # except the concat_dim. slice(0, size) is used for ':', and
                # a list of slices is used to index into result.
                index = [slice(0, params[p[i]].shape[j]) for j in np.arange(2)]
                index[concat_dim] = slice(
                    cur_offset, cur_offset + params[p[i]].shape[concat_dim])
                cur_offset += params[p[i]].shape[concat_dim]
                self.assertAllEqual(result[tuple(index)], params[p[i]])
