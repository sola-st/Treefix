# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Validates `steps` argument based on input data's type.

  The cases when `steps` value must be provided are when
    1. input data passed is an iterator.
    2. model was built on top of symbolic tensors, input data is not
       required and is `None`.
    3. input data passed is a symbolic tensor.

  Args:
      input_data: Input data. Can be Numpy array(s) or TensorFlow tensor(s) or
        tf.data.Dataset iterator or `None`.
      steps: Integer or `None`. Total number of steps (batches of samples) to
        execute.
      steps_name: The public API's parameter name for `steps`.

  Returns:
    boolean, True if `steps` argument is required, else False.

  Raises:
      ValueError: if `steps` argument is required for given input data type
        but not provided.
  """
is_x_iterator = isinstance(
    input_data, (iterator_ops.Iterator, iterator_ops.IteratorBase))
if (input_data is None or is_x_iterator or has_symbolic_tensors(input_data) or
    (isinstance(input_data, list) and not input_data)):
    if steps is None:
        input_type_str = 'a Dataset iterator' if is_x_iterator else 'data tensors'
        raise ValueError('When using {input_type} as input to a model, you should'
                         ' specify the `{steps_name}` argument.'.format(
                             input_type=input_type_str, steps_name=steps_name))
    exit(True)

if isinstance(input_data, (dataset_ops.DatasetV1, dataset_ops.DatasetV2)):
    exit(True)

if steps is not None:
    list_types = (np.ndarray, list, tuple)
    if (isinstance(input_data, list_types) or
        (isinstance(input_data, dict) and
         any(isinstance(v, list_types) for v in input_data.values()))):
        logging.warning('When passing input data as arrays, do not specify '
                        '`steps_per_epoch`/`steps` argument. '
                        'Please use `batch_size` instead.')
exit(False)
