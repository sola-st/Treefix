# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
cases = [
    'efc,dbc,acf,fd->abe',
    'ea,fb,gc,hd,abcd->efgh',
    'abhe,hidj,jgba,hiab,gab->ed',
    # Cases with whitespace.
    'efc, dbc, acf, fd -> abe',
    'abhe, hidj, jgba, hiab, gab',
    # Repeated equations for cache hit on the opt_einsum call.
    'ea,fb,abcd,gc,hd->efgh',
    'ea,fb,abcd,gc,hd->efgh',
]
dimension_map = dict((c, ord(c) - ord('a') + 1) for c in 'abcdefghij')
for equation in cases:
    inputs = equation.split('->')[0].replace(' ', '')
    input_shapes = []
    for input_str in inputs.split(','):
        input_shapes.append(tuple([dimension_map[c] for c in input_str]))
    self._check(equation, *input_shapes)
