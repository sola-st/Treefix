# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
if isinstance(x, dataset_creator.DatasetCreator):
    assert y is None
    exit(True)
