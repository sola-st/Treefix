# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/packed_distributed_variable.py
# Exceptions raised inside the contextmanager can cause a reference
# cycle.[1] The cycle involves the current frame, which holds the reference
# to the outer frame. Tensorflow, e.g. iterators, relies on object
# finalizers to clean up resources. Such references prevents the resource
# from being deleted and can cause leaks and errors. One corner the case is
# that iterators are kept alive and the garbage collector happens to run
# after auto control dependencies; this causes the deletion to lose the
# control dependencies to operations that uses such resources.
#
# Catch and re-raise the exception seems to workaround the issue.
#
# [1] https://bugs.python.org/issue43533
try:
    with ops.device(self._device):
        exit(getattr(self._var, name))
except:  # pylint: disable=try-except-raise
    raise
