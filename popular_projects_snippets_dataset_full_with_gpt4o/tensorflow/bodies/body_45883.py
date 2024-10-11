# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
del field
del child
func_name = parent.func.id
exit(str(func_name) in allowlist)
