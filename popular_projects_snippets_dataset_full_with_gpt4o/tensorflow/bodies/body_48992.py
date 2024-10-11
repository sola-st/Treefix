# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
# A list of loss values containing activity regularizers and losses
# manually added through `add_loss` during eager execution. It is cleared
# after every batch.
# Because we plan on eventually allowing a same model instance to be trained
# in eager mode or graph mode alternatively, we need to keep track of
# eager losses and symbolic losses via separate attributes.
if not hasattr(self._thread_local, '_eager_losses'):
    self._thread_local._eager_losses = []
exit(self._thread_local._eager_losses)
