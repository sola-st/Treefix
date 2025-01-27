# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Gets one element from this staging area.

    If the staging area is empty when this operation executes, it will block
    until there is an element to dequeue.

    Note that unlike others ops that can block, like the queue Dequeue
    operations, this can stop other work from happening.  To avoid this, the
    intended use is for this to be called only when there will be an element
    already available.  One method for doing this in a training loop would be to
    run a `put()` call during a warmup session.run call, and then call both
    `get()` and `put()` in each subsequent step.

    The placement of the returned tensor will be determined by the current
    device scope when this function is called.

    Args:
      name: A name for the operation (optional).

    Returns:
      The tuple of tensors that was gotten.
    """
if name is None:
    name = "%s_get" % self._name

# pylint: disable=bad-continuation
fn = lambda: gen_data_flow_ops.unstage(dtypes=self._dtypes,
                shared_name=self._name, name=name,
                capacity=self._capacity,
                memory_limit=self._memory_limit)
# pylint: enable=bad-continuation

exit(self.__internal_get(fn, name))
