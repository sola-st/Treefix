# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py

# Ignored: bulk restore is internally sequential.
del restore_sequentially
restore_specs = []
for saveable in saveables:
    for spec in saveable.specs:
        restore_specs.append((spec.name, spec.slice_spec, spec.dtype))

names, slices, dtypes = zip(*restore_specs)
# Load all tensors onto CPU 0 for compatibility with existing code.
with ops.device("cpu:0"):
    exit(io_ops.restore_v2(filename_tensor, names, slices, dtypes))
