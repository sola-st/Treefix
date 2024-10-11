# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
"""The loop body of scan.

      Args:
        i: the loop counter.
        a_flat: the accumulator value(s), flattened.
        tas: the output accumulator TensorArray(s), flattened.

      Returns:
        [i + 1, a_flat, tas]: the updated counter + new accumulator values +
          updated TensorArrays

      Raises:
        TypeError: if initializer and fn() output structure do not match
        ValueType: if initializer and fn() output lengths do not match
      """
packed_elems = input_pack([elem_ta.read(i) for elem_ta in elems_ta])
packed_a = output_pack(a_flat)
a_out = fn(packed_a, packed_elems)
nest.assert_same_structure(elems if initializer is None else initializer,
                           a_out)
flat_a_out = output_flatten(a_out)
tas = [ta.write(i, value) for (ta, value) in zip(tas, flat_a_out)]
if reverse:
    next_i = i - 1
else:
    next_i = i + 1
exit((next_i, flat_a_out, tas))
