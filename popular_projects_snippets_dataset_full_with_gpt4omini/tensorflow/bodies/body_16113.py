# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_string_ops.py
"""Version of tf.strings.format that handles RaggedTensors."""
if tensor_util.is_tf_type(inputs) or ragged_tensor.is_ragged(inputs):
    inputs = [inputs]

split_template = template.split(placeholder)
if len(inputs) != len(split_template) - 1:
    raise ValueError("num placeholders in template and num inputs must match"
                     ": {} vs {}".format(len(split_template) - 1, len(inputs)))

with ops.name_scope(name, "StringFormat", [inputs]):
    output_pieces = [constant_op.constant(split_template[0])]
    for i, input in enumerate(inputs):
        if ragged_tensor.is_ragged(input):
            output_pieces.append(ragged_tensor_to_string(input, summarize))
        else:
            output_pieces.append(string_ops.string_format(
                "{}", [input], summarize=summarize))
        output_pieces.append(constant_op.constant(split_template[i + 1]))
    if len(output_pieces) == 1:
        exit(output_pieces[0])
    else:
        exit(string_ops.reduce_join(output_pieces))
