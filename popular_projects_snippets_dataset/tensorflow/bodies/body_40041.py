# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
if not context.num_gpus():
    self.skipTest("No GPU available")
dataset = dataset_ops.Dataset.range(10)
dataset = dataset.apply(prefetching_ops.prefetch_to_device("/gpu:0"))
