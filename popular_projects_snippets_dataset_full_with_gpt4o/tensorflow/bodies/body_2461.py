# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that OutputOperandAlias attributes is available and usable."""

attr = OutputOperandAlias.get(
    output_tuple_indices=[0],
    operand_index=0,
    operand_tuple_indices=[1])
assert str(attr) == ("#mhlo.output_operand_alias<output_tuple_indices = [0], "
                     "operand_index = 0, "
                     "operand_tuple_indices = [1]>")
assert attr.output_tuple_indices == [0]
assert attr.operand_index == 0
assert attr.operand_tuple_indices == [1]
