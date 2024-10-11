# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
if not isinstance(trackable, tracking.Trackable):
    raise ValueError('%s is not a Trackable object.' % (trackable,))
self._trackable = trackable
self._distribute_strategy = distribution_strategy_context.get_strategy()

# TODO(b/141682913): Figure out why this is private and fix it.
saveables = trackable._gather_saveables_for_checkpoint().values()  # pylint: disable=protected-access
# 'Saveables' won't exist when we're passed a legacy TF1 table like
# a StaticHashTable.
if not saveables:
    self._num_tensors = 0
    self._setter = lambda weights: None
    self._getter = lambda: []

elif len(saveables) == 1:
    saveable = list(saveables)[0]

    if ops.executing_eagerly_outside_functions():
        # If we're in eager mode, we need to defer calling the Trackable's
        # saveable() callable until data export time.
        # However, it is safe to call the saveable as many times as we want, so
        # we will call it now to figure out how many tensors this Trackable will
        # produce.
        self._saveable = saveable
        self._num_tensors = len(self._saveable().specs)
        self._setter = lambda weights: self._saveable().restore(weights, None)
        self._getter = lambda: [spec.tensor for spec in self._saveable().specs]
    else:
        # If we're in Graph mode, we need to evaluate the Saveable only once and
        # cache the resulting restore graph. Failing to do this will result in
        # new assignment ops being added to the graph each time set_weights() is
        # called.
        self._placeholder_tensors = []
        self._saveable = saveable()
        self._num_tensors = len(self._saveable.specs)
        for spec in self._saveable.specs:
            tensor = spec.tensor
            self._placeholder_tensors.append(
                array_ops.placeholder(tensor.dtype, tensor.shape))
        self._assign_op = self._saveable.restore(self._placeholder_tensors,
                                                 None)
        self._setter = self._set_weights_v1
        self._getter = lambda: [spec.tensor for spec in self._saveable.specs]
else:
    raise ValueError('Only Trackables with one Saveable are supported. '
                     'The Trackable %s has %d Saveables.' %
                     (trackable, len(saveables)))
