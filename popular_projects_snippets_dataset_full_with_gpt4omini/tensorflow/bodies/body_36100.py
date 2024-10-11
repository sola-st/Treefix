# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with self.cached_session() as sess, variable_scope.variable_scope(
    "foo", use_resource=True):
    var = variable_scope.get_variable("x", shape=[1, 1], dtype=dtypes.float32)
    placeholder = array_ops.placeholder(dtypes.float32)
    assign = var.assign(placeholder)
    sess.run(
        [assign],
        feed_dict={placeholder: np.zeros(shape=[2, 2], dtype=np.float32)})
