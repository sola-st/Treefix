# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/zip_test_utils.py
"""Given a dictionary of `examples`, write a text format representation.

  The file format is protocol-buffer-like, even though we don't use proto due
  to the needs of the Android team.

  Args:
    fp: File-like object to write to.
    model_name: Filename where the model was written to, relative to filename.
    examples: Example dictionary consisting of keys "inputs" and "outputs"

  Raises:
    RuntimeError: Example dictionary does not have input / output names.
  """

writer = TextFormatWriter(fp)
writer.write_field("load_model", os.path.basename(model_name))
for example in examples:
    inputs = []
    for name in example["inputs"].keys():
        if name:
            inputs.append(name)
    outputs = []
    for name in example["outputs"].keys():
        if name:
            outputs.append(name)
    if not (inputs and outputs):
        raise RuntimeError("Empty input / output names.")

    # Reshape message
    with writer.sub_message("reshape") as reshape:
        for name, value in example["inputs"].items():
            with reshape.sub_message("input") as input_msg:
                input_msg.write_field("key", name)
                input_msg.write_field("value", ",".join(map(str, value.shape)))

    # Invoke message
    with writer.sub_message("invoke") as invoke:
        for name, value in example["inputs"].items():
            with invoke.sub_message("input") as input_msg:
                input_msg.write_field("key", name)
                input_msg.write_field("value", format_result(value))
      # Expectations
        for name, value in example["outputs"].items():
            with invoke.sub_message("output") as output_msg:
                output_msg.write_field("key", name)
                output_msg.write_field("value", format_result(value))
            with invoke.sub_message("output_shape") as output_shape:
                output_shape.write_field("key", name)
                output_shape.write_field("value",
                                         ",".join([str(dim) for dim in value.shape]))
