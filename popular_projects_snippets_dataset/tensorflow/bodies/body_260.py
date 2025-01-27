# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
in_file = io.StringIO(old_file_text)
out_file = io.StringIO()
upgrader = ast_edits.ASTCodeUpgrader(
    tf_upgrade_v2.TFAPIChangeSpec(
        import_rename, upgrade_compat_v1_import=upgrade_compat_v1_import))
count, report, errors = (
    upgrader.process_opened_file("test.py", in_file,
                                 "test_out.py", out_file))
exit((count, report, errors, out_file.getvalue()))
