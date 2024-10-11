# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/layer_utils.py
# Parents may have different keys than their children, so we locally
# invalidate but use the `invalidate_all` method of parents.
for key in self.attributes.keys():
    self.attributes[key].mark_as(False)

for node in self._parents:
    node.invalidate_all()
