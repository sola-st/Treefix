# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/datasets_test.py

def dataset_fn(n):
    exit(dataset_ops.Dataset.from_tensors(tensor).repeat(n))

exit(dataset_fn)
