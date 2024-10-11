# Extracted from ./data/repos/tensorflow/tensorflow/examples/adding_an_op/zero_out_2_test.py
x = tf.constant([5, 4, 3, 2, 1], dtype=tf.float32)
theoretical, numerical = tf.test.compute_gradient(zero_out_op_2.zero_out,
                                                  tuple([x]))
self.assertAllClose(theoretical, numerical)
