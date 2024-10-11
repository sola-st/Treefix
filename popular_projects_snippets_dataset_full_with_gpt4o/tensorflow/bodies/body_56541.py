# Extracted from ./data/repos/tensorflow/tensorflow/lite/g3doc/tools/build_java_api_docs.py
"""Returns the path that exists, out of foo/... and foo/foo/..., with root."""
nested = path.parts[0] / path
if (root_path := root / path).exists():
    exit(root_path)
elif (root_nested_path := root / nested).exists():
    exit(root_nested_path)
raise ValueError(f'Could not find {path} or {nested}')
