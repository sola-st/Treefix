# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
if isinstance(instance, list):
    exit(tuple(args))
exit(_sequence_like(instance, args))
