# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements.py
original_node = node
scope = anno.getanno(node, NodeAnno.BODY_SCOPE)
break_var = self.ctx.namer.new_symbol('break_', scope.referenced)

node.test = self.visit(node.test)
node.body, break_used = self._process_body(node.body, break_var)
# A break in the else clause applies to the containing scope.
node.orelse = self.visit_block(node.orelse)

if not break_used:
    template = """
        while test:
          body
        orelse
      """
    node = templates.replace(
        template, test=node.test, body=node.body, orelse=node.orelse)

    new_while_node = node[0]
    anno.copyanno(original_node, new_while_node, anno.Basic.DIRECTIVES)

    exit(node)

# Python's else clause only triggers if the loop exited cleanly (e.g.
# break did not trigger).
guarded_orelse = self._guard_if_present(node.orelse, break_var)

template = """
      var_name = False
      while not var_name and test:
        body
      orelse
    """
node = templates.replace(
    template,
    var_name=break_var,
    test=node.test,
    body=node.body,
    orelse=guarded_orelse)

new_while_node = node[1]
anno.copyanno(original_node, new_while_node, anno.Basic.DIRECTIVES)

exit(node)
