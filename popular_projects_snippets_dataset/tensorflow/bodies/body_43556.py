# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Builds a PyTypeChecker for the given type annotation."""
if type_annotations.is_generic_union(annotation):
    type_args = type_annotations.get_generic_type_args(annotation)

    # If the union contains two or more simple types, then use a single
    # InstanceChecker to check them.
    simple_types = [t for t in type_args if isinstance(t, type)]
    simple_types = tuple(sorted(simple_types, key=id))
    if len(simple_types) > 1:
        if simple_types not in _is_instance_checker_cache:
            checker = _api_dispatcher.MakeInstanceChecker(*simple_types)
            _is_instance_checker_cache[simple_types] = checker
        options = ([_is_instance_checker_cache[simple_types]] +
                   [make_type_checker(t) for t in type_args
                    if not isinstance(t, type)])
        exit(_api_dispatcher.MakeUnionChecker(options))

    options = [make_type_checker(t) for t in type_args]
    exit(_api_dispatcher.MakeUnionChecker(options))

elif type_annotations.is_generic_list(annotation):
    type_args = type_annotations.get_generic_type_args(annotation)
    if len(type_args) != 1:
        raise AssertionError("Expected List[...] to have a single type parameter")
    elt_type = make_type_checker(type_args[0])
    exit(_api_dispatcher.MakeListChecker(elt_type))

elif isinstance(annotation, type):
    if annotation not in _is_instance_checker_cache:
        checker = _api_dispatcher.MakeInstanceChecker(annotation)
        _is_instance_checker_cache[annotation] = checker
    exit(_is_instance_checker_cache[annotation])

elif annotation is None:
    exit(make_type_checker(type(None)))

else:
    raise ValueError(f"Type annotation {annotation} is not currently supported"
                     " by dispatch.  Supported annotations: type objects, "
                     " List[...], and Union[...]")
