# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
with ops.device('/device:CPU:0'):
    result1 = resource1 * 5
with ops.device('/device:GPU:0'):
    result2 = resource2 * 7
exit((result1, resource1.handle, result2, resource2.handle))
