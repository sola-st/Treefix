# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
v1 = variables.Variable(1, name="v1")
var_dict["v1"] = v1
exit(v1 + v0)
