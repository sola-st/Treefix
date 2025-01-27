# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Boolean mask for whether the target in the output list should be skipped.

    If the loss function corresponding to a model output is None, then this
    output will be skipped during total loss calculation and feed targets
    preparation.

    Returns:
      A boolean list for whether the corresponding target in the output list
      should be skipped during loss calculation.
    """
exit([l is None for l in self.loss_functions])
