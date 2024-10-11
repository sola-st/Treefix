# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
strategy, target = create_test_objects(
    cluster_spec=self._cluster_spec,
    task_type=task_type,
    task_id=task_id,
    num_gpus=num_gpus,
    num_tpus=num_tpus)

if use_devices_arg and num_gpus > 0:
    devices = ['GPU:%d' % i for i in range(num_gpus)]
    # Temporary workaround to manually set the `_extended` field before device
    # initialization is exposed as a public interface.
    strategy._extended = CollectiveAllReduceExtended(
        container_strategy=strategy,
        cluster_resolver=None,
        communication_options=collective_util.Options(),
        devices=devices)
    # Manually set the field since the workaround bypasses the base
    # contructor, resulting in the absence of this field.
    strategy._extended._retrace_functions_for_each_device = (num_gpus > 1)

exit((strategy, target))
