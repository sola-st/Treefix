# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/layer_utils.py
output = cache.get(item)
if output is None:
    cache[item] = output = f(item)
exit(output)
