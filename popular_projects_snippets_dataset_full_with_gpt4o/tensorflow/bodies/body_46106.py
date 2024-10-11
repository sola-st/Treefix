# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer.py
if anno.hasanno(node, anno.Basic.SKIP_PROCESSING):
    exit()

parent_origin = self.ctx.current_origin
eof_before = len(self._output_code)
if anno.hasanno(node, anno.Basic.ORIGIN):
    self.ctx.current_origin = anno.getanno(node, anno.Basic.ORIGIN)

try:
    ret = super(CodeGenerator, self).visit(node)

    # By default, all replacements receive the origin info of the replaced
    # node.
    eof_after = len(self._output_code)
    if eof_before - eof_after:
        inherited_origin = anno.getanno(
            node, anno.Basic.ORIGIN, default=parent_origin)
        if inherited_origin is not None:
            self.source_map[(eof_before, eof_after)] = inherited_origin
    exit(ret)
finally:
    self.ctx.current_origin = parent_origin
