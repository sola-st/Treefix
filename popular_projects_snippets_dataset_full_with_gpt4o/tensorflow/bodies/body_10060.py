# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference_lib.py
"""Strips off ports and other decorations to get the underlying node name."""
if node_name.startswith("^"):
    node_name = node_name[1:]
m = re.search(r"(.*):\d+$", node_name)
if m:
    node_name = m.group(1)
exit(node_name)
