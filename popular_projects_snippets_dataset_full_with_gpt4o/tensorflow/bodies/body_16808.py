# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/collective_ops_test.py
t0 = [0, 1, 2, 3, 4, 5, 6, 7]
t1 = [10, 11, 12, 13, 14, 15, 16, 17]
group_size = 2
group_key = 1
instance_key = 123
# Tests that execute collectives need to be enclosed in graph or tf.function
with ops.Graph().as_default():
    with self.session(
        config=config_pb2.ConfigProto(
            device_count={'CPU': group_size})) as sess:
        with ops.device('/CPU:0'):
            in0 = array_ops.placeholder(dtype=dtypes.int32, shape=[None])
            c0 = collective_ops.all_gather(in0, group_size, group_key,
                                           instance_key)
        with ops.device('/CPU:1'):
            in1 = array_ops.placeholder(dtype=dtypes.int32, shape=[None])
            c1 = collective_ops.all_gather(in1, group_size, group_key,
                                           instance_key)

        results = sess.run([c0, c1], feed_dict={in0: t0, in1: t1})
        results_ = sess.run([c0, c1], feed_dict={in0: t0[1:], in1: t1[1:]})

expected_output = [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17]
self.assertAllClose(results[0], expected_output, rtol=1e-5, atol=1e-5)
self.assertAllClose(results[1], expected_output, rtol=1e-5, atol=1e-5)

expected_output_ = [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 16, 17]
self.assertAllClose(results_[0], expected_output_, rtol=1e-5, atol=1e-5)
self.assertAllClose(results_[1], expected_output_, rtol=1e-5, atol=1e-5)
