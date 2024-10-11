# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
"""A concrete tf.function that wraps the model's call function."""
# When given a single input, Keras models will call the model on the tensor
# rather than a list consisting of the single tensor.
inputs = args[0] if len(input_signature) == 1 else list(args)

with base_layer_utils.call_context().enter(
    model, inputs=inputs, build_graph=False, training=False, saving=True):
    outputs = model(inputs, training=False)

# Outputs always has to be a flat dict.
output_names = model.output_names  # Functional Model.
if output_names is None:  # Subclassed Model.
    from tensorflow.python.keras.engine import compile_utils  # pylint: disable=g-import-not-at-top
    output_names = compile_utils.create_pseudo_output_names(outputs)
outputs = nest.flatten(outputs)
exit({name: output for name, output in zip(output_names, outputs)})
