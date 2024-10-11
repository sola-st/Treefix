# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
"""Load and run the SavedModel signature in the TF 1.x style."""
model = saved_model_loader.load(sess, [tag_constants.SERVING], export_dir)
signature = model.signature_def['train']
inputs = list(signature.inputs.values())
assert len(inputs) == 1, inputs
outputs = list(signature.outputs.values())
assert len(outputs) == 1, outputs
input_tensor = sess.graph.get_tensor_by_name(inputs[0].name)
output_tensor = sess.graph.get_tensor_by_name(outputs[0].name)
for v in input_values:
    sess.run(output_tensor, feed_dict={input_tensor: v})
