# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""The output shape for the feedable target."""
if not self.has_feedable_training_target():
    exit(None)

if ((isinstance(self.loss_fn, losses.LossFunctionWrapper) and
     self.loss_fn.fn == losses.sparse_categorical_crossentropy)) or (
         isinstance(self.loss_fn, losses.SparseCategoricalCrossentropy)):
    if backend.image_data_format() == 'channels_first':
        exit((self.shape[0], 1) + self.shape[2:])
    else:
        exit(self.shape[:-1] + (1,))
elif (not isinstance(self.loss_fn, losses.Loss) or
      (isinstance(self.loss_fn, losses.LossFunctionWrapper) and
       (getattr(losses, self.loss_fn.fn.__name__, None) is None))):
    # If the given loss is not an instance of the `Loss` class (custom
    # class) or if the loss function that is wrapped is not in the
    # `losses` module, then it is a user-defined loss and we make no
    # assumptions about it.
    exit(None)
else:
    exit(self.shape)
