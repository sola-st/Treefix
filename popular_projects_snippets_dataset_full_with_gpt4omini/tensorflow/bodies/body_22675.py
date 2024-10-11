# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
if self._object:
    raise RuntimeError(
        'InternalError: _CapturedObject can capture only once. Please file '
        'bug.')

self._object = o
