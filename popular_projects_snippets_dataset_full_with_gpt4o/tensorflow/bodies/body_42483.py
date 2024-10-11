# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions.py
node = self.generic_visit(node)
if isinstance(node.ctx, gast.Load) and node.id in self.ctx.info.namespace:
    anno.setanno(node, "static_value", self.ctx.info.namespace[node.id])
exit(node)
