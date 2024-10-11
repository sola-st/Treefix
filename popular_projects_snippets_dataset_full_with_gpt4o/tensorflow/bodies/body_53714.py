# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Decorator for asserting that no new Python objects persist after a test.

  Runs the test multiple times executing eagerly, first as a warmup and then to
  let objects accumulate. The warmup helps ignore caches which do not grow as
  the test is run repeatedly.

  Useful for checking that there are no missing Py_DECREFs in the C exercised by
  a bit of Python.

  Args:
    func: The function to test.
    warmup_iters: The numer of warmup iterations, excluded from measuring.

  Returns:
    The wrapped function performing the test.
  """

def wrap_f(f):
    def decorator(self, *args, **kwargs):
        """Warms up, gets object counts, runs the test, checks for new objects."""
        with context.eager_mode():
            gc.disable()
            # Python 3.11 removed "errors" and "skipped" as members of
            # unittest.case._Outcome so get them from the test result object
            # instead.
            test_errors = None
            test_skipped = None
            if hasattr(self._outcome, "errors"):
                test_errors = self._outcome.errors
                test_skipped = self._outcome.skipped
            else:
                test_errors = self._outcome.result.errors
                test_skipped = self._outcome.result.skipped
            # Run the test 2 times as warmup, in an attempt to fill up caches, which
            # should not grow as the test is run repeatedly below.
            #
            # TODO(b/117156879): Running warmup twice is black magic; we have seen
            # tests that fail with 1 warmup run, and pass with 2, on various
            # versions of python2.7.x.
            for _ in range(warmup_iters):
                f(self, *args, **kwargs)
            # Since we aren't in the normal test lifecycle, we need to manually run
            # cleanups to clear out their object references.
            self.doCleanups()

            # Some objects are newly created by _get_object_count_by_type().  So
            # create and save as a dummy variable to include it as a baseline.
            obj_count_by_type = _get_object_count_by_type()
            gc.collect()

            # Make sure any registered functions are cleaned up in the C++ runtime.
            registered_function_names = context.context().list_function_names()

            # unittest.doCleanups adds to self._outcome with each unwound call.
            # These objects are retained across gc collections so we exclude them
            # from the object count calculation.
            obj_count_by_type = _get_object_count_by_type(
                exclude=gc.get_referents(test_errors, test_skipped))

            if ops.has_default_graph():
                collection_sizes_before = {
                    collection: len(ops.get_collection(collection))
                    for collection in ops.get_default_graph().collections
                }
            for _ in range(3):
                f(self, *args, **kwargs)
            # Since we aren't in the normal test lifecycle, we need to manually run
            # cleanups to clear out their object references.
            self.doCleanups()
            # Note that gc.get_objects misses anything that isn't subject to garbage
            # collection (C types). Collections are a common source of leaks, so we
            # test for collection sizes explicitly.
            if ops.has_default_graph():
                for collection_key in ops.get_default_graph().collections:
                    collection = ops.get_collection(collection_key)
                    size_before = collection_sizes_before.get(collection_key, 0)
                    if len(collection) > size_before:
                        raise AssertionError(
                            ("Collection %s increased in size from "
                             "%d to %d (current items %s).") %
                            (collection_key, size_before, len(collection), collection))
                    # Make sure our collection checks don't show up as leaked memory by
                    # removing references to temporary variables.
                    del collection
                    del collection_key
                    del size_before
                del collection_sizes_before
            gc.collect()

            # There should be no new Python objects hanging around.
            obj_count_by_type = (
                _get_object_count_by_type(
                    exclude=gc.get_referents(test_errors, test_skipped)) -
                obj_count_by_type)

            # There should be no newly registered functions hanging around.
            leftover_functions = (
                context.context().list_function_names() - registered_function_names)
            assert not leftover_functions, (
                "The following functions were newly created: %s" %
                leftover_functions)

            # In some cases (specifically on MacOS), new_count is somehow
            # smaller than previous_count.
            # Using plain assert because not all classes using this decorator
            # have assertLessEqual
            assert not obj_count_by_type, (
                "The following objects were newly created: %s" %
                str(obj_count_by_type))
            gc.enable()
    exit(decorator)

if func is None:
    exit(wrap_f)
else:
    exit(wrap_f(func))
