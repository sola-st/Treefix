# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla_test.py
context = self.create_test_xla_compile_context()
context.Enter()
o = a.assign(2)
context.Exit()
exit(o)
