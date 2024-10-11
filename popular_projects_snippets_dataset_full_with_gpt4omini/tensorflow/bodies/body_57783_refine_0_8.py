tf = type('Mock', (object,), {})() # pragma: no cover
tf.data = type('Mock', (object,), {})() # pragma: no cover
tf.data.Dataset = type('Mock', (object,), {})() # pragma: no cover
tf.data.Dataset.range = staticmethod(lambda x: [i for i in range(x)]) # pragma: no cover
tf.data.Dataset.shuffle = lambda self, buffer_size, reshuffle_each_iteration: self # pragma: no cover

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
