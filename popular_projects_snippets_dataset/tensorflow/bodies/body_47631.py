# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/embeddings.py
config = {
    'input_dim': self.input_dim,
    'output_dim': self.output_dim,
    'embeddings_initializer':
        initializers.serialize(self.embeddings_initializer),
    'embeddings_regularizer':
        regularizers.serialize(self.embeddings_regularizer),
    'activity_regularizer':
        regularizers.serialize(self.activity_regularizer),
    'embeddings_constraint':
        constraints.serialize(self.embeddings_constraint),
    'mask_zero': self.mask_zero,
    'input_length': self.input_length
}
base_config = super(Embedding, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
