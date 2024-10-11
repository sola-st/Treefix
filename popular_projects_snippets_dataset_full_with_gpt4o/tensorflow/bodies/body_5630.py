# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
with ops.device(strategy.extended.parameter_devices[1]):
    v.assign(2.)
