# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema.py
"""Upgrade data from Version 0 to Version 1.

    Changes: Added subgraphs (which contains a subset of formally global
    entries).

    Args:
      data: Dictionary representing the TensorFlow lite data to be upgraded.
        This will be modified in-place to be an upgraded version.
    """
subgraph = {}
for key_to_promote in ["tensors", "operators", "inputs", "outputs"]:
    subgraph[key_to_promote] = data[key_to_promote]
    del data[key_to_promote]
data["subgraphs"] = [subgraph]
