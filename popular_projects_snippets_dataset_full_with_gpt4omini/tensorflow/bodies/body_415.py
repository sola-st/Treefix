# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
"""In place file should not be modified when parsing error is handled."""
temp_file = tempfile.NamedTemporaryFile("w", delete=False)
original = "print 'a' \n"
upgraded = "print 'a' \n"
temp_file.write(original)
temp_file.close()
upgrader = ast_edits.ASTCodeUpgrader(tf_upgrade_v2.TFAPIChangeSpec())
upgrader.process_file(
    temp_file.name, temp_file.name, no_change_to_outfile_on_error=True)
self.assertAllEqual(open(temp_file.name).read(), upgraded)
os.unlink(temp_file.name)
