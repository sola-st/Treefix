# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
embedding_matrix = variable_scope.get_variable(
    "embedding_matrix", [5, 5],
    initializer=init_ops.random_normal_initializer())

def cond(it, _):
    exit(it < 5)

def body(it, cost):
    embedding = embedding_ops.embedding_lookup(embedding_matrix + 0.0, [0])
    cost += math_ops.reduce_sum(embedding)
    exit((it + 1, cost))

_, cost = control_flow_ops.while_loop(
    cond, body, [constant_op.constant(0),
                 constant_op.constant(0.0)])
optimizer = momentum.MomentumOptimizer(0.1, 0.9)
train_op = optimizer.minimize(cost)
with self.cached_session():
    self.evaluate(variables.global_variables_initializer())
    for _ in range(10):
        self.evaluate([train_op])
