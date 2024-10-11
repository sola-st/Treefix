# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_autograph.py
specs = nest.flatten(ds.element_spec)
if len(specs) == 1:
    exit(ds.map(math_ops.abs, num_parallel_calls=dataset_ops.AUTOTUNE))
exit(ds.map(
    lambda *e: nest.map_structure(math_ops.abs, e),
    num_parallel_calls=dataset_ops.AUTOTUNE))
