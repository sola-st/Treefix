# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py
try:
    # Outer race condition: on program exit, the destruction context may be
    # deleted before this __del__ is called. At this point we can safely
    # exit without calling _destroy_resource() and let Python handle things.
    with self._destruction_context():
        # Inner race condition: possible between this and `ScopedTFFunction`
        # whereby if an entire garbage collection chain containing both
        # objects is moved to unreachable during the same garbage collection
        # cycle, the __del__ for `ScopedTFFunction` can be collected before
        # this method is called. In that case, we can't do much but
        # continue.
        self._destroy_resource()
except Exception:  # pylint: disable=broad-except
    # Silence all error logs that occur when attempting to destroy this
    # resource.
    pass
