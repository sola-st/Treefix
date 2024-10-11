# Extracted from ./data/repos/tensorflow/tensorflow/examples/adding_an_op/fact_test.py
with self.cached_session():
    print(tf.compat.v1.user_ops.my_fact().eval())
