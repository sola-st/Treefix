# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Configure the Projector for embeddings."""
# TODO(omalleyt): Add integration tests.
from google.protobuf import text_format
from tensorflow.python.keras.layers import embeddings
from tensorflow.python.keras.protobuf import projector_config_pb2

config = projector_config_pb2.ProjectorConfig()
for layer in self.model.layers:
    if isinstance(layer, embeddings.Embedding):
        embedding = config.embeddings.add()
        # Embeddings are always the first layer, so this naming should be
        # consistent in any keras models checkpoints.
        name = 'layer_with_weights-0/embeddings/.ATTRIBUTES/VARIABLE_VALUE'
        embedding.tensor_name = name

        if self.embeddings_metadata is not None:
            if isinstance(self.embeddings_metadata, str):
                embedding.metadata_path = self.embeddings_metadata
            else:
                if layer.name in self.embeddings_metadata.keys():
                    embedding.metadata_path = self.embeddings_metadata.pop(layer.name)

if self.embeddings_metadata and not isinstance(self.embeddings_metadata,
                                               str):
    raise ValueError('Unrecognized `Embedding` layer names passed to '
                     '`keras.callbacks.TensorBoard` `embeddings_metadata` '
                     'argument: ' + str(self.embeddings_metadata.keys()))

config_pbtxt = text_format.MessageToString(config)
path = os.path.join(self._log_write_dir, 'projector_config.pbtxt')
with gfile.Open(path, 'w') as f:
    f.write(config_pbtxt)
