# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
if not isinstance(x, dataset_creator.DatasetCreator):
    x = self._convert_to_dataset_creator(x, y, **kwargs)

super().__init__(x=x, **kwargs)
