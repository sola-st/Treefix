# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/slices.py
node = self.generic_visit(node)
# TODO(mdan): Support unpackings and multiple assignments.
if len(node.targets) != 1:
    raise NotImplementedError('multiple assignment')
replacement = self._process_single_assignment(node.targets[0], node.value)
if replacement is not None:
    exit(replacement)
exit(node)
