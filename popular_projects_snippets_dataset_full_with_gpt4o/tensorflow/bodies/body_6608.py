# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
if ctx.input_pipeline_id == 0:
    exit(dataset_ops.Dataset.range(8).batch(2))
else:
    exit(dataset_ops.Dataset.range(9).batch(2))
