# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_view.py
"""Returns all matching trackables between CheckpointView and Trackable.

    Matching trackables represents trackables with the same name and position in
    graph.

    Args:
      obj: `Trackable` root.

    Returns:
      Dictionary containing all overlapping trackables that maps `node_id` to
      `Trackable`.

    Example usage:

    >>> class SimpleModule(tf.Module):
    ...   def __init__(self, name=None):
    ...     super().__init__(name=name)
    ...     self.a_var = tf.Variable(5.0)
    ...     self.b_var = tf.Variable(4.0)
    ...     self.vars = [tf.Variable(1.0), tf.Variable(2.0)]

    >>> root = SimpleModule(name="root")
    >>> leaf = root.leaf = SimpleModule(name="leaf")
    >>> leaf.leaf3 = tf.Variable(6.0, name="leaf3")
    >>> leaf.leaf4 = tf.Variable(7.0, name="leaf4")
    >>> ckpt = tf.train.Checkpoint(root)
    >>> save_path = ckpt.save('/tmp/tf_ckpts')
    >>> checkpoint_view = tf.train.CheckpointView(save_path)

    >>> root2 = SimpleModule(name="root")
    >>> leaf2 = root2.leaf2 = SimpleModule(name="leaf2")
    >>> leaf2.leaf3 = tf.Variable(6.0)
    >>> leaf2.leaf4 = tf.Variable(7.0)

    Pass `node_id=0` to `tf.train.CheckpointView.children()` to get the
    dictionary of all children directly linked to the checkpoint root.

    >>> checkpoint_view_match = checkpoint_view.match(root2).items()
    >>> for item in checkpoint_view_match:
    ...   print(item)
    (0, ...)
    (1, <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=5.0>)
    (2, <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=4.0>)
    (3, ListWrapper([<tf.Variable 'Variable:0' shape=() dtype=float32,
    numpy=1.0>, <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=2.0>]))
    (6, <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>)
    (7, <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=2.0>)

    """
if not isinstance(obj, base.Trackable):
    raise ValueError(f"Expected a Trackable, got {obj} of type {type(obj)}.")

overlapping_nodes = {}
# Root node is always matched.
overlapping_nodes[0] = obj

# Queue of tuples of node_id and trackable.
to_visit = collections.deque([(0, obj)])
visited = set()
view = trackable_view.TrackableView(obj)
while to_visit:
    current_node_id, current_trackable = to_visit.popleft()
    trackable_children = view.children(current_trackable)
    for child_name, child_node_id in self.children(current_node_id).items():
        if child_node_id in visited or child_node_id == 0:
            continue
        if child_name in trackable_children:
            current_assignment = overlapping_nodes.get(child_node_id)
            if current_assignment is None:
                overlapping_nodes[child_node_id] = trackable_children[child_name]
                to_visit.append((child_node_id, trackable_children[child_name]))
            else:
                # The object was already mapped for this checkpoint load, which
                # means we don't need to do anything besides check that the mapping
                # is consistent (if the dependency DAG is not a tree then there are
                # multiple paths to the same object).
                if current_assignment is not trackable_children[child_name]:
                    logging.warning(
                        "Inconsistent references when matching the checkpoint into "
                        "this object graph. The referenced objects are: "
                        f"({current_assignment} and "
                        f"{trackable_children[child_name]}).")
    visited.add(current_node_id)
exit(overlapping_nodes)
