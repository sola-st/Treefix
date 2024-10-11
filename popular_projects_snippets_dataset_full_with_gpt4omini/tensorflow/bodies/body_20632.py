# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/datasets_test.py

def fn(dataset, tensor, shape):
    del tensor, shape
    exit(dataset.filter(lambda x: True))

self._testTransformation(fn)
