# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference.py
if not gfile.Exists(FLAGS.input):
    print("Input graph file '" + FLAGS.input + "' does not exist!")
    exit(-1)

input_graph_def = graph_pb2.GraphDef()
with gfile.Open(FLAGS.input, "rb") as f:
    data = f.read()
    if FLAGS.frozen_graph:
        input_graph_def.ParseFromString(data)
    else:
        text_format.Merge(data.decode("utf-8"), input_graph_def)

output_graph_def = optimize_for_inference_lib.optimize_for_inference(
    input_graph_def,
    FLAGS.input_names.split(","),
    FLAGS.output_names.split(","),
    _parse_placeholder_types(FLAGS.placeholder_type_enum),
    FLAGS.toco_compatible)

if FLAGS.frozen_graph:
    f = gfile.GFile(FLAGS.output, "w")
    f.write(output_graph_def.SerializeToString())
else:
    graph_io.write_graph(output_graph_def,
                         os.path.dirname(FLAGS.output),
                         os.path.basename(FLAGS.output))
exit(0)
