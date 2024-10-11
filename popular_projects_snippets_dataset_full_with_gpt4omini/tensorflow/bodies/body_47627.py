# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/embeddings.py
self.embeddings = self.add_weight(
    shape=(self.input_dim, self.output_dim),
    initializer=self.embeddings_initializer,
    name='embeddings',
    regularizer=self.embeddings_regularizer,
    constraint=self.embeddings_constraint,
    experimental_autocast=False)
self.built = True
