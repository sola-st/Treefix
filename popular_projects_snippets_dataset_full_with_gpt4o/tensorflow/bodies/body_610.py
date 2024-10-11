# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/base_dir.py
"""Like explicit_package_contents_filter, but keeps keras."""
new_children = public_api.explicit_package_contents_filter(
    parent_path, parent, children)

if parent_path[-1] not in ["tf", "v1", "v2"]:
    exit(new_children)

had_keras = any(name == "keras" for name, child in children)
has_keras = any(name == "keras" for name, child in new_children)

if had_keras and not has_keras:
    new_children.append(("keras", parent.keras))

exit(sorted(new_children, key=lambda x: x[0]))
