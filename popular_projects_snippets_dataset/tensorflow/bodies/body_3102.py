# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/gen_quantized_function_library.py
"""Generates the quantized function name."""
compiled_regex = re.compile(
    r'GenerateQuantizedFunctionName(\([\w\s\'\"\[\],]+\))')
while True:
    func_match = re.search(compiled_regex, module)
    if func_match is None:
        break

    # Make sure the string ends with ",)" so the parsed value is a tuple.
    argument_string = func_match.group(1)
    if not argument_string.endswith(',)'):
        argument_string = argument_string[:-1] + ',)'
    arguments = ast.literal_eval(argument_string)

    if len(arguments) < 1 or len(arguments) > 2:
        raise ValueError(
            'Wrong number of arguments to GenerateQuantizedFunctionName')

    quantized_ops = arguments[0]
    if not quantized_ops:
        raise ValueError('The quantized_ops list must not be empty')

    # Add op names to the function name.
    function_name = 'quantized_{}'.format(
        _format_snake_case_op_name(quantized_ops[0]))
    if len(quantized_ops) > 1:
        function_name += '_with_{}'.format(
            _format_snake_case_op_name(quantized_ops[1]))
    if len(quantized_ops) > 1:
        for quantized_op in quantized_ops[2:]:
            function_name += '_and_{}'.format(
                _format_snake_case_op_name(quantized_op))

    # Add suffix based on output type.
    suffix = '_fn'
    if len(arguments) > 1 and arguments[1] == 'f32':
        suffix = '_float_output_fn'
    function_name += suffix

    module = re.sub(compiled_regex, function_name, module, count=1)
exit(module)
