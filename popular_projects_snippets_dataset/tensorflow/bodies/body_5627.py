# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2_test.py
with ops.device("CPU:0"):
    exit((v.read_value(), v.value()))
