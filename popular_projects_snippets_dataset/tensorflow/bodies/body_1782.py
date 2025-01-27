# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_call_module_test.py
exit(xla.call_module([x, y],
                       version=2,
                       module=module,
                       Tout=[x.dtype, np.int32],
                       Sout=[(None, 3), ()],
                       dim_args_spec=dim_args_spec))
