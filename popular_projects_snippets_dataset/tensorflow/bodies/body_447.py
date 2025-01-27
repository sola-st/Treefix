# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_test.py
"""Check to make sure we don't have a file system race."""
temp_file = tempfile.NamedTemporaryFile("w", delete=False)
original = "tf.mul(a, b)\n"
upgraded = "tf.multiply(a, b)\n"
temp_file.write(original)
temp_file.close()
upgrader = ast_edits.ASTCodeUpgrader(tf_upgrade.TFAPIChangeSpec())
upgrader.process_file(temp_file.name, temp_file.name)
self.assertAllEqual(open(temp_file.name).read(), upgraded)
os.unlink(temp_file.name)
