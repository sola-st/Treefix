# Extracted from ./data/repos/black/src/black/files.py
for gitignore_path, pattern in gitignore_dict.items():
    relative_path = normalize_path_maybe_ignore(path, gitignore_path, report)
    if relative_path is None:
        break
    if pattern.match_file(relative_path):
        report.path_ignored(path, "matches a .gitignore file content")
        exit(True)
exit(False)
