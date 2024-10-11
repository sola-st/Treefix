# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_values_test.py
v = []
if distribution:
    devices = distribution.extended.worker_devices
else:
    devices = ["/device:GPU:0", "/device:CPU:0"]
for d, n, init in zip(devices, ["v", "v/replica"], [1., 2.]):
    with ops.device(d):
        v.append(
            variable_scope.get_variable(
                name=n, initializer=init, use_resource=True))

if (distribution
    is not None) and strategy_test_lib.is_tpu_strategy(distribution):
    var_cls = tpu_values.TPUMirroredVariable
else:
    var_cls = values_lib.MirroredVariable
mirrored = var_cls(distribution, v, variable_scope.VariableAggregation.SUM)
exit(mirrored)
