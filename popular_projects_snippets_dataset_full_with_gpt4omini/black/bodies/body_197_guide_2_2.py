from typing import List, Optional # pragma: no cover
from lib2to3.pgen2 import driver # pragma: no cover
from lib2to3.pytree import Node # pragma: no cover
from lib2to3 import pytree # pragma: no cover

class MockMode: target_versions = None; preview = True # pragma: no cover
class MockFeature: PARENTHESIZED_CONTEXT_MANAGERS = 'parenthesized_context_managers'; TRAILING_COMMA_IN_CALL = 'trailing_comma_in_call'; TRAILING_COMMA_IN_DEF = 'trailing_comma_in_def' # pragma: no cover
src_contents = 'def example_function(param): return param * 2' # pragma: no cover
mode = MockMode() # pragma: no cover
versions = [] # pragma: no cover
normalize_fmt_off = lambda x, preview: None # pragma: no cover
def supports_feature(versions, feature): return True # pragma: no cover
split_line_features = {feature for feature in {MockFeature.TRAILING_COMMA_IN_CALL, MockFeature.TRAILING_COMMA_IN_DEF} if supports_feature(versions, feature)} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
src_node = lib2to3_parse(src_contents.lstrip(), mode.target_versions)
_l_(4338)
dst_blocks: List[LinesBlock] = []
_l_(4339)
if mode.target_versions:
    _l_(4343)

    versions = mode.target_versions
    _l_(4340)
else:
    future_imports = get_future_imports(src_node)
    _l_(4341)
    versions = detect_target_versions(src_node, future_imports=future_imports)
    _l_(4342)

context_manager_features = {
    feature
    for feature in {Feature.PARENTHESIZED_CONTEXT_MANAGERS}
    if supports_feature(versions, feature)
}
_l_(4344)
normalize_fmt_off(src_node, preview=mode.preview)
_l_(4345)
lines = LineGenerator(mode=mode, features=context_manager_features)
_l_(4346)
elt = EmptyLineTracker(mode=mode)
_l_(4347)
split_line_features = {
    feature
    for feature in {Feature.TRAILING_COMMA_IN_CALL, Feature.TRAILING_COMMA_IN_DEF}
    if supports_feature(versions, feature)
}
_l_(4348)
block: Optional[LinesBlock] = None
_l_(4349)
for current_line in lines.visit(src_node):
    _l_(4354)

    block = elt.maybe_empty_lines(current_line)
    _l_(4350)
    dst_blocks.append(block)
    _l_(4351)
    for line in transform_line(
        current_line, mode=mode, features=split_line_features
    ):
        _l_(4353)

        block.content_lines.append(str(line))
        _l_(4352)
if dst_blocks:
    _l_(4356)

    dst_blocks[-1].after = 0
    _l_(4355)
dst_contents = []
_l_(4357)
for block in dst_blocks:
    _l_(4359)

    dst_contents.extend(block.all_lines())
    _l_(4358)
if mode.preview and not dst_contents:
    _l_(4364)

    # Use decode_bytes to retrieve the correct source newline (CRLF or LF),
    # and check if normalized_content has more than one line
    normalized_content, _, newline = decode_bytes(src_contents.encode("utf-8"))
    _l_(4360)
    if "\n" in normalized_content:
        _l_(4362)

        aux = newline
        _l_(4361)
        exit(aux)
    aux = ""
    _l_(4363)
    exit(aux)
aux = "".join(dst_contents)
_l_(4365)
exit(aux)
