# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
deindent = lambda n, s: "\n".join(line[n:] for line in s.split("\n"))
text = deindent(4, """
    import tensorflow as tf
    tf.enable_eager_execution()
    writer = tf.contrib.summary.create_file_writer(
        "/tmp/migration_test", flush_millis=1000)
    with writer.as_default(), tf.contrib.summary.always_record_summaries():
      tf.contrib.summary.scalar("loss", 0.42)
      tf.contrib.summary.histogram("weights", [1.0, 2.0], step=7)
      tf.contrib.summary.flush()
    """)
expected = deindent(4, """
    import tensorflow as tf
    tf.compat.v1.enable_eager_execution()
    writer = tf.compat.v2.summary.create_file_writer(
        logdir="/tmp/migration_test", flush_millis=1000)
    with writer.as_default(), tf.compat.v2.summary.record_if(True):
      tf.compat.v2.summary.scalar(name="loss", data=0.42, step=tf.compat.v1.train.get_or_create_global_step())
      tf.compat.v2.summary.histogram(name="weights", data=[1.0, 2.0], step=7)
      tf.compat.v2.summary.flush()
    """)
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
