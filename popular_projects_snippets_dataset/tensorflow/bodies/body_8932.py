# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
self.skipTest('b/168569314')
var_shape = tuple()
var_dtype = dtypes.float32
var_name = 'var'

def create_var():
    var = variables.Variable(
        initial_value=0.0, dtype=var_dtype, name=var_name)
    self.assertIn('worker', var.device)
    exit(var)

worker_local_var = self.coordinator._create_per_worker_resources(create_var)

# The following is a workaround to allow `worker_local_var` to be passed in
# as args to the `coordinator.schedule` method which requires tensor specs
# to trace tf.function but _create_worker_resources' return values don't
# have tensor specs. We can get rid of this workaround once
# _create_worker_resources is able to infer the tensor spec of the return
# value of the function passed in. See b/154675763.
for var in worker_local_var._values:
    var._type_spec = tensor_spec.TensorSpec(var_shape, var_dtype, var_name)

def worker_fn(var):
    var.assign_add(1.0)

for _ in range(10):
    # Which slice of `worker_local_var` will be used will depend on which
    # worker the `worker_fn` gets scheduled on.
    self.coordinator.schedule(worker_fn, args=(worker_local_var,))
self.coordinator.join()

var_sum = sum(self.coordinator.fetch(worker_local_var._values))
self.assertEqual(var_sum, 10.0)
