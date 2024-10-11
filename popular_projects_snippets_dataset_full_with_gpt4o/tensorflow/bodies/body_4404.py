# Extracted from ./data/repos/tensorflow/tensorflow/examples/label_image/label_image.py
proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
exit([l.rstrip() for l in proto_as_ascii_lines])
