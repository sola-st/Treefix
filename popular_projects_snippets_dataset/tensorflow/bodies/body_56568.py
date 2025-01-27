# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/visualize.py
"""Returns html description with the given tflite model.

  Args:
    tflite_input: TFLite flatbuffer model path or model object.
    input_is_filepath: Tells if tflite_input is a model path or a model object.

  Returns:
    Dump of the given tflite model in HTML format.

  Raises:
    RuntimeError: If the input is not valid.
  """

# Convert the model into a JSON flatbuffer using flatc (build if doesn't
# exist.
if input_is_filepath:
    if not os.path.exists(tflite_input):
        raise RuntimeError("Invalid filename %r" % tflite_input)
    if tflite_input.endswith(".tflite") or tflite_input.endswith(".bin"):
        with open(tflite_input, "rb") as file_handle:
            file_data = bytearray(file_handle.read())
        data = CreateDictFromFlatbuffer(file_data)
    elif tflite_input.endswith(".json"):
        data = json.load(open(tflite_input))
    else:
        raise RuntimeError("Input file was not .tflite or .json")
else:
    data = CreateDictFromFlatbuffer(tflite_input)
html = ""
html += _CSS
html += "<h1>TensorFlow Lite Model</h2>"

data["filename"] = tflite_input if input_is_filepath else (
    "Null (used model object)")  # Avoid special case

toplevel_stuff = [("filename", None), ("version", None),
                  ("description", None)]

html += "<table>\n"
for key, mapping in toplevel_stuff:
    if not mapping:
        mapping = lambda x: x
    html += "<tr><th>%s</th><td>%s</td></tr>\n" % (key, mapping(data.get(key)))
html += "</table>\n"

# Spec on what keys to display
buffer_keys_to_display = [("data", DataSizeMapper())]
operator_keys_to_display = [("builtin_code", BuiltinCodeToName),
                            ("custom_code", NameListToString),
                            ("version", None)]

# Update builtin code fields.
for d in data["operator_codes"]:
    d["builtin_code"] = max(d["builtin_code"], d["deprecated_builtin_code"])

for subgraph_idx, g in enumerate(data["subgraphs"]):
    # Subgraph local specs on what to display
    html += "<div class='subgraph'>"
    tensor_mapper = TensorMapper(g)
    opcode_mapper = OpCodeMapper(data)
    op_keys_to_display = [("inputs", tensor_mapper), ("outputs", tensor_mapper),
                          ("builtin_options", None),
                          ("opcode_index", opcode_mapper)]
    tensor_keys_to_display = [("name", NameListToString),
                              ("type", TensorTypeToName), ("shape", None),
                              ("shape_signature", None), ("buffer", None),
                              ("quantization", None)]

    html += "<h2>Subgraph %d</h2>\n" % subgraph_idx

    # Inputs and outputs.
    html += "<h3>Inputs/Outputs</h3>\n"
    html += GenerateTableHtml([{
        "inputs": g["inputs"],
        "outputs": g["outputs"]
    }], [("inputs", tensor_mapper), ("outputs", tensor_mapper)],
                              display_index=False)

    # Print the tensors.
    html += "<h3>Tensors</h3>\n"
    html += GenerateTableHtml(g["tensors"], tensor_keys_to_display)

    # Print the ops.
    if g["operators"]:
        html += "<h3>Ops</h3>\n"
        html += GenerateTableHtml(g["operators"], op_keys_to_display)

    # Visual graph.
    html += "<svg id='subgraph%d' width='1600' height='900'></svg>\n" % (
        subgraph_idx,)
    html += GenerateGraph(subgraph_idx, g, opcode_mapper)
    html += "</div>"

# Buffers have no data, but maybe in the future they will
html += "<h2>Buffers</h2>\n"
html += GenerateTableHtml(data["buffers"], buffer_keys_to_display)

# Operator codes
html += "<h2>Operator Codes</h2>\n"
html += GenerateTableHtml(data["operator_codes"], operator_keys_to_display)

html += "</body></html>\n"

exit(html)
