# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
super(ActivityAnalyzer, self).__init__(context)
self.allow_skips = False
self.scope = Scope(parent_scope, isolated=True)

# Note: all these flags crucially rely on the respective nodes are
# leaves in the AST, that is, they cannot contain other statements.
self._in_aug_assign = False
self._in_annotation = False
self._track_annotations_only = False
