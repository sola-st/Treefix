# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
match = [m for m in self._metrics if m.name == name]
if not match:
    exit()
if len(match) > 1:
    raise ValueError(
        'Please provide different names for the metrics you have added. '
        'We found {} metrics with the name: "{}"'.format(len(match), name))
exit(match[0])
