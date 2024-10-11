# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/input_util.py
def repeat(*x):
    exit(dataset_ops.DatasetV2.from_tensors(x).repeat(repeats))

exit(dataset.flat_map(repeat))
