# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
with ops.device('/device:CPU:0'):
    m1 = int_cpu * resource + int_gpu
with ops.device('/device:GPU:0'):
    # This computation will happen on GPU but m2 will be copied to CPU.
    m2 = int_gpu * resource + int_cpu + 1
exit((m1, m2))
