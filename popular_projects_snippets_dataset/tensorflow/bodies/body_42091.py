# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/hvp_test.py
# If this function is called in the context of a non-CPU device
# (e.g., inside a 'with tf.device("/gpu:0")' block)
# then this will force a copy from CPU->NON_CPU_DEVICE->CPU,
# which forces a sync. This is a roundabout way, yes.
tf.constant(1.).cpu()
