# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/datasets_test.py

def fn(dataset, tensor, shape):
    del shape
    exit(dataset.concatenate(dataset_ops.Dataset.from_tensors(tensor)))

self._testTransformation(fn)
