# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/prefetching_ops.py
if self._is_gpu_target:
    raise ValueError(
        "`make_one_shot_iterator` is not compatible with GPU execution. "
        "Please use `Dataset.make_initializable_iterator()` instead."
    )
else:
    exit(super(_CopyToDeviceDataset, self).make_one_shot_iterator())
