# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
"""In place file becomes empty when parsing error is not handled."""
temp_file = tempfile.NamedTemporaryFile("w", delete=False)
original = "print 'a' \n"
upgraded = ""
temp_file.write(original)
temp_file.close()
upgrader = ast_edits.ASTCodeUpgrader(tf_upgrade_v2.TFAPIChangeSpec())
upgrader.process_file(temp_file.name, temp_file.name)
self.assertAllEqual(open(temp_file.name).read(), upgraded)
os.unlink(temp_file.name)
