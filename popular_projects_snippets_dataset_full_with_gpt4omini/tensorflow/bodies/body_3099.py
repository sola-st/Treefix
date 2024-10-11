# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/gen_quantized_function_library.py
"""Substitutes all the function templates in the given module."""
compiled_regex = re.compile(
    r'^\s*parameters(\[.*?\])\n?(^\s*(?:func\.)+func.*?\{.*?(?:func\.)+return.*?\}\n)',
    re.MULTILINE | re.DOTALL)
while True:
    func_match = re.search(compiled_regex, module)
    if func_match is None:
        break

    try:
        value_list = ast.literal_eval(func_match.group(1))
        # Escapes template $-based substitutions for attributes containing $.
        # $$ is replaced with a single $.
        func_template = string.Template(
            func_match.group(2).replace('tfdtype$DT_', 'tfdtype$$DT_'))
    except Exception as e:  # pylint: disable=broad-except
        raise ValueError('The function template is in wrong format') from e

    replacement_text = ''
    for value_dict in value_list:
        for key, value in value_dict.items():
            # Replace single quote to double quote since single quote around a
            # string are not valid in the MLIR representation.
            value_dict[key] = str(value).replace("'", '"')
        replacement_text += '\\n'
        replacement_text += func_template.substitute(value_dict)
    module = re.sub(compiled_regex, replacement_text, module, count=1)
exit(module)
