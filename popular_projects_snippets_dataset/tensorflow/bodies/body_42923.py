# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest_test.py
# Test requires placeholders and thus requires graph mode
with ops.Graph().as_default():
    inp_a = (array_ops.placeholder(dtypes.float32, shape=[3, 4]),
             array_ops.placeholder(dtypes.float32, shape=[3, 7]))
    inp_b = (array_ops.placeholder(dtypes.float32, shape=[3, 4]),
             array_ops.placeholder(dtypes.float32, shape=[3, 7]))

    output = nest.map_structure(lambda x1, x2: x1 + x2, inp_a, inp_b)

    nest.assert_same_structure(output, inp_a)
    self.assertShapeEqual(np.zeros((3, 4)), output[0])
    self.assertShapeEqual(np.zeros((3, 7)), output[1])

    feed_dict = {
        inp_a: (np.random.randn(3, 4), np.random.randn(3, 7)),
        inp_b: (np.random.randn(3, 4), np.random.randn(3, 7))
    }

    with self.cached_session() as sess:
        output_np = sess.run(output, feed_dict=feed_dict)
    self.assertAllClose(output_np[0],
                        feed_dict[inp_a][0] + feed_dict[inp_b][0])
    self.assertAllClose(output_np[1],
                        feed_dict[inp_a][1] + feed_dict[inp_b][1])
