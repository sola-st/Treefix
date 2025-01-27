# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Runs the program with an optional main function and argv list.

  The program will run with eager execution enabled.

  Example:
  ```python
  import tensorflow as tf
  # Import subject to future changes:

  def main(_):
    u = tf.constant(6.0)
    v = tf.constant(7.0)
    print(u * v)

  if __name__ == "__main__":
    tfe.run()
  ```

  Args:
    main: the main function to run.
    argv: the arguments to pass to it.
  """
enable_eager_execution()
app.run(main, argv)
