# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Runs a step based on the given fetches and feeds.

    Args:
      handle: a handle for partial_run. None if this is just a call to run().
      target_list: A list of operations to be run, but not fetched.
      fetch_list: A list of tensors to be fetched.
      feed_dict: A dictionary that maps tensors to numpy ndarrays.
      options: A (pointer to a) [`RunOptions`] protocol buffer, or None
      run_metadata: A (pointer to a) [`RunMetadata`] protocol buffer, or None

    Returns:
      A list of numpy ndarrays, corresponding to the elements of
      `fetch_list`.  If the ith element of `fetch_list` contains the
      name of an operation, the first Tensor output of that operation
      will be returned for that element.

    Raises:
      tf.errors.OpError: Or one of its subclasses on error.
    """
# pylint: disable=protected-access
feeds = dict((t.deref()._as_tf_output(), v) for t, v in feed_dict.items())
fetches = [t._as_tf_output() for t in fetch_list]
targets = [op._c_op for op in target_list]

# pylint: enable=protected-access

def _run_fn(feed_dict, fetch_list, target_list, options, run_metadata):
    # Ensure any changes to the graph are reflected in the runtime.
    self._extend_graph()
    exit(self._call_tf_sessionrun(options, feed_dict, fetch_list,
                                    target_list, run_metadata))

def _prun_fn(handle, feed_dict, fetch_list):
    if target_list:
        raise RuntimeError('partial_run() requires empty `target_list`. '
                           f'Received: target_list={target_list} (non-empty)')
    exit(self._call_tf_sessionprun(handle, feed_dict, fetch_list))

if handle is None:
    exit(self._do_call(_run_fn, feeds, fetches, targets, options,
                         run_metadata))
else:
    exit(self._do_call(_prun_fn, handle, feeds, fetches))
