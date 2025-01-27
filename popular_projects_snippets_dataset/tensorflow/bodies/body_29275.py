# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest.py
"""Asserts that `shallow_tree` is a shallow structure of `input_tree`.

  That is, this function tests if the `input_tree` structure can be created from
  the `shallow_tree` structure by replacing its leaf nodes with deeper
  tree structures.

  Examples:

  The following code will raise an exception:
  ```python
    shallow_tree = ["a", "b"]
    input_tree = ["c", ["d", "e"], "f"]
    assert_shallow_structure(shallow_tree, input_tree)
  ```

  The following code will not raise an exception:
  ```python
    shallow_tree = ["a", "b"]
    input_tree = ["c", ["d", "e"]]
    assert_shallow_structure(shallow_tree, input_tree)
  ```

  Args:
    shallow_tree: an arbitrarily nested structure.
    input_tree: an arbitrarily nested structure.
    check_types: if `True` (default) the sequence types of `shallow_tree` and
      `input_tree` have to be the same.

  Raises:
    TypeError: If `shallow_tree` is a sequence but `input_tree` is not.
    TypeError: If the sequence types of `shallow_tree` are different from
      `input_tree`. Only raised if `check_types` is `True`.
    ValueError: If the sequence lengths of `shallow_tree` are different from
      `input_tree`.
  """
if is_nested(shallow_tree):
    if not is_nested(input_tree):
        raise TypeError(
            "If shallow structure is a sequence, input must also be a sequence. "
            f"Input has type: '{type(input_tree).__name__}'.")

    if check_types and not isinstance(input_tree, type(shallow_tree)):
        raise TypeError(
            "The two structures don't have the same sequence type. Input "
            f"structure has type '{type(input_tree).__name__}', while shallow "
            f"structure has type '{type(shallow_tree).__name__}'.")

    if len(input_tree) != len(shallow_tree):
        raise ValueError(
            "The two structures don't have the same sequence length. Input "
            f"structure has length {len(input_tree)}, while shallow structure "
            f"has length {len(shallow_tree)}.")

    if check_types and isinstance(shallow_tree, _collections_abc.Mapping):
        if set(input_tree) != set(shallow_tree):
            raise ValueError(
                "The two structures don't have the same keys. Input "
                f"structure has keys {list(input_tree)}, while shallow structure "
                f"has keys {list(shallow_tree)}.")
        input_tree = sorted(input_tree.items())
        shallow_tree = sorted(shallow_tree.items())

    for shallow_branch, input_branch in zip(shallow_tree, input_tree):
        assert_shallow_structure(shallow_branch, input_branch,
                                 check_types=check_types)
