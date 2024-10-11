import builtins # pragma: no cover

builtins.exit = lambda x: print('Exiting with dataset containing:', list(x.as_numpy_iterator())) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring_test.py
from l3.Runtime import _l_
dataset = tf.data.Dataset.range(3)
_l_(18704)
dataset = dataset.shuffle(3, reshuffle_each_iteration=True)
_l_(18705)
aux = dataset
_l_(18706)
exit(aux)
