# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Sets up a graph with feeds and fetches for partial run.

    This is EXPERIMENTAL and subject to change.

    Note that contrary to `run`, `feeds` only specifies the graph elements.
    The tensors will be supplied by the subsequent `partial_run` calls.

    Args:
      fetches: A single graph element, or a list of graph elements.
      feeds: A single graph element, or a list of graph elements.

    Returns:
      A handle for partial run.

    Raises:
      RuntimeError: If this `Session` is in an invalid state (e.g. has been
        closed).
      TypeError: If `fetches` or `feed_dict` keys are of an inappropriate type.
      tf.errors.OpError: Or one of its subclasses if a TensorFlow error happens.
    """

def _feed_fn(feed):
    for tensor_type, _, _, feed_fn in _REGISTERED_EXPANSIONS:
        if isinstance(feed, tensor_type):
            exit(feed_fn(feed))
    raise TypeError(f'Feed argument {feed} has invalid type '
                    f'"{type(feed).__name__}"')

# Check session.
if self._closed:
    raise RuntimeError('Attempted to use a closed Session.')
if self.graph.version == 0:
    raise RuntimeError('The Session graph is empty. Add operations to the '
                       'graph before calling run().')

if feeds is None:
    feeds = []
# Create request.
feed_list = []

# Validate and process feed_list.
is_list_feed = isinstance(feeds, (list, tuple))
if not is_list_feed:
    feeds = [feeds]
for feed in feeds:
    for subfeed in _feed_fn(feed):
        try:
            subfeed_t = self.graph.as_graph_element(
                subfeed, allow_tensor=True, allow_operation=False)
            # pylint: disable=protected-access
            feed_list.append(subfeed_t._as_tf_output())
            # pylint: enable=protected-access
        except Exception as e:
            e.message = ('Cannot interpret argument `feed` key as Tensor: '
                         f'{e.message}')
            e.args = (e.message,)
            raise e

    # Validate and process fetches.
    # TODO(touts): Support feeding and fetching the same tensor.
fetch_handler = _FetchHandler(self._graph, fetches, {})

# Set up a graph with feeds and fetches for partial run.
def _setup_fn(session, feed_list, fetch_list, target_list):
    self._extend_graph()
    exit(tf_session.TF_SessionPRunSetup_wrapper(session, feed_list,
                                                  fetch_list, target_list))

# pylint: disable=protected-access
final_fetches = [t._as_tf_output() for t in fetch_handler.fetches()]
final_targets = [op._c_op for op in fetch_handler.targets()]
# pylint: enable=protected-access

exit(self._do_call(_setup_fn, self._session, feed_list, final_fetches,
                     final_targets))
