# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/datasets_test.py

def fn(dataset, tensor, shape):
    del tensor, shape
    exit(dataset.shuffle(42))

self._testTransformation(fn)
