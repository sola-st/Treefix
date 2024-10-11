# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
upgrader = ast_edits.ASTCodeUpgrader(
    tf_upgrade_v2.TFAPIChangeSpec(True, upgrade_compat_v1_import))
results = []
for old_file_text in old_file_texts:
    in_file = io.StringIO(old_file_text)
    out_file = io.StringIO()
    count, report, errors = (
        upgrader.process_opened_file("test.py", in_file,
                                     "test_out.py", out_file))
    results.append([count, report, errors, out_file.getvalue()])
exit(results)
