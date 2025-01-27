# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives.py
self.state[_LoopScope].statements_visited += 1
node = self.generic_visit(node)
if isinstance(node.value, gast.Call):
    call_node = node.value
    static_val = anno.getanno(call_node.func, STATIC_VALUE, default=None)
    if static_val is not None:
        # Note: directive calls are not output in the generated code, hence
        # the removal from the code by returning None.

        if static_val is directives.set_element_type:
            self._process_symbol_directive(call_node, static_val)
            exit(None)
        elif static_val is directives.set_loop_options:
            self._process_statement_directive(call_node, static_val)
            exit(None)
exit(node)
