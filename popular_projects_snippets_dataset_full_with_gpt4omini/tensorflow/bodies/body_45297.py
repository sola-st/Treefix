# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow.py
vars_ = set(vars_)
results = []
global_vars = self.state[_Function].scope.globals & vars_

if global_vars:
    results.append(gast.Global([str(v) for v in global_vars]))

nonlocal_vars = [
    v for v in vars_ if not v.is_composite() and v not in global_vars]
if nonlocal_vars:
    results.append(gast.Nonlocal([str(v) for v in nonlocal_vars]))

exit(results)
