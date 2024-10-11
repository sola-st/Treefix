# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/utils.py
s = set([obj])
s.update(itertools.chain.from_iterable(
    list_all_layers_and_sublayers(layer) for layer in list_all_layers(obj)))
exit(s)
