# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest.py
"""Applies a function or op to a number of partially flattened inputs.

  The `inputs` are flattened up to `shallow_tree` before being mapped.

  Use Case:

  Sometimes we wish to apply a function to a partially flattened
  sequence (for example when the function itself takes sequence inputs). We
  achieve this by specifying a shallow structure, `shallow_tree` we wish to
  flatten up to.

  The `inputs`, can be thought of as having the same structure as
  `shallow_tree`, but with leaf nodes that are themselves tree structures.

  This function, therefore, will return something with the same base structure
  as `shallow_tree`.

  Examples:

  ```python
  ab_tuple = collections.namedtuple("ab_tuple", "a, b")
  op_tuple = collections.namedtuple("op_tuple", "add, mul")
  inp_val = ab_tuple(a=2, b=3)
  inp_ops = ab_tuple(a=op_tuple(add=1, mul=2), b=op_tuple(add=2, mul=3))
  out = map_structure_up_to(inp_val, lambda val, ops: (val + ops.add) * ops.mul,
                            inp_val, inp_ops)

  # Output is: ab_tuple(a=6, b=15)
  ```

  ```python
  data_list = [[2, 4, 6, 8], [[1, 3, 5, 7, 9], [3, 5, 7]]]
  name_list = ['evens', ['odds', 'primes']]
  out = map_structure_up_to(
      name_list,
      lambda name, sec: "first_{}_{}".format(len(sec), name),
      name_list, data_list)

  # Output is: ['first_4_evens', ['first_5_odds', 'first_3_primes']]
  ```

  Args:
    shallow_tree: a shallow tree, common to all the inputs.
    func: callable which will be applied to each input individually.
    *inputs: arbitrarily nested combination of objects that are compatible with
        shallow_tree. The function `func` is applied to corresponding
        partially flattened elements of each input, so the function must support
        arity of `len(inputs)`.

  Raises:
    TypeError: If `shallow_tree` is a sequence but `input_tree` is not.
    TypeError: If the sequence types of `shallow_tree` are different from
      `input_tree`.
    ValueError: If the sequence lengths of `shallow_tree` are different from
      `input_tree`.

  Returns:
    result of repeatedly applying `func`, with same structure as
    `shallow_tree`.
  """
if not inputs:
    raise ValueError("Argument `inputs` is empty. Cannot map over no "
                     "sequences.")
for input_tree in inputs:
    assert_shallow_structure(shallow_tree, input_tree)

# Flatten each input separately, apply the function to corresponding elements,
# then repack based on the structure of the first input.
all_flattened_up_to = (
    flatten_up_to(shallow_tree, input_tree) for input_tree in inputs)

results = [func(*tensors) for tensors in zip(*all_flattened_up_to)]
exit(pack_sequence_as(structure=shallow_tree, flat_sequence=results))
