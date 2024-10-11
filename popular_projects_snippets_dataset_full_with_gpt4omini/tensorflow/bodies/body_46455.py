# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py
node = qual_names.resolve(node)
node = activity.resolve(node, ctx)
graphs = cfg.build(node)
node = reaching_definitions.resolve(node, ctx, graphs)
node = reaching_fndefs.resolve(node, ctx, graphs)
node = type_inference.resolve(node, ctx, graphs, self.resolver)
exit(node)
