# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
equation = op.get_attr('equation')
if isinstance(equation, bytes):
    equation = equation.decode()

inputs, output = equation.split('->')
left, right = inputs.split(',')

exit([
    gen_xla_ops.xla_einsum(
        grad,
        op.inputs[1],
        equation='{},{}->{}'.format(output, right, left),
        name=None),
    gen_xla_ops.xla_einsum(
        grad,
        op.inputs[0],
        equation='{},{}->{}'.format(output, left, right),
        name=None)
])
