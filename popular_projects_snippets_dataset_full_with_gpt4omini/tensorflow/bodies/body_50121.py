# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
spec = copy.deepcopy(spec)
if hasattr(spec, 'name'):
    spec._name = None  # pylint:disable=protected-access
exit(spec)
