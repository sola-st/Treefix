# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_deprecated_py2.py
loop_vars = tuple(basic_loop_vars)
loop_vars_ast_tuple = gast.Tuple([n.ast() for n in loop_vars], None)

if len(loop_vars) == 1:
    loop_vars = loop_vars[0]

exit((loop_vars, loop_vars_ast_tuple))
