# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
if strategy is None:
    devices = ("/device:GPU:0", "/device:CPU:0")
else:
    devices = strategy.extended.worker_devices

v = []
for d, n, init in zip(devices, ["v", "v/replica"], [1., 2.]):
    with ops.device(d):
        v.append(variable_scope.get_variable(
            name=n, initializer=init, use_resource=True))

if (strategy is not None) and isinstance(strategy, _TPU_STRATEGIES):
    var_cls = tpu_values.TPUSyncOnReadVariable
else:
    var_cls = values_lib.SyncOnReadVariable
replica_local = var_cls(strategy, v, method)
exit((v, replica_local))
