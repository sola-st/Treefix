# Extracted from ./data/repos/tensorflow/tensorflow/python/util/nest.py
"""Asserts that `shallow_tree` is a shallow structure of `input_tree`.

  That is, this function tests if the `input_tree` structure can be created from
  the `shallow_tree` structure by replacing its leaf nodes with deeper
  tree structures.

  Examples:

  The following code will raise an exception:
  ```python
    shallow_tree = {"a": "A", "b": "B"}
    input_tree = {"a": 1, "c": 2}
    assert_shallow_structure(shallow_tree, input_tree)
  ```

  The following code will raise an exception:
  ```python
    shallow_tree = ["a", "b"]
    input_tree = ["c", ["d", "e"], "f"]
    assert_shallow_structure(shallow_tree, input_tree)
  ```

  Args:
    shallow_tree: an arbitrarily nested structure.
    input_tree: an arbitrarily nested structure.
    check_types: if `True` (default) the sequence types of `shallow_tree` and
      `input_tree` have to be the same. Note that even with check_types==True,
      this function will consider two different namedtuple classes with the same
      name and _fields attribute to be the same class.
    expand_composites: If true, then composite tensors such as
      `tf.sparse.SparseTensor` and `tf.RaggedTensor` are expanded into their
      component tensors.
  Raises:
    TypeError: If `shallow_tree` is a sequence but `input_tree` is not.
    TypeError: If the sequence types of `shallow_tree` are different from
      `input_tree`. Only raised if `check_types` is `True`.
    ValueError: If the sequence lengths of `shallow_tree` are different from
      `input_tree`.
  """
is_nested_fn = _is_nested_or_composite if expand_composites else _is_nested
if is_nested_fn(shallow_tree):
    if not is_nested_fn(input_tree):
        raise TypeError(
            "If shallow structure is a sequence, input must also be a sequence. "
            "Input has type: %s." % type(input_tree))

    if isinstance(shallow_tree, _wrapt.ObjectProxy):
        shallow_type = type(shallow_tree.__wrapped__)
    else:
        shallow_type = type(shallow_tree)

    if check_types and not isinstance(input_tree, shallow_type):
        # Duck-typing means that nest should be fine with two different
        # namedtuples with identical name and fields.
        shallow_is_namedtuple = is_namedtuple(shallow_tree, False)
        input_is_namedtuple = is_namedtuple(input_tree, False)
        if shallow_is_namedtuple and input_is_namedtuple:
            if not same_namedtuples(shallow_tree, input_tree):
                raise TypeError(_STRUCTURES_HAVE_MISMATCHING_TYPES.format(
                    input_type=type(input_tree),
                    shallow_type=type(shallow_tree)))

        elif isinstance(shallow_tree, list) and isinstance(input_tree, list):
            # List subclasses are considered the same,
            # e.g. python list vs. _ListWrapper.
            pass

        elif ((_is_composite_tensor(shallow_tree) or
               _is_type_spec(shallow_tree)) and
              (_is_composite_tensor(input_tree) or _is_type_spec(input_tree))):
            pass  # Compatibility will be checked below.

        elif not (isinstance(shallow_tree, _collections_abc.Mapping) and
                  isinstance(input_tree, _collections_abc.Mapping)):
            raise TypeError(_STRUCTURES_HAVE_MISMATCHING_TYPES.format(
                input_type=type(input_tree),
                shallow_type=type(shallow_tree)))

    if _is_composite_tensor(shallow_tree) or _is_composite_tensor(input_tree):
        if not (
            (_is_composite_tensor(input_tree) or _is_type_spec(input_tree)) and
            (_is_composite_tensor(shallow_tree) or _is_type_spec(shallow_tree))):
            raise TypeError(_STRUCTURES_HAVE_MISMATCHING_TYPES.format(
                input_type=type(input_tree),
                shallow_type=type(shallow_tree)))
        # pylint: disable=protected-access
        type_spec_1 = (shallow_tree if _is_type_spec(shallow_tree) else
                       shallow_tree._type_spec)._without_tensor_names()
        type_spec_2 = (input_tree if _is_type_spec(input_tree) else
                       input_tree._type_spec)._without_tensor_names()
        # TODO(b/246356867): Replace the most_specific_common_supertype below
        # with get_structure.
        if hasattr(type_spec_1, "_get_structure") and hasattr(type_spec_2,
                                                              "_get_structure"):
            result = (type_spec_1._get_structure() == type_spec_2._get_structure()
                      or None)
        else:
            result = type_spec_1.most_specific_common_supertype([type_spec_2])
        if result is None:
            raise ValueError("Incompatible CompositeTensor TypeSpecs: %s vs. %s" %
                             (type_spec_1, type_spec_2))
        # pylint: enable=protected-access

    elif _is_type_spec(shallow_tree):
        if not _is_type_spec(input_tree):
            raise TypeError("If shallow structure is a TypeSpec, input must also "
                            "be a TypeSpec.  Input has type: %s."
                            % type(input_tree))
    else:
        if len(input_tree) != len(shallow_tree):
            raise ValueError(
                _STRUCTURES_HAVE_MISMATCHING_LENGTHS.format(
                    input_length=len(input_tree), shallow_length=len(shallow_tree)))
        elif len(input_tree) < len(shallow_tree):
            raise ValueError(
                _INPUT_TREE_SMALLER_THAN_SHALLOW_TREE.format(
                    input_size=len(input_tree), shallow_size=len(shallow_tree)))

    if isinstance(shallow_tree, _collections_abc.Mapping):
        absent_keys = set(shallow_tree) - set(input_tree)
        if absent_keys:
            raise ValueError(_SHALLOW_TREE_HAS_INVALID_KEYS
                             .format(sorted(absent_keys)))

    for shallow_branch, input_branch in zip(_yield_value(shallow_tree),
                                            _yield_value(input_tree)):
        assert_shallow_structure(shallow_branch, input_branch,
                                 check_types=check_types,
                                 expand_composites=expand_composites)
