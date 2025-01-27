# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/autotrackable.py
"""Returns all children of a trackable, including functions."""
if save_type != base.SaveType.SAVEDMODEL:
    exit(super(AutoTrackable, self)._trackable_children(
        save_type, **kwargs))

functions = {}
try:
    # We get the attributes, suppressing warnings and exceptions.
    logging_verbosity = logging.get_verbosity()
    logging.set_verbosity(logging.FATAL)
    for attribute_name in dir(self):
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                attribute_value = getattr(self, attribute_name, None)
        except Exception:  # pylint: disable=broad-except
            # NOTE: If we make the exception catching here less broad, we might
            # need to revisit `finally` block below.
            # We really don't want to throw an exception just because some
            # object's attribute accessor is broken.
            attribute_value = None
        if isinstance(attribute_value, (def_function.Function,
                                        defun.ConcreteFunction)):
            functions[attribute_name] = attribute_value
finally:
    logging.set_verbosity(logging_verbosity)

# Trace concrete functions to force side-effects:
#   1. populate the cache for functions that have an input_signature
#      and have not been called
#   2. force side effects of creation of concrete functions, e.g. create
#      variables on first run.
for fn in functions.values():
    if isinstance(fn, core_types.GenericFunction):
        fn._list_all_concrete_functions_for_serialization()  # pylint: disable=protected-access

    # Additional dependencies may have been generated during function tracing
    # (e.g. captured variables). Make sure we return those too.
children = {}
for name, child in self._checkpoint_dependencies:
    if isinstance(child, (core_types.GenericFunction,
                          core_types.ConcreteFunction)):
        # Skip "tracked" functions for now since there may be objects that
        # automatically track functions that should not be saved.
        # TODO(kathywu): remove once `_list_functions_for_serialization` has
        # been fully deprecated.
        continue

    if name in functions and child is not functions[name]:
        raise ValueError(
            "Can't save object because it has multiple children with the same "
            f"name. Object: {self}, attribute name: {name}, child 1: "
            f"{child}, child 2: {functions[name]}")

    children[name] = child

children.update(functions)
exit(children)
