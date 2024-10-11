# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
cases = [
    # Tests from dask.
    'fdf,cdd,ccd,afe->ae',
    'fff,fae,bef,def->abd',
]
dimension_map = dict((c, ord(c) - ord('a') + 1) for c in 'abcdefghij')
for equation in cases:
    inputs = equation.split('->')[0].replace(' ', '')
    input_shapes = []
    for input_str in inputs.split(','):
        input_shapes.append(tuple([dimension_map[c] for c in input_str]))
    self._check(equation, *input_shapes)
