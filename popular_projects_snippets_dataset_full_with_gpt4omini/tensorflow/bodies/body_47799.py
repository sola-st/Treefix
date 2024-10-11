# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
"""Create a RNN cell composed sequentially of a number of RNNCells.

    Args:
      cells: list of RNNCells that will be composed in this order.
      state_is_tuple: If True, accepted and returned states are n-tuples, where
        `n = len(cells)`.  If False, the states are all concatenated along the
        column axis.  This latter behavior will soon be deprecated.

    Raises:
      ValueError: if cells is empty (not allowed), or at least one of the cells
        returns a state tuple but the flag `state_is_tuple` is `False`.
    """
logging.warning("`tf.nn.rnn_cell.MultiRNNCell` is deprecated. This class "
                "is equivalent as `tf.keras.layers.StackedRNNCells`, "
                "and will be replaced by that in Tensorflow 2.0.")
super(MultiRNNCell, self).__init__()
if not cells:
    raise ValueError("Must specify at least one cell for MultiRNNCell.")
if not nest.is_nested(cells):
    raise TypeError("cells must be a list or tuple, but saw: %s." % cells)

if len(set(id(cell) for cell in cells)) < len(cells):
    logging.log_first_n(
        logging.WARN, "At least two cells provided to MultiRNNCell "
        "are the same object and will share weights.", 1)

self._cells = cells
for cell_number, cell in enumerate(self._cells):
    # Add Trackable dependencies on these cells so their variables get
    # saved with this object when using object-based saving.
    if isinstance(cell, trackable.Trackable):
        # TODO(allenl): Track down non-Trackable callers.
        self._track_trackable(cell, name="cell-%d" % (cell_number,))
self._state_is_tuple = state_is_tuple
if not state_is_tuple:
    if any(nest.is_nested(c.state_size) for c in self._cells):
        raise ValueError("Some cells return tuples of states, but the flag "
                         "state_is_tuple is not set.  State sizes are: %s" %
                         str([c.state_size for c in self._cells]))
