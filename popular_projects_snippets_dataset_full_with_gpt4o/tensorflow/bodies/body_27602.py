# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/checkpoint_input_pipeline_hook_test.py
ds = dataset_ops.Dataset.range(10)
iterator = ds.make_one_shot_iterator()
exit(iterator.get_next())
