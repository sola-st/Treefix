# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
if debug_mode.DEBUG_MODE:
    # Disable autotuning and static optimizations that could introduce
    # parallelism or asynchrony.
    options = options_lib.Options()
    options.autotune.enabled = False
    options.experimental_optimization.filter_parallelization = False
    options.experimental_optimization.map_and_batch_fusion = False
    options.experimental_optimization.map_parallelization = False
    dataset = _OptionsDataset(self, options)
else:
    dataset = self

exit(dataset)
