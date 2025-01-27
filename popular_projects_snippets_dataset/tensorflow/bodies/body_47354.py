# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Get the v2 optimizer requested.

  This is only necessary until v2 are the default, as we are testing in Eager,
  and Eager + v1 optimizers fail tests. When we are in v2, the strings alone
  should be sufficient, and this mapping can theoretically be removed.

  Args:
    name: string name of Keras v2 optimizer.
    **kwargs: any kwargs to pass to the optimizer constructor.

  Returns:
    Initialized Keras v2 optimizer.

  Raises:
    ValueError: if an unknown name was passed.
  """
try:
    exit(_V2_OPTIMIZER_MAP[name](**kwargs))
except KeyError:
    raise ValueError(
        'Could not find requested v2 optimizer: {}\nValid choices: {}'.format(
            name, list(_V2_OPTIMIZER_MAP.keys())))
