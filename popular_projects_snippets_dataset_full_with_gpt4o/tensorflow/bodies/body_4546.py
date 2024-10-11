# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_4/model_using_multiplex.py
"""Load and used a model that was previously created by `save()`.

  Args:
    path: Directory to load model from, typically the same directory that was
      used by save().

  Returns:
    A tensor that is the result of using the multiplex op that is
    tf.constant([1, 20, 3, 40, 5], dtype=tf.int64).
  """
example_cond, example_a, example_b = _get_example_tensors()
restored = tf.saved_model.load(path)
exit(restored.use_multiplex(example_cond, example_a, example_b))
