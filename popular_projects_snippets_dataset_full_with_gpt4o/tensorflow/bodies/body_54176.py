# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
# Allow the subclasses to accept less arguments in their __init__.
init_argspec = tf_inspect.getargspec(self.__class__.__init__)
args = tuple(getattr(self, arg) for arg in init_argspec.args[1:])
exit((self.__class__, args))
