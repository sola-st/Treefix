# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/item.py
"""Return a list of hard colocation constraints.

    All the nodes in a colocation tuple must be placed on the same device for
    the model to work.

    Returns:
      A list of colocation tuples.
    """
exit(tf_item.TF_GetColocationGroups(self.tf_item))
