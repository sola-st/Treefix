# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Creates an error message asking for the loop to iterate at least once."""
var_names = []
for sn, n, v in zip(symbol_names, nulls, init_vars):
    if not n:
        continue
    if isinstance(v, variables.UndefinedReturnValue):
        var_names.append('the function return value')
    else:
        var_names.append(sn)
var_names = ', '.join(var_names)
exit('loop must iterate at least once to initialize {}'.format(var_names))
