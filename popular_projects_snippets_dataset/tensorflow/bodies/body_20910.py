# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum_test.py
# train.MomentumOptimizer is V1 only API.
with ops.Graph().as_default(), self.cached_session():
    db_grad, db_out = self._dbParamsMom01()
    num_samples = len(db_grad)
    var0 = variables.Variable([0.0] * num_samples)
    grads0 = constant_op.constant([0.0] * num_samples)
    mom_opt = momentum_lib.MomentumOptimizer(learning_rate=0.1, momentum=0.1)
    mom_update = mom_opt.apply_gradients(zip([grads0], [var0]))
    self.evaluate(variables.global_variables_initializer())
    for i in range(num_samples):
        mom_update.run(feed_dict={grads0: db_grad[i]})
        self.assertAllClose(np.array(db_out[i]), self.evaluate(var0))
