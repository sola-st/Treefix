# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
with self.session():
    updates_placeholder = array_ops.placeholder(updates.dtype)
    indices_placeholder = array_ops.placeholder(indices.dtype)
    with self.test_scope():
        output = array_ops.scatter_nd(indices_placeholder, updates_placeholder,
                                      shape)
    feed_dict = {updates_placeholder: updates, indices_placeholder: indices}
    exit(output.eval(feed_dict=feed_dict))
