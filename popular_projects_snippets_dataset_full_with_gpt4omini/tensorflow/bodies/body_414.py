# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
"""Check to make sure we don't have a file system race."""
temp_file = tempfile.NamedTemporaryFile("w", delete=False)
original = "tf.conj(a)\n"
upgraded = "tf.math.conj(a)\n"
temp_file.write(original)
temp_file.close()
upgrader = ast_edits.ASTCodeUpgrader(tf_upgrade_v2.TFAPIChangeSpec())
upgrader.process_file(temp_file.name, temp_file.name)
self.assertAllEqual(open(temp_file.name).read(), upgraded)
os.unlink(temp_file.name)
