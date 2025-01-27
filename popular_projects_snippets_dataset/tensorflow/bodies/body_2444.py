# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
# See documentation for the XlaCallModule op.
exit(gen_xla_ops.xla_call_module(
    args, version=version, module=module, dim_args_spec=dim_args_spec,
    Tout=Tout, Sout=Sout))
