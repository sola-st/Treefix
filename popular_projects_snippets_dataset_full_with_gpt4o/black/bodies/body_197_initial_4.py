from typing import List, Optional # pragma: no cover

lib2to3_parse = lambda x, mode: Parse() # pragma: no cover
src_contents = 'example source code' # pragma: no cover
mode = type('MockMode', (object,), {'target_versions': ['3.6'], 'preview': True})() # pragma: no cover
List = list # pragma: no cover
LinesBlock = type('MockLinesBlock', (object,), {'__init__': lambda self: setattr(self, 'content_lines', []), 'all_lines': lambda self: []}) # pragma: no cover
Feature = type('MockFeature', (object,), {'PARENTHESIZED_CONTEXT_MANAGERS': 'Feature1', 'TRAILING_COMMA_IN_CALL': 'Feature2', 'TRAILING_COMMA_IN_DEF': 'Feature3'})() # pragma: no cover
normalize_fmt_off = lambda src_node, preview: None # pragma: no cover
LineGenerator = type('MockLineGenerator', (object,), {'__init__': lambda self, mode, features: None, 'visit': lambda self, src_node: []}) # pragma: no cover
EmptyLineTracker = type('MockEmptyLineTracker', (object,), {'__init__': lambda self, mode: None, 'maybe_empty_lines': lambda self, current_line: LinesBlock()}) # pragma: no cover
Optional = lambda x: x # pragma: no cover
transform_line = lambda current_line, mode, features: [current_line] # pragma: no cover
decode_bytes = lambda x: (x.decode('utf-8'), None, '\n') # pragma: no cover
supports_feature = lambda versions, feature: True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
src_node = lib2to3_parse(src_contents.lstrip(), mode.target_versions)
_l_(16122)
dst_blocks: List[LinesBlock] = []
_l_(16123)
if mode.target_versions:
    _l_(16127)

    versions = mode.target_versions
    _l_(16124)
else:
    future_imports = get_future_imports(src_node)
    _l_(16125)
    versions = detect_target_versions(src_node, future_imports=future_imports)
    _l_(16126)

context_manager_features = {
    feature
    for feature in {Feature.PARENTHESIZED_CONTEXT_MANAGERS}
    if supports_feature(versions, feature)
}
_l_(16128)
normalize_fmt_off(src_node, preview=mode.preview)
_l_(16129)
lines = LineGenerator(mode=mode, features=context_manager_features)
_l_(16130)
elt = EmptyLineTracker(mode=mode)
_l_(16131)
split_line_features = {
    feature
    for feature in {Feature.TRAILING_COMMA_IN_CALL, Feature.TRAILING_COMMA_IN_DEF}
    if supports_feature(versions, feature)
}
_l_(16132)
block: Optional[LinesBlock] = None
_l_(16133)
for current_line in lines.visit(src_node):
    _l_(16138)

    block = elt.maybe_empty_lines(current_line)
    _l_(16134)
    dst_blocks.append(block)
    _l_(16135)
    for line in transform_line(
        current_line, mode=mode, features=split_line_features
    ):
        _l_(16137)

        block.content_lines.append(str(line))
        _l_(16136)
if dst_blocks:
    _l_(16140)

    dst_blocks[-1].after = 0
    _l_(16139)
dst_contents = []
_l_(16141)
for block in dst_blocks:
    _l_(16143)

    dst_contents.extend(block.all_lines())
    _l_(16142)
if mode.preview and not dst_contents:
    _l_(16148)

    # Use decode_bytes to retrieve the correct source newline (CRLF or LF),
    # and check if normalized_content has more than one line
    normalized_content, _, newline = decode_bytes(src_contents.encode("utf-8"))
    _l_(16144)
    if "\n" in normalized_content:
        _l_(16146)

        aux = newline
        _l_(16145)
        exit(aux)
    aux = ""
    _l_(16147)
    exit(aux)
aux = "".join(dst_contents)
_l_(16149)
exit(aux)
