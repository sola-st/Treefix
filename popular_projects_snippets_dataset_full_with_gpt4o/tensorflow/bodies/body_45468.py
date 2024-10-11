# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements.py
original_node = node
scope = anno.getanno(node, NodeAnno.BODY_SCOPE)
break_var = self.ctx.namer.new_symbol('break_', scope.referenced)

node.target = self.visit(node.target)
node.iter = self.visit(node.iter)
node.body, break_used = self._process_body(node.body, break_var)
# A break in the else clause applies to the containing scope.
node.orelse = self.visit_block(node.orelse)

if not break_used:
    template = """
        for target in iter_:
          body
        orelse
      """
    node = templates.replace(
        template,
        iter_=node.iter,
        target=node.target,
        body=node.body,
        orelse=node.orelse)

    new_for_node = node[0]
    anno.copyanno(original_node, new_for_node, anno.Basic.EXTRA_LOOP_TEST)
    anno.copyanno(original_node, new_for_node, anno.Basic.DIRECTIVES)

    exit(node)

# Python's else clause only triggers if the loop exited cleanly (e.g.
# break did not trigger).
guarded_orelse = self._guard_if_present(node.orelse, break_var)
extra_test = templates.replace_as_expression(
    'not var_name', var_name=break_var)

# The extra test is hidden in the AST, which will confuse the static
# analysis. To mitigate that, we insert a no-op statement that ensures
# the control variable is marked as used.
# TODO(mdan): Use a marker instead, e.g. ag__.condition_loop_on(var_name)
template = """
      var_name = False
      for target in iter_:
        (var_name,)
        body
      orelse
    """
node = templates.replace(
    template,
    var_name=break_var,
    iter_=node.iter,
    target=node.target,
    body=node.body,
    orelse=guarded_orelse)

new_for_node = node[1]
anno.setanno(new_for_node, anno.Basic.EXTRA_LOOP_TEST, extra_test)
anno.copyanno(original_node, new_for_node, anno.Basic.DIRECTIVES)

exit(node)
