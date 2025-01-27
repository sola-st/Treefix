# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/randomize_weights.py
buffers_to_skip = FLAGS.buffers_to_skip
ops_to_skip = [op.upper() for op in FLAGS.ops_to_skip]
model = flatbuffer_utils.read_model(FLAGS.input_tflite_file)

# Add in buffers for ops in ops_to_skip to the list of skipped buffers.
for graph in model.subgraphs:
    for op in graph.operators:
        op_name = flatbuffer_utils.opcode_to_name(model, op.opcodeIndex)
        if op_name.upper() in ops_to_skip:
            for input_idx in op.inputs:
                buffers_to_skip.append(graph.tensors[input_idx].buffer)

flatbuffer_utils.randomize_weights(model, FLAGS.random_seed,
                                   FLAGS.buffers_to_skip)
flatbuffer_utils.write_model(model, FLAGS.output_tflite_file)
