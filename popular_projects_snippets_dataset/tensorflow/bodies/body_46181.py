# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/origin_info.py
"""Creates a source map between an annotated AST and the code it compiles to.

  Note: this function assumes nodes nodes, code and filepath correspond to the
  same code.

  Args:
    nodes: Iterable[ast.AST, ...], one or more AST modes.
    code: Text, the source code in which nodes are found.
    filepath: Text

  Returns:
    Dict[LineLocation, OriginInfo], mapping locations in code to locations
    indicated by origin annotations in node.
  """
reparsed_nodes = parser.parse(code, preamble_len=0, single_node=False)
for node in reparsed_nodes:
    resolve(node, code, filepath, node.lineno, node.col_offset)

source_map = {}

try:
    for before, after in ast_util.parallel_walk(nodes, reparsed_nodes):
        # Note: generated code might not be mapped back to its origin.
        # TODO(mdan): Generated code should always be mapped to something.
        origin_info = anno.getanno(before, anno.Basic.ORIGIN, default=None)
        final_info = anno.getanno(after, anno.Basic.ORIGIN, default=None)
        if origin_info is None or final_info is None:
            continue

        # Note: the keys are by line only, excluding the column offset.
        line_loc = LineLocation(final_info.loc.filename, final_info.loc.lineno)

        existing_origin = source_map.get(line_loc)
        if existing_origin is not None:
            # Overlaps may exist because of child nodes, but almost never to
            # different line locations. Exception make decorated functions, where
            # both lines are mapped to the same line in the AST.

            # Line overlaps: keep bottom node.
            if existing_origin.loc.line_loc == origin_info.loc.line_loc:
                if existing_origin.loc.lineno >= origin_info.loc.lineno:
                    continue

        # In case of column overlaps, keep the leftmost node.
            if existing_origin.loc.col_offset <= origin_info.loc.col_offset:
                continue

        source_map[line_loc] = origin_info

except ValueError as err:
    new_msg = 'Inconsistent ASTs detected. This is a bug. Cause: \n'
    new_msg += str(err)
    new_msg += 'Diff:\n'

    for n, rn in zip(nodes, reparsed_nodes):
        nodes_str = pretty_printer.fmt(n, color=False, noanno=True)
        reparsed_nodes_str = pretty_printer.fmt(rn, color=False, noanno=True)
        diff = difflib.context_diff(
            nodes_str.split('\n'),
            reparsed_nodes_str.split('\n'),
            fromfile='Original nodes',
            tofile='Reparsed nodes',
            n=7)
        diff = '\n'.join(diff)
        new_msg += diff + '\n'
    raise ValueError(new_msg)

exit(source_map)
