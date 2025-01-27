# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
gpus = tf_config.list_physical_devices('GPU')
if len(gpus) > 1:
    self.skipTest('Skip logical device test on multi GPUs, since partial GPU '
                  'virtualization is not permitted.')
# Cannot change logical device after the context initialization.
context._reset_context()  # pylint: disable=protected-access
cluster_spec = multi_worker_test_base.create_cluster_spec(
    has_chief=False, num_workers=1)
resolver = cluster_resolver_lib.SimpleClusterResolver(
    cluster_spec=multi_worker_util.normalize_cluster_spec(cluster_spec),
    task_type='worker',
    task_id=0)

logical_gpus = len(gpus) * 2
for i, device in enumerate(gpus):
    n = (i + 1) * logical_gpus // len(gpus) - i * logical_gpus // len(gpus)
    assert n > 0  # guaranteed if count >= len(devices)
    configs = []
    for ordinal in range(n):
        config = context.LogicalDeviceConfiguration(
            memory_limit=64,
            experimental_device_ordinal=ordinal)
        configs.append(config)

    tf_config.set_logical_device_configuration(device, configs)

collective_all_reduce_strategy.CollectiveAllReduceStrategy(
    cluster_resolver=resolver)
# Since we create two logical GPUs out of the last GPU, there should be one
# more logical GPUs than physical GPUs.
self.assertLen(tf_config.list_logical_devices('GPU'), logical_gpus)
context._reset_context()  # pylint: disable=protected-access
