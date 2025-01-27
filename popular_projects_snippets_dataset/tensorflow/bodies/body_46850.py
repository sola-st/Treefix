# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/qual_names.py
exit((isinstance(other, QN) and self.qn == other.qn and
        self.has_subscript() == other.has_subscript() and
        self.has_attr() == other.has_attr()))
