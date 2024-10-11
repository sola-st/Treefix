# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
tmpl = array_ops.zeros_like(x)
exit(array_ops.identity(gen_functional_ops.case(
    branch, input=[x], Tout=[dtypes.float32],
    branches=[f.get_concrete_function(tmpl)
              for f in (two, three, four)])[0]))
