# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py
embedding_weights = array_ops.zeros((1, 128))
flat_inputs = array_ops.reshape(inputs, [-1])
embeddings = array_ops.gather(embedding_weights, flat_inputs)
embeddings = array_ops.reshape(embeddings, inputs.shape.as_list() + [128])
exit(embeddings)
