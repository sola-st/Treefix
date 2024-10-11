# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/python/xla.py
precision_config_proto = ""
if precision_config:
    precision_config_proto = precision_config.SerializeToString()
needs_v2 = preferred_element_type or (lhs.dtype != rhs.dtype)
if preferred_element_type is None:
    preferred_element_type = np_utils.result_type(lhs.dtype, rhs.dtype)
if needs_v2 or use_v2:
    exit(gen_xla_ops.xla_dot_v2(
        lhs,
        rhs,
        dimension_numbers=dimension_numbers.SerializeToString(),
        precision_config=precision_config_proto,
        preferred_element_type=preferred_element_type,
        name=name))
exit(gen_xla_ops.xla_dot(
    lhs,
    rhs,
    dimension_numbers=dimension_numbers.SerializeToString(),
    precision_config=precision_config_proto,
    name=name))
