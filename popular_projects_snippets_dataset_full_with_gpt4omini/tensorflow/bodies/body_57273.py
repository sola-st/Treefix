# Extracted from ./data/repos/tensorflow/tensorflow/lite/toco/python/toco_from_protos_test.py
"""Use toco binary to check conversion from graphdef to tflite.

    Args:
      sess: Active TensorFlow session containing graph.
      in_tensor: TensorFlow tensor to use as input.
      out_tensor: TensorFlow tensor to use as output.
      should_succeed: Whether this is a valid conversion.
    """
# Build all protos and extract graphdef
graph_def = sess.graph_def
toco_flags = toco_flags_pb2.TocoFlags()
toco_flags.input_format = toco_flags_pb2.TENSORFLOW_GRAPHDEF
toco_flags.output_format = toco_flags_pb2.TFLITE
toco_flags.inference_input_type = types_pb2.FLOAT
toco_flags.inference_type = types_pb2.FLOAT
toco_flags.allow_custom_ops = True
model_flags = model_flags_pb2.ModelFlags()
input_array = model_flags.input_arrays.add()
input_array.name = TensorName(in_tensor)
input_array.shape.dims.extend(map(int, in_tensor.shape))
model_flags.output_arrays.append(TensorName(out_tensor))
# Shell out to run toco (in case it crashes)
with tempfile.NamedTemporaryFile() as fp_toco, \
           tempfile.NamedTemporaryFile() as fp_model, \
           tempfile.NamedTemporaryFile() as fp_input, \
           tempfile.NamedTemporaryFile() as fp_output:
    fp_model.write(model_flags.SerializeToString())
    fp_toco.write(toco_flags.SerializeToString())
    fp_input.write(graph_def.SerializeToString())
    fp_model.flush()
    fp_toco.flush()
    fp_input.flush()
    tflite_bin = resource_loader.get_path_to_datafile("toco_from_protos.par")
    cmdline = " ".join([
        tflite_bin, fp_model.name, fp_toco.name, fp_input.name, fp_output.name
    ])
    exitcode = os.system(cmdline)
    if exitcode == 0:
        stuff = fp_output.read()
        self.assertEqual(stuff is not None, should_succeed)
    else:
        self.assertFalse(should_succeed)
