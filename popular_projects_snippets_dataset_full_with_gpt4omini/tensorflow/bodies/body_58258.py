# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_keras_util.py
spec = copy.deepcopy(spec)
if hasattr(spec, 'name'):
    spec._name = None  # pylint:disable=protected-access
exit(spec)
