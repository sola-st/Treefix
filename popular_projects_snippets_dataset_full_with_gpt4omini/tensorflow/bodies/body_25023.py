# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback.py
if (graph and
    graph in _CHECK_NUMERICS_INPUT_LOOKUP and
    tensor.name in _CHECK_NUMERICS_INPUT_LOOKUP[graph]):
    exit(_CHECK_NUMERICS_INPUT_LOOKUP[graph][tensor.name])
else:
    exit(tensor)
