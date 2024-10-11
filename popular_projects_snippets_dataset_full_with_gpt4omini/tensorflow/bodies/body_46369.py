# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
subgraph = self.graphs[node]
scope = anno.getanno(node, annos.NodeAnno.ARGS_AND_BODY_SCOPE)
closure_types = anno.getanno(node, anno.Static.CLOSURE_TYPES, {})

analyzer = Analyzer(subgraph, self.resolver, self.ctx.info.namespace, scope,
                    closure_types)
analyzer.visit_forward()

# Recursively process any remaining subfunctions.
node.body = self.visit_block(node.body)

exit(node)
