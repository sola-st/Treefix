# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/integration_test/tpu_memory_test.py
if not FLAGS.tpu_use_tfrt:
    self.skipTest(
        "TPU StreamExecutor does not support auto-defrag in allocation.")
with tf.device("TPU:0"):
    # DF has ~15G HBM. Following 7 buffers will consume most HBM.
    # pylint: disable=unused-variable
    buffer_2g_1 = tf.random.uniform((2, 256, 1024, 1024), dtype=tf.float32)
    buffer_2g_2 = tf.random.uniform((2, 256, 1024, 1024), dtype=tf.float32)
    buffer_2g_3 = tf.random.uniform((2, 256, 1024, 1024), dtype=tf.float32)
    buffer_2g_4 = tf.random.uniform((2, 256, 1024, 1024), dtype=tf.float32)
    buffer_2g_5 = tf.random.uniform((2, 256, 1024, 1024), dtype=tf.float32)
    buffer_2g_6 = tf.random.uniform((2, 256, 1024, 1024), dtype=tf.float32)
    buffer_2g_7 = tf.random.uniform((2, 256, 1024, 1024), dtype=tf.float32)
    #  pylint: enable=unused-variable

    # Deallocate two buffers.
    del buffer_2g_1, buffer_2g_3
    gc.collect()

    # The buffer we just deallocated doesn't provide enough contiguous region
    # for allocating 4G. This allocation will trigger auto-defrag.
    buffer_4g = tf.random.uniform((4, 256, 1024, 1024), dtype=tf.float32)

self.assertEndsWith(buffer_4g.device, "device:TPU:0")
