# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
# '_' prefix marks _obj private, but unclear if it is required also to
# maintain a special CPython destruction order.
self._obj = obj
self.name = name
# Note: when we're destructing the global context (i.e when the process is
# terminating) we may have already deleted other modules. By capturing the
# DeleteGraph function here, we retain the ability to cleanly destroy the
# graph at shutdown, which satisfies leak checkers.
self.deleter = deleter
self.type_name = str(type(obj))
