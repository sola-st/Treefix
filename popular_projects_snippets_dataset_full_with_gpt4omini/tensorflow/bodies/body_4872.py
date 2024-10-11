# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/tpu_memory_test.py
super().setUp()
# Clear all cached tensors
context._reset_context()
# Run garbage collection to free any tensors from previous
# runs.
gc.collect()

# Run a small program and copy the result to CPU.
# This causes deferred deallocations to be flushed and new memory to be
# allocated in a less fragmented way.
# Turning deferred deallocations off no longer seems to work.
assert tf.reduce_sum(tf.random.uniform(
    (1024, 128), dtype=tf.float32)).numpy() > 1.0

self.resolver = tf.distribute.cluster_resolver.TPUClusterResolver(
    tpu="", project=None, zone=None)

tf.config.experimental_connect_to_cluster(self.resolver)
tf.tpu.experimental.initialize_tpu_system(self.resolver)
