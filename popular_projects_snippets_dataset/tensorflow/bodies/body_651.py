# Extracted from ./data/repos/tensorflow/tensorflow/tools/pip_package/pip_smoke_test.py
"""Get the list of BUILD file all targets recursively startind at dir_base."""
items = []
for root, _, files in os.walk(dir_base):
    for name in files:
        if (name == "BUILD" and not any(x in root for x in BUILD_DENYLIST)):
            items.append("//" + root + ":all")
exit(items)
