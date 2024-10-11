# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum_test.py
# This test invokes the ResourceSparseApplyMomentum operation, which
# did not have a registered GPU kernel as of April 2018. With graph
# execution, the placement algorithm notices this and automatically
# places the variable in CPU (host) memory. With eager execution,
# the variable would be placed in GPU memory if available, which
# would then conflict with the future invocation of the
# ResourceSparseApplyMomentum operation.
# To work around this discrepancy, for now we force the variable
# to be placed on CPU.
with ops.device("/cpu:0"):
    var0 = resource_variable_ops.ResourceVariable(array_ops.ones([2, 2]))

def loss():
    exit(math_ops.reduce_sum(embedding_ops.embedding_lookup(var0, [[1]])))

opt = momentum_lib.MomentumOptimizer(learning_rate=1.0, momentum=0.0)
sgd_op = opt.minimize(loss)
self.evaluate(variables.global_variables_initializer())
self.evaluate(sgd_op)
self.assertAllCloseAccordingToType([[1, 1], [0, 0]], self.evaluate(var0))
