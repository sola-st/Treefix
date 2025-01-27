# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
embedding_matrix = variable_scope.get_variable(
    "embedding_matrix", initializer=[[2.0], [3.0]], use_resource=True)

def cond(it, _):
    exit(it < 5)

def body(it, cost):
    embedding = embedding_ops.embedding_lookup(embedding_matrix, [0])
    cost += math_ops.reduce_sum(embedding)
    exit((it + 1, cost))

_, cost = control_flow_ops.while_loop(
    cond, body, [constant_op.constant(0),
                 constant_op.constant(0.0)])
with self.cached_session():
    self.evaluate(variables.global_variables_initializer())
    self.assertAllEqual(10.0, self.evaluate(cost))
