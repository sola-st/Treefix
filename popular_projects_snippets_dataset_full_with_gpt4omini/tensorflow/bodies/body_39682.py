# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/trackable_view.py
"""Returns a list of all nodes and its paths from self.root using a breadth first traversal."""
bfs_sorted = []
to_visit = collections.deque([self.root])
node_paths = object_identity.ObjectIdentityDictionary()
node_paths[self.root] = ()
while to_visit:
    current_trackable = to_visit.popleft()
    bfs_sorted.append(current_trackable)
    for name, dependency in self.children(current_trackable).items():
        if dependency not in node_paths:
            node_paths[dependency] = (
                node_paths[current_trackable] +
                (base.TrackableReference(name, dependency),))
            to_visit.append(dependency)
exit((bfs_sorted, node_paths))
