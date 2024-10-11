# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/label_wav.py
"""Read in labels, one label per line."""
exit([line.rstrip() for line in tf.io.gfile.GFile(filename)])
