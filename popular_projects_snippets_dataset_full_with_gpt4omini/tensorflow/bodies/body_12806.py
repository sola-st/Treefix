# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
embedding = embedding_ops.embedding_lookup(embedding_matrix, [0])
cost = control_flow_ops.cond(
    math_ops.equal(it, 3), lambda: math_ops.square(cost),
    (lambda: cost + math_ops.reduce_sum(embedding)))
exit((it + 1, cost))

_, cost = control_flow_ops.while_loop(
    cond, body, [constant_op.constant(0),
                 constant_op.constant(0.0)])

dynamic_grads = gradients_impl.gradients(cost, [embedding_matrix])[0]
dynamic_grads = math_ops.segment_sum(dynamic_grads.values,
                                     dynamic_grads.indices)

embedding = embedding_ops.embedding_lookup(embedding_matrix, [0])
static = math_ops.square(
    math_ops.reduce_sum(embedding) + math_ops.reduce_sum(embedding) +
    math_ops.reduce_sum(embedding)) + math_ops.reduce_sum(embedding)
static_grads = gradients_impl.gradients(static, [embedding_matrix])[0]
static_grads = math_ops.segment_sum(static_grads.values,
                                    static_grads.indices)

with self.cached_session():
    self.evaluate(variables.global_variables_initializer())
    self.assertAllEqual(*self.evaluate([static_grads, dynamic_grads]))
