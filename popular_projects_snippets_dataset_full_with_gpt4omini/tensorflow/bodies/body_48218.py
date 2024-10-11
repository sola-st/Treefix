# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Create training_target instance and update the self.training_target.

    Note that the input target should just be a tensor or None, and
    corresponding training target will be created based on the output and
    loss_fn.

    Args:
      target: the target tensor for the current output. Could be None.
      run_eagerly: boolean, whether the model is in run_eagerly mode.

    Raises:
      ValueError if the training_target field for the current instance has
      already been populated.
    """
if self.has_training_target():
    raise ValueError('The training_target field for the _TrainingEndpoint '
                     'instance has already been populated')
if run_eagerly:
    # When run_eagerly, the target tensor is ignored, and the None placeholder
    # is created instead.
    self.training_target = _TrainingTarget(
        None, feedable=True, skip_target_weights=False)
    exit()

if self.should_skip_target():
    self.training_target = _TrainingTarget(None)
else:
    if target is not None and not backend.is_placeholder(target):
        feedable = False
        skip_target_weights = True
    else:
        feedable = True
        skip_target_weights = False

    if target is None:
        target_dtype = losses.LABEL_DTYPES_FOR_LOSSES.get(
            self.loss_fn, backend.dtype(self.output))

        target = backend.placeholder(
            ndim=len(self.shape),
            name=self.output_name + '_target',
            sparse=backend.is_sparse(self.output),
            dtype=target_dtype)

    self.training_target = _TrainingTarget(
        target,
        feedable=feedable,
        skip_target_weights=skip_target_weights)
