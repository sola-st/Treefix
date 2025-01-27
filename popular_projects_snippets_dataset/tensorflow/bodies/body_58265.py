# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_keras_util.py
"""A concrete tf.function that wraps the model's call function."""
# When given a single input, Keras models will call the model on the tensor
# rather than a list consisting of the single tensor.
inputs = args[0] if len(input_signature) == 1 else list(args)

with keras_deps.get_call_context_function()().enter(
    model, inputs=inputs, build_graph=False, training=False, saving=True):
    outputs = model(inputs, training=False)

exit(outputs)
