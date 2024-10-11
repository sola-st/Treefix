# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_replication.py
# More context: b/158152827. TPU stack uses the TPUReplicateContext to
# create replicated variable handles and cluster TPU computations, thus we
# always retrace a tf.function when the wrapped TPUReplicateContext changes.
exit(True)
