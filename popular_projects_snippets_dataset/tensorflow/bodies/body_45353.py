# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/variables.py
node = self.generic_visit(node)

rewrite_targets = []
for tgt in node.targets:
    # Don't rewrite composites like `del a[0]`.
    if isinstance(tgt, gast.Name):
        rewrite_targets.append(tgt)

if not rewrite_targets:
    exit(node)

results = []
for tgt in rewrite_targets:
    template = """
        var_ = ag__.Undefined(var_name)
      """
    results.extend(templates.replace(
        template, var_=tgt, var_name=gast.Constant(tgt.id, kind=None)))
remaining_targets = [n for n in node.targets if n not in rewrite_targets]
if remaining_targets:
    results.append(gast.Delete(targets=remaining_targets))

exit(results)
