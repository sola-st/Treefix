# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/models.py
"""Utility function to centralize checkpoint restoration.

  Args:
    sess: TensorFlow session.
    start_checkpoint: Path to saved checkpoint on disk.
  """
saver = tf.compat.v1.train.Saver(tf.compat.v1.global_variables())
saver.restore(sess, start_checkpoint)
