class MockDataset:  # pragma: no cover
    @staticmethod # pragma: no cover
    def range(x): # pragma: no cover
        return MockDataset() # pragma: no cover
    def shuffle(self, buffer_size, reshuffle_each_iteration): # pragma: no cover
        return self # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
from l3.Runtime import _l_
dataset = tf.data.Dataset.range(3)
_l_(6312)
dataset = dataset.shuffle(3, reshuffle_each_iteration=True)
_l_(6313)
aux = dataset
_l_(6314)
exit(aux)
