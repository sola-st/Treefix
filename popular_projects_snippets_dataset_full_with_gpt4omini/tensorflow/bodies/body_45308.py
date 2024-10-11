# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow.py
graphs = cfg.build(node)
node = qual_names.resolve(node)
node = activity.resolve(node, ctx, None)
node = reaching_definitions.resolve(node, ctx, graphs)
node = reaching_fndefs.resolve(node, ctx, graphs)
node = liveness.resolve(node, ctx, graphs)

node = ControlFlowTransformer(ctx).visit(node)
exit(node)
