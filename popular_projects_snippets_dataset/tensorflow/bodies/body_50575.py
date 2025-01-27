# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
embeddings_ckpt = os.path.join(self._log_write_dir, 'train',
                               'keras_embedding.ckpt-{}'.format(epoch))
self.model.save_weights(embeddings_ckpt)
