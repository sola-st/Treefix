# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
cases = [
    'abhe,hidj,jgba,hiab,gab->ed',
    # Tests from dask.
    'ea,fb,abcd,gc,hd->efgh',
]
dimension_map = dict(
    (c, ((ord(c) - ord('a')) % 3) + 1) for c in 'abcdefghij')
for equation in cases:
    inputs = equation.split('->')[0].replace(' ', '')
    input_shapes = []
    for input_str in inputs.split(','):
        input_shapes.append(tuple([dimension_map[c] for c in input_str]))
    self._check_gradient(equation, *input_shapes)
