# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_test.py
input_info = {
    input_name: utils.build_tensor_info(tensor)
    for input_name, tensor in inputs.items()
}
output_info = {
    output_name: utils.build_tensor_info(tensor)
    for output_name, tensor in outputs.items()
}
exit(signature_def_utils_impl.build_signature_def(input_info, output_info,
                                                    name))
