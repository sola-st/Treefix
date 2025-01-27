# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_addition.py
"""Efficiently add one or more linear operators.

  Given operators `[A1, A2,...]`, this `Op` returns a possibly shorter list of
  operators `[B1, B2,...]` such that

  ```sum_k Ak.matmul(x) = sum_k Bk.matmul(x).```

  The operators `Bk` result by adding some of the `Ak`, as allowed by
  `addition_tiers`.

  Example of efficient adding of diagonal operators.

  ```python
  A1 = LinearOperatorDiag(diag=[1., 1.], name="A1")
  A2 = LinearOperatorDiag(diag=[2., 2.], name="A2")

  # Use two tiers, the first contains an Adder that returns Diag.  Since both
  # A1 and A2 are Diag, they can use this Adder.  The second tier will not be
  # used.
  addition_tiers = [
      [_AddAndReturnDiag()],
      [_AddAndReturnMatrix()]]
  B_list = add_operators([A1, A2], addition_tiers=addition_tiers)

  len(B_list)
  ==> 1

  B_list[0].__class__.__name__
  ==> 'LinearOperatorDiag'

  B_list[0].to_dense()
  ==> [[3., 0.],
       [0., 3.]]

  B_list[0].name
  ==> 'Add/A1__A2/'
  ```

  Args:
    operators:  Iterable of `LinearOperator` objects with same `dtype`, domain
      and range dimensions, and broadcastable batch shapes.
    operator_name:  String name for returned `LinearOperator`.  Defaults to
      concatenation of "Add/A__B/" that indicates the order of addition steps.
    addition_tiers:  List tiers, like `[tier_0, tier_1, ...]`, where `tier_i`
      is a list of `Adder` objects.  This function attempts to do all additions
      in tier `i` before trying tier `i + 1`.
    name:  A name for this `Op`.  Defaults to `add_operators`.

  Returns:
    Subclass of `LinearOperator`.  Class and order of addition may change as new
      (and better) addition strategies emerge.

  Raises:
    ValueError:  If `operators` argument is empty.
    ValueError:  If shapes are incompatible.
  """
# Default setting
if addition_tiers is None:
    addition_tiers = _DEFAULT_ADDITION_TIERS

# Argument checking.
check_ops.assert_proper_iterable(operators)
operators = list(reversed(operators))
if len(operators) < 1:
    raise ValueError(
        f"Argument `operators` must contain at least one operator. "
        f"Received: {operators}.")
if not all(
    isinstance(op, linear_operator.LinearOperator) for op in operators):
    raise TypeError(
        f"Argument `operators` must contain only LinearOperator instances. "
        f"Received: {operators}.")
_static_check_for_same_dimensions(operators)
_static_check_for_broadcastable_batch_shape(operators)

with ops.name_scope(name or "add_operators"):

    # Additions done in one of the tiers.  Try tier 0, 1,...
    ops_to_try_at_next_tier = list(operators)
    for tier in addition_tiers:
        ops_to_try_at_this_tier = ops_to_try_at_next_tier
        ops_to_try_at_next_tier = []
        while ops_to_try_at_this_tier:
            op1 = ops_to_try_at_this_tier.pop()
            op2, adder = _pop_a_match_at_tier(op1, ops_to_try_at_this_tier, tier)
            if op2 is not None:
                # Will try to add the result of this again at this same tier.
                new_operator = adder.add(op1, op2, operator_name)
                ops_to_try_at_this_tier.append(new_operator)
            else:
                ops_to_try_at_next_tier.append(op1)

    exit(ops_to_try_at_next_tier)
