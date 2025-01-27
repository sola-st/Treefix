# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser.py
"""Returns the AST and source code of given lambda function.

  Args:
    lam: types.LambdaType, Python function/method/class

  Returns:
    gast.AST, Text: the parsed AST node; the source code that was parsed to
    generate the AST (including any prefixes that this function may have added).
  """
# TODO(mdan): Use a fast path if the definition is not multi-line.
# We could detect that the lambda is in a multi-line expression by looking
# at the surrounding code - an surrounding set of parentheses indicates a
# potential multi-line definition.

mod = inspect.getmodule(lam)
f = inspect.getsourcefile(lam)
def_line = lam.__code__.co_firstlineno

# This method is more robust that just calling inspect.getsource(mod), as it
# works in interactive shells, where getsource would fail. This is the
# same procedure followed by inspect for non-modules:
# https://github.com/python/cpython/blob/3.8/Lib/inspect.py#L772
lines = linecache.getlines(f, mod.__dict__)
source = ''.join(lines)

# Narrow down to the last node starting before our definition node.
all_nodes = parse(source, preamble_len=0, single_node=False)
search_nodes = []
for node in all_nodes:
    # Also include nodes without a line number, for safety. This is defensive -
    # we don't know whether such nodes might exist, and if they do, whether
    # they are not safe to skip.
    # TODO(mdan): Replace this check with an assertion or skip such nodes.
    if getattr(node, 'lineno', def_line) <= def_line:
        search_nodes.append(node)
    else:
        # Found a node starting past our lambda - can stop the search.
        break

  # Extract all lambda nodes from the shortlist.
lambda_nodes = []
for node in search_nodes:
    lambda_nodes.extend(
        n for n in gast.walk(node) if isinstance(n, gast.Lambda))

# Filter down to lambda nodes which span our actual lambda.
candidates = []
for ln in lambda_nodes:
    minl, maxl = MAX_SIZE, 0
    for n in gast.walk(ln):
        minl = min(minl, getattr(n, 'lineno', minl))
        lineno = getattr(n, 'lineno', maxl)
        end_lineno = getattr(n, 'end_lineno', None)
        if end_lineno is not None:
            # end_lineno is more precise, but lineno should almost always work too.
            lineno = end_lineno
        maxl = max(maxl, lineno)
    if minl <= def_line <= maxl:
        candidates.append((ln, minl, maxl))

  # Happy path: exactly one node found.
if len(candidates) == 1:
    (node, minl, maxl), = candidates  # pylint:disable=unbalanced-tuple-unpacking
    exit(_without_context(node, lines, minl, maxl))

elif not candidates:
    lambda_codes = '\n'.join([unparse(l) for l in lambda_nodes])
    raise errors.UnsupportedLanguageElementError(
        f'could not parse the source code of {lam}:'
        f' no matching AST found among candidates:\n{lambda_codes}')

# Attempt to narrow down selection by signature is multiple nodes are found.
matches = [v for v in candidates if _node_matches_argspec(v[0], lam)]
if len(matches) == 1:
    (node, minl, maxl), = matches
    exit(_without_context(node, lines, minl, maxl))

# Give up if could not narrow down to a single node.
matches = '\n'.join(
    'Match {}:\n{}\n'.format(i, unparse(node, include_encoding_marker=False))
    for i, (node, _, _) in enumerate(matches))
raise errors.UnsupportedLanguageElementError(
    f'could not parse the source code of {lam}: found multiple definitions'
    ' with identical signatures at the location. This error'
    ' may be avoided by defining each lambda on a single line and with'
    f' unique argument names. The matching definitions were:\n{matches}')
