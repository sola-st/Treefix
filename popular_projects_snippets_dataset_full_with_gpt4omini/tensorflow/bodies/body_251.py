# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Process a directory of python files in place."""
files_to_process = []
for dir_name, _, file_list in os.walk(root_directory):
    py_files = [
        os.path.join(dir_name, f) for f in file_list if f.endswith(".py")
    ]
    files_to_process += py_files

file_count = 0
tree_errors = {}
report = ""
report += ("=" * 80) + "\n"
report += "Input tree: %r\n" % root_directory
report += ("=" * 80) + "\n"

for path in files_to_process:
    if os.path.islink(path):
        report += "Skipping symlink %s.\n" % path
        continue
    file_count += 1
    _, l_report, l_errors = self.process_file(path, path)
    tree_errors[path] = l_errors
    report += l_report

exit((file_count, report, tree_errors))
