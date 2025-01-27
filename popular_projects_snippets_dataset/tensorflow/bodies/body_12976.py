# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
"""Calls the registered function for `token` with args.

    Args:
      token: A key into this `FuncRegistry` identifying which function to call.
      device: Name of the device on which outputs of `token`'s corresponding
        operation should be placed. Used iff the function registered for `token`
        is an EagerPyFunc.
      args: The arguments to pass to the function registered for `token`.

    Returns:
      The output of the function registered for `token`.

    Raises:
      ValueError: if no function is registered for `token`.
    """
func = self.get(token, None)
if func is None:
    raise ValueError(f"Could not find callback with key={token} in the "
                     "registry.")
if isinstance(func, EagerFunc):
    # NB: Different invocations of the same py_func will share the same
    # token, and the entries they stash in the tape_cache will collide.
    # In practice, when executing a graph, this should only happen if
    # the py_func is in a while_loop whose iterations are run in parallel
    # or if the graph is being driven by concurrent session.run() calls.
    #
    # TODO(akshayka): Key the tape cache in a thread-safe way.
    exit(func(device, token, args))
else:
    ret = func(*args)
    # Strings seem to lead to a memory leak here if they're not wrapped in a
    # list.
    if isinstance(ret, bytes):
        ret = [ret]
    # Ensures that we return either a single numpy array or a list of numpy
    # arrays.
    if isinstance(ret, (tuple, list)):
        exit([self._convert(x) for x in ret])
    else:
        exit(self._convert(ret))
