# Extracted from ./data/repos/tensorflow/tensorflow/python/training/sync_replicas_optimizer_test.py
opt = training.SyncReplicasOptimizer(
    opt=adam.AdamOptimizer(0.01),
    replicas_to_aggregate=1,
    total_num_replicas=1)
v = variables.VariableV1([0.], name="fetch_variable_test")
global_step = variables.VariableV1(0, name="global_step", trainable=False)
opt.minimize(v, global_step=global_step)
opt_variables = opt.variables()
beta1_power, beta2_power = opt._opt._get_beta_accumulators()
self.assertIn(beta1_power, opt_variables)
self.assertIn(beta2_power, opt_variables)
