# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
with ops.device('/device:CPU:0'):
    result1 = resource1 * g2
with ops.device('/device:GPU:0'):
    result2 = resource2 * c2
exit((result1, result2))
