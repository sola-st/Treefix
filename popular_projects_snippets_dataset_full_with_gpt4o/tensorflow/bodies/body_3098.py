# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/gen_quantized_function_library.py
"""Substitutes the for loop templates in the given module."""
compiled_regex = re.compile(
    r'^\s*for\s(.*?)\sin\s(\[.*?\])\s\{(.*?)\}\s//\send\sfor\n',
    re.MULTILINE | re.DOTALL)
while True:
    func_match = re.search(compiled_regex, module)
    if func_match is None:
        break

    try:
        arg_name = func_match.group(1)
        arg_values = ast.literal_eval(func_match.group(2))
        loop_template = string.Template(func_match.group(3))
    except Exception as e:  # pylint: disable=broad-except
        raise ValueError('The loop template is in wrong format') from e

    replacement_text = ''
    for arg_value in arg_values:
        arg_dict = {arg_name: arg_value}
        replacement_text += '\\n'
        replacement_text += _substitute_parameterization_template(
            loop_template.safe_substitute(arg_dict))
    module = re.sub(compiled_regex, replacement_text, module, count=1)

exit(module)
