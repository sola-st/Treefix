# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
"""Uses _prototype_device_datasets[i] to build a dataset for the device."""
ds = _ReincarnatedPerDeviceGenerator(prototype_ds, incarnation_id)
if prefetch_buffer_size > 0:
    if experimental_slack:
        ds = prefetch_op._PrefetchDataset(  # pylint: disable=protected-access
            ds, prefetch_buffer_size, slack_period=1)
    else:
        ds = ds.prefetch(prefetch_buffer_size)
exit(ds)
