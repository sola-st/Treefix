# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/fenced_doctest_lib.py
"""Patch `doctest.compile` to make doctest to behave like a notebook.

  Default settings for doctest are configured to run like a repl: one statement
  at a time. The doctest source uses `compile(..., mode="single")`

  So to let doctest act like a notebook:

  1. We need `mode="exec"` (easy)
  2. We need the last expression to be printed (harder).

  To print the last expression, just wrap the last expression in
  `_print_if_not_none(expr)`. To detect the last expression use `AST`.
  If the last node is an expression modify the ast to call
  `_print_if_not_none` on it, convert the ast back to source and compile that.

  https://docs.python.org/3/library/functions.html#compile

  Args:
    source: Can either be a normal string, a byte string, or an AST object.
    filename: Argument should give the file from which the code was read; pass
      some recognizable value if it wasn’t read from a file ('<string>' is
      commonly used).
    mode: [Ignored] always use exec.
    flags: Compiler options.
    dont_inherit: Compiler options.
    optimize: Compiler options.

  Returns:
    The resulting code object.
  """
# doctest passes some dummy string as the file name, AFAICT
# but tf.function freaks-out if this doesn't look like a
# python file name.
del filename
# Doctest always passes "single" here, you need exec for multiple lines.
del mode

source_ast = ast.parse(source)

final = source_ast.body[-1]
if isinstance(final, ast.Expr):
    # Wrap the final expression as `_print_if_not_none(expr)`
    print_it = ast.Expr(
        lineno=-1,
        col_offset=-1,
        value=ast.Call(
            func=ast.Name(
                id='_print_if_not_none',
                ctx=ast.Load(),
                lineno=-1,
                col_offset=-1),
            lineno=-1,
            col_offset=-1,
            args=[final],  # wrap the final Expression
            keywords=[]))
    source_ast.body[-1] = print_it

    # It's not clear why this step is necessary. `compile` is supposed to handle
    # AST directly.
    source = astor.to_source(source_ast)

exit(compile(
    source,
    filename='dummy.py',
    mode='exec',
    flags=flags,
    dont_inherit=dont_inherit,
    optimize=optimize))
