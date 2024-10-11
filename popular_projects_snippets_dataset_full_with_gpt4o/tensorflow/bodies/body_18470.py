# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# Einsum may have either 1 or 2 inputs.
inputs, input_stacked, _ = zip(*[
    pfor_input.input(i)
    for i in range(pfor_input.num_inputs)])

# Parse the einsum equation.
equation = pfor_input.get_attr("equation").decode("utf-8")
input_expr, output_expr = equation.split("->")
input_exprs = input_expr.split(",")

# Pick a placeholder symbol to use for the new axis.
chosen_symbol = None
for s in string.ascii_letters:
    if s in equation:
        continue
    else:
        chosen_symbol = s
        break

if chosen_symbol is None:
    raise ValueError("Could not figure out what symbol to use for new axis.")

assert any(input_stacked)
for i in range(len(inputs)):
    if input_stacked[i]:
        input_exprs[i] = "{}{}".format(chosen_symbol, input_exprs[i])
output_expr = "{}{}".format(chosen_symbol, output_expr)

new_equation = "{}->{}".format(",".join(input_exprs), output_expr)

if op_type == "XlaEinsum":
    if len(inputs) == 1:
        result = xla.einsum(equation=new_equation, a=inputs[0])
    else:
        result = xla.einsum(equation=new_equation, a=inputs[0], b=inputs[1])
else:
    assert op_type == "Einsum"
    result = special_math_ops.einsum(new_equation, *inputs)

exit(wrap(result, True))
