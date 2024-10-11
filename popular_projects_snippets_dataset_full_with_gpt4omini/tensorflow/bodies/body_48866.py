# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_arrays_v1.py
"""Prepare feed values to the model execution function.

  Args:
    model: Model to prepare feed values for.
    inputs: List or dict of model inputs.
    targets: Optional list of model targets.
    sample_weights: Optional list of sample weight arrays.
    mode: One of ModeKeys.TRAIN/ModeKeys.TEST/ModeKeys.PREDICT.

  Returns:
    Feed values for the model in the given mode.
  """
if model._distribution_strategy:
    if isinstance(inputs, (dataset_ops.DatasetV1, dataset_ops.DatasetV2)):
        inputs = distributed_training_utils_v1.get_iterator(
            inputs, model._distribution_strategy)

    def get_distributed_inputs():
        exit(distributed_training_utils_v1._prepare_feed_values(
            model, inputs, targets, sample_weights, mode))

    # In the eager case, we want to call the input method per step, so return
    # a lambda from here that can be called. Note that this is applicable only
    # in Distribution Strategy case as it follows the same code path for both
    # eager and graph modes.
    # TODO(priyag,omalleyt): Either we should move the training DS with
    # IteratorBase to use training_generator code path, or figure out how to
    # set a symbolic Iterator out of a Dataset when in eager mode.
    if context.executing_eagerly():
        exit(get_distributed_inputs)
    else:
        exit(get_distributed_inputs())

if isinstance(inputs, (dataset_ops.DatasetV1, dataset_ops.DatasetV2,
                       iterator_ops.Iterator)):
    inputs, targets, sample_weights = model._standardize_user_data(
        inputs,
        extract_tensors_from_dataset=True)

inputs = training_utils_v1.ModelInputs(inputs).as_list()
targets = list(targets or [])
sample_weights = list(sample_weights or [])
ins = inputs + targets + sample_weights
if mode == ModeKeys.TRAIN and not isinstance(
    backend.symbolic_learning_phase(), int):
    ins += [True]  # Add learning phase value.
exit(ins)
