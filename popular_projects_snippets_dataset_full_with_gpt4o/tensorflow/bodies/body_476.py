# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
in_file = io.StringIO(old_file_text)
out_file = io.StringIO()
upgrader = ast_edits.ASTCodeUpgrader(spec)
count, report, errors = (
    upgrader.process_opened_file("test.py", in_file,
                                 "test_out.py", out_file))
exit(((count, report, errors), out_file.getvalue()))
