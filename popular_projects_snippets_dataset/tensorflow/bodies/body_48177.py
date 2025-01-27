# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Runs validation checks on input and target data passed by the user.

    Also standardizes the data to lists of arrays, in order.

    Also builds and compiles the model on the fly if it is a subclassed model
    that has never been called before (and thus has no inputs/outputs).

    This is a purely internal method, subject to refactoring at any time.

    Args:
      x: Input data. It could be:
        - A Numpy array (or array-like), or a list of arrays
          (in case the model has multiple inputs).
        - A TensorFlow tensor, or a list of tensors
          (in case the model has multiple inputs).
        - A dict mapping input names to the corresponding array/tensors,
          if the model has named inputs.
        - A `tf.data` dataset.
      y: Target data. Like the input data `x`,
        it could be either Numpy array(s) or TensorFlow tensor(s).
        It should be consistent with `x` (you cannot have Numpy inputs and
        tensor targets, or inversely). If `x` is a dataset, `y` should not be
        specified (since targets will be obtained from the iterator).
      sample_weight: An optional sample-weight array passed by the user to
        weight the importance of each sample in `x`.
      class_weight: An optional class-weight array by the user to
        weight the importance of samples in `x` based on the class they belong
        to, as conveyed by `y`. If both `sample_weight` and `class_weight` are
        provided, the weights are multiplied.
      batch_size: Integer batch size. If provided, it is used to run additional
        validation checks on stateful models.
      check_steps: boolean, True if we want to check for validity of `steps` and
        False, otherwise. For example, when we are standardizing one batch of
        data for train_on_batch/predict_on_batch/test_on_batch APIs, `steps`
        value is not required and we should not check for its validity in these
        cases.
      steps_name: The public API's parameter name for `steps`.
      steps: Integer or `None`. Total number of steps (batches of samples) to
        execute.
      validation_split: Float between 0 and 1.
        Fraction of the training data to be used as validation data.
      shuffle: Boolean whether to shuffle the training data before each epoch.
      extract_tensors_from_dataset: Boolean. When `x` is a dataset instance,
        this indicates whether to extract actual tensors from the dataset or
        instead output the dataset instance itself.
        Set to True when calling from `train_on_batch`/etc.

    Returns:
      A tuple of 3: inputs (arrays or dicts, depending on whether `x` was a dict
      or not), target arrays, sample-weight arrays.
      If the model's input and targets are symbolic, these lists are empty
      (since the model takes no user-provided data, instead the data comes
      from the symbolic inputs/targets).

    Raises:
      ValueError: In case of invalid user-provided data.
      RuntimeError: If the model was never compiled.
    """
if isinstance(x, (dataset_ops.DatasetV1, dataset_ops.DatasetV2)):
    # Graph mode dataset. We'll pass the dataset as-is (unless
    # `extract_tensors_from_dataset` is True, in which case we extract
    # the tensors from the dataset and we output them.
    training_utils_v1.validate_dataset_input(x, y, sample_weight,
                                             validation_split)
    if shuffle:
        training_utils_v1.verify_dataset_shuffled(x)

    is_dataset = True
    if extract_tensors_from_dataset:
        # We do this for `train_on_batch`/etc.
        x, y, sample_weight = training_utils_v1.extract_tensors_from_dataset(x)
elif isinstance(x, iterator_ops.Iterator):
    # Graph mode iterator. We extract the symbolic tensors.
    training_utils_v1.validate_dataset_input(x, y, sample_weight,
                                             validation_split)
    iterator = x
    x, y, sample_weight = training_utils_v1.unpack_iterator_input(iterator)
    is_dataset = True
else:
    is_dataset = False

# Validates `steps` argument based on x's type.
if check_steps:
    training_utils_v1.check_steps_argument(x, steps, steps_name)

# First, we build the model on the fly if necessary.
if not self.inputs:
    all_inputs, y_input, dict_inputs = self._build_model_with_inputs(x, y)
    is_build_called = True
else:
    all_inputs = []
    # Whether this is a subclassed model that expects dictionary inputs
    # rather than list inputs (e.g. FeatureColumn-based models).
    dict_inputs = isinstance(self.inputs, dict)
    is_build_called = False
    y_input = y

# Second, we compile the model on the fly if necessary, mostly for subclass
# models.
is_compile_called = False
if not self._is_compiled and self.optimizer:
    self._compile_from_inputs(all_inputs, y_input, x, y)
    is_compile_called = True

# In graph mode, if we had just set inputs and targets as symbolic tensors
# by invoking build and compile on the model respectively, we do not have to
# feed anything to the model. Model already has input and target data as
# part of the graph.
# Note: in this case, `any` and `all` are equivalent since we disallow
# mixed symbolic/value inputs.

# self.run_eagerly is not free to compute, so we want to reuse the value.
run_eagerly = self.run_eagerly

if (not run_eagerly and is_build_called and is_compile_called and
    not is_dataset  and any(_is_symbolic_tensor(v) for v in all_inputs)):
    exit(([], [], None))

exit(self._standardize_tensors(
    x, y, sample_weight,
    run_eagerly=run_eagerly,
    dict_inputs=dict_inputs,
    is_dataset=is_dataset,
    class_weight=class_weight,
    batch_size=batch_size))
