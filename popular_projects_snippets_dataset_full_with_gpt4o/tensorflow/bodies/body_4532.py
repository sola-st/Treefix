# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/freeze.py
"""Writes a SavedModel out to disk.

  Args:
    file_name: Where to save the file.
    sess: TensorFlow session containing the graph.
    input_tensor: Tensor object defining the input's properties.
    output_tensor: Tensor object defining the output's properties.
  """
# Store the frozen graph as a SavedModel for v2 compatibility.
builder = tf.compat.v1.saved_model.builder.SavedModelBuilder(file_name)
tensor_info_inputs = {
    'input': tf.compat.v1.saved_model.utils.build_tensor_info(input_tensor)
}
tensor_info_outputs = {
    'output': tf.compat.v1.saved_model.utils.build_tensor_info(output_tensor)
}
signature = (
    tf.compat.v1.saved_model.signature_def_utils.build_signature_def(
        inputs=tensor_info_inputs,
        outputs=tensor_info_outputs,
        method_name=tf.compat.v1.saved_model.signature_constants
        .PREDICT_METHOD_NAME))
builder.add_meta_graph_and_variables(
    sess,
    [tf.compat.v1.saved_model.tag_constants.SERVING],
    signature_def_map={
        tf.compat.v1.saved_model.signature_constants
        .DEFAULT_SERVING_SIGNATURE_DEF_KEY:
            signature,
    },
)
builder.save()
