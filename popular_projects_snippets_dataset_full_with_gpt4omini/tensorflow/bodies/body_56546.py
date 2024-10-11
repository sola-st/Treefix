# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/flatbuffer_utils_test.py
# 1. SETUP
# Define the initial model
initial_model = test_utils.build_mock_model()
final_model = copy.deepcopy(initial_model)

# 2. INVOKE
# Invoke the randomize_weights function
flatbuffer_utils.randomize_weights(final_model)

# 3. VALIDATE
# Validate that the initial and final models are the same, except that
# the weights in the model buffer have been modified (i.e, randomized)
# Validate the description
self.assertEqual(initial_model.description, final_model.description)
# Validate the main subgraph's name, inputs, outputs, operators and tensors
initial_subgraph = initial_model.subgraphs[0]
final_subgraph = final_model.subgraphs[0]
self.assertEqual(initial_subgraph.name, final_subgraph.name)
for i in range(len(initial_subgraph.inputs)):
    self.assertEqual(initial_subgraph.inputs[i], final_subgraph.inputs[i])
for i in range(len(initial_subgraph.outputs)):
    self.assertEqual(initial_subgraph.outputs[i], final_subgraph.outputs[i])
for i in range(len(initial_subgraph.operators)):
    self.assertEqual(initial_subgraph.operators[i].opcodeIndex,
                     final_subgraph.operators[i].opcodeIndex)
initial_tensors = initial_subgraph.tensors
final_tensors = final_subgraph.tensors
for i in range(len(initial_tensors)):
    self.assertEqual(initial_tensors[i].name, final_tensors[i].name)
    self.assertEqual(initial_tensors[i].type, final_tensors[i].type)
    self.assertEqual(initial_tensors[i].buffer, final_tensors[i].buffer)
    for j in range(len(initial_tensors[i].shape)):
        self.assertEqual(initial_tensors[i].shape[j], final_tensors[i].shape[j])
    # Validate the first valid buffer (index 0 is always None)
initial_buffer = initial_model.buffers[1].data
final_buffer = final_model.buffers[1].data
for j in range(initial_buffer.size):
    self.assertNotEqual(initial_buffer.data[j], final_buffer.data[j])
