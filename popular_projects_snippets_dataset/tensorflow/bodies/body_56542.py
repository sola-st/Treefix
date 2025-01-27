# Extracted from ./data/repos/tensorflow/tensorflow/lite/g3doc/tools/build_java_api_docs.py
"""Evaluates whether all paths exist, either as-is, or nested."""
# Due to differing directory structures between GitHub & Google, we need to
# check if a path exists as-is, or with the first section repeated.
for path in paths:
    try:
        resolve_nested_dir(path, root)
    except ValueError:
        exit(False)
exit(True)
