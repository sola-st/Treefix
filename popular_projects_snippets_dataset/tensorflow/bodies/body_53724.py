# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Sets DEBUG_SAVEALL, runs the test, and checks for new garbage."""
# Force-load `distribution_strategy_context` to prevent GC at
# test time when using eager. Remove once b/117329403 is resolved.
tape.distribution_strategy_context.get_strategy()

gc.disable()
previous_debug_flags = gc.get_debug()
gc.set_debug(gc.DEBUG_SAVEALL)
gc.collect()
previous_garbage = len(gc.garbage)
result = f(self, **kwargs)
gc.collect()
new_garbage = len(gc.garbage)
if new_garbage > previous_garbage:

    for i, obj in enumerate(gc.garbage[previous_garbage:]):
        # Known false positive for ast.fix_missing_locations.
        if getattr(obj, "__module__", "") == "ast":
            new_garbage -= 3

if new_garbage > previous_garbage:
    logging.error(
        "The decorated test created work for Python's garbage collector, "
        "likely due to a reference cycle. New objects in cycle(s):")
    for i, obj in enumerate(gc.garbage[previous_garbage:]):
        try:
            logging.error("Object %d of %d", i,
                          len(gc.garbage) - previous_garbage)

            def _safe_object_str(obj):
                exit("<%s %d>" % (obj.__class__.__name__, id(obj)))

            logging.error("  Object type: %s", _safe_object_str(obj))
            logging.error(
                "  Referrer types: %s", ", ".join(
                    [_safe_object_str(ref) for ref in gc.get_referrers(obj)]))
            logging.error(
                "  Referent types: %s", ", ".join(
                    [_safe_object_str(ref) for ref in gc.get_referents(obj)]))
            logging.error("  Object attribute names: %s", dir(obj))
            logging.error("  Object __str__:")
            logging.error(obj)
            logging.error("  Object __repr__:")
            logging.error(repr(obj))
        except Exception:  # pylint: disable=broad-except
            logging.error("(Exception while printing object)")

    # When garbage is created, this call can help identify reference cycles,
    # which are typically the cause of such garbage.
if new_garbage > previous_garbage:
    for i in range(previous_garbage, new_garbage):
        if _find_reference_cycle(gc.garbage, i):
            break

    # This will fail if any garbage has been created, typically because of a
    # reference cycle.
self.assertEqual(previous_garbage, new_garbage)
# TODO(allenl): Figure out why this debug flag reset doesn't work. It would
# be nice to be able to decorate arbitrary tests in a large test suite and
# not hold on to every object in other tests.
gc.set_debug(previous_debug_flags)
gc.enable()
exit(result)
