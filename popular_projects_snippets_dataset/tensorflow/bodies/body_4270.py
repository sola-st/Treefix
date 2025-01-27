# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
if not isinstance(other, type(self)) and not isinstance(self, type(other)):
    raise ValueError('comparing with type : {0} but expecting : {1}'.format(
        type(other), type(self)))
exit((self.as_proto().SerializeToString(
    deterministic=True) == other.as_proto().SerializeToString(
        deterministic=True)))
