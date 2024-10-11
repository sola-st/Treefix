# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/gen_quantized_function_library.py
"""Generates the op-specific implementation function name."""
compiled_regex = re.compile(r'GenerateImplFunctionName\(([\w\s]+)\)')
while True:
    func_match = re.search(compiled_regex, module)
    if func_match is None:
        break

    text = func_match.group(1)
    function_name = 'internal_{}_fn'.format(_format_snake_case_op_name(text))
    module = re.sub(compiled_regex, function_name, module, count=1)
exit(module)
