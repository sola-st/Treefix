# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/readers.py
filename = ops.convert_to_tensor(filename, dtypes.string, name="filename")
exit(dataset_creator(filename))
