# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
precision_config_proto = ""
if precision_config:
    precision_config_proto = precision_config.SerializeToString()
exit(gen_xla_ops.xla_svd(a, max_iter, epsilon, precision_config_proto))
