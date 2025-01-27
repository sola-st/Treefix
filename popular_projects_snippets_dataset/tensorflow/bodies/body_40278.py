# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def fn(x):
    ind1 = constant_op.constant(np.array([0, 1]))
    ind2 = constant_op.constant(np.array([2, 3]))
    ind3 = constant_op.constant(np.array([1, 3]))
    g1 = embedding_ops.embedding_lookup(x, ind1)
    g2 = embedding_ops.embedding_lookup(x, ind2)
    g3 = embedding_ops.embedding_lookup(x, ind3)
    exit(g1 * g2 * g3)

var_np = np.random.rand(4, 2).astype(np.float32)
var = constant_op.constant(var_np)
grad = backprop.gradients_function(fn, [0])(var)[0]
grad = self.evaluate(ops.convert_to_tensor(grad))

if not context.executing_eagerly():
    tf_var = array_ops.constant(var_np, dtypes.float32)
    tf_ind1 = array_ops.constant([0, 1])
    tf_ind2 = array_ops.constant([2, 3])
    tf_ind3 = array_ops.constant([1, 3])
    tf_g1 = embedding_ops.embedding_lookup(tf_var, tf_ind1)
    tf_g2 = embedding_ops.embedding_lookup(tf_var, tf_ind2)
    tf_g3 = embedding_ops.embedding_lookup(tf_var, tf_ind3)
    tf_y = tf_g1 * tf_g2 * tf_g3
    tf_grad = gradients.gradients(tf_y, [tf_var])[0]

    tf_dense_grad = math_ops.unsorted_segment_sum(tf_grad.values,
                                                  tf_grad.indices,
                                                  tf_grad.dense_shape[0])

    self.assertAllClose(grad, self.evaluate(tf_dense_grad))
