# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer.py
"""Populates the TF_ImportGraphDefOptions `options`."""
c_api.TF_ImportGraphDefOptionsSetPrefix(options, prefix)
c_api.TF_ImportGraphDefOptionsSetUniquifyNames(options, True)
c_api.TF_ImportGraphDefOptionsSetPropagateDeviceSpec(options,
                                                     propagate_device_spec)

for input_src, input_dst in input_map.items():
    input_src = compat.as_str(input_src)
    if input_src.startswith('^'):
        src_name = compat.as_str(input_src[1:])
        dst_op = input_dst._as_tf_output().oper  # pylint: disable=protected-access
        c_api.TF_ImportGraphDefOptionsRemapControlDependency(
            options, src_name, dst_op)
    else:
        src_name, src_idx = _ParseTensorName(input_src)
        src_name = compat.as_str(src_name)
        dst_output = input_dst._as_tf_output()  # pylint: disable=protected-access
        c_api.TF_ImportGraphDefOptionsAddInputMapping(options, src_name, src_idx,
                                                      dst_output)
for name in return_elements or []:
    if ':' in name:
        op_name, index = _ParseTensorName(name)
        op_name = compat.as_str(op_name)
        c_api.TF_ImportGraphDefOptionsAddReturnOutput(options, op_name, index)
    else:
        c_api.TF_ImportGraphDefOptionsAddReturnOperation(options,
                                                         compat.as_str(name))

c_api.TF_ImportGraphDefOptionsSetValidateColocationConstraints(
    options, validate_colocation_constraints)
