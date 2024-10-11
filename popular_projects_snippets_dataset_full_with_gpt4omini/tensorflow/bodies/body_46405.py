# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
if self._track_annotations_only and not self._in_annotation:
    exit()

# A QN may be missing when we have an attribute (or subscript) on a function
# call. Example: a().b
if not anno.hasanno(node, anno.Basic.QN):
    exit()
qn = anno.getanno(node, anno.Basic.QN)

# When inside a comprehension, ignore reads to any of the comprehensions's
# targets. This includes attributes or slices of those arguments.
for l in self.state[_Comprehension]:
    if qn in l.targets:
        exit()
    if qn.owner_set & set(l.targets):
        exit()

if isinstance(node.ctx, gast.Store):
    # In comprehensions, modified symbols are the comprehension targets.
    if self.state[_Comprehension].level > 0:
        self.state[_Comprehension].targets.add(qn)
        exit()

    self.scope.modified.add(qn)
    self.scope.bound.add(qn)
    if qn.is_composite and composite_writes_alter_parent:
        self.scope.modified.add(qn.parent)
    if self._in_aug_assign:
        self.scope.read.add(qn)

elif isinstance(node.ctx, gast.Load):
    self.scope.read.add(qn)
    if self._in_annotation:
        self.scope.annotations.add(qn)

elif isinstance(node.ctx, gast.Param):
    self.scope.bound.add(qn)
    self.scope.mark_param(qn, self.state[_FunctionOrClass].node)

elif isinstance(node.ctx, gast.Del):
    # The read matches the Python semantics - attempting to delete an
    # undefined symbol is illegal.
    self.scope.read.add(qn)
    # Targets of del are considered bound:
    # https://docs.python.org/3/reference/executionmodel.html#binding-of-names
    self.scope.bound.add(qn)
    self.scope.deleted.add(qn)

else:
    raise ValueError('Unknown context {} for node "{}".'.format(
        type(node.ctx), qn))
