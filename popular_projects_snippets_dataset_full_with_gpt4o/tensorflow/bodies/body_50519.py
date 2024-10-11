# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
# Only call batch hooks when saving on batch
exit(self.save_freq != 'epoch')
