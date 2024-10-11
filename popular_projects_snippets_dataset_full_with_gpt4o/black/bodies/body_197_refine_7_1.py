from typing import List, Optional # pragma: no cover
from lib2to3.refactor import RefactoringTool # pragma: no cover

lib2to3_parse = RefactoringTool([]).refactor_string # pragma: no cover
src_contents = type('Mock', (object,), {'lstrip': lambda self: '', 'encode': lambda self, encoding: b''})() # pragma: no cover
mode = type('Mock', (object,), {'target_versions': [], 'preview': False})() # pragma: no cover

from typing import List, Optional # pragma: no cover
from unittest.mock import Mock # pragma: no cover

lib2to3_parse = lambda contents, version: Mock() # pragma: no cover
mode = type('Mock', (object,), {'target_versions': [], 'preview': False})() # pragma: no cover
List = list # pragma: no cover
class LinesBlock:# pragma: no cover
    def __init__(self, content_lines=None):# pragma: no cover
        self.content_lines = content_lines if content_lines is not None else []# pragma: no cover
        self.after = 0# pragma: no cover
    def all_lines(self):# pragma: no cover
        return self.content_lines # pragma: no cover
class Feature:# pragma: no cover
    PARENTHESIZED_CONTEXT_MANAGERS = 'PARENTHESIZED_CONTEXT_MANAGERS'# pragma: no cover
    TRAILING_COMMA_IN_CALL = 'TRAILING_COMMA_IN_CALL'# pragma: no cover
    TRAILING_COMMA_IN_DEF = 'TRAILING_COMMA_IN_DEF' # pragma: no cover
normalize_fmt_off = lambda node, preview: None # pragma: no cover
class LineGenerator:# pragma: no cover
    def __init__(self, mode, features):# pragma: no cover
        self.mode = mode# pragma: no cover
        self.features = features# pragma: no cover
    def visit(self, node):# pragma: no cover
        yield 'example line' # pragma: no cover
class EmptyLineTracker:# pragma: no cover
    def __init__(self, mode):# pragma: no cover
        self.mode = mode# pragma: no cover
    def maybe_empty_lines(self, current_line):# pragma: no cover
        return LinesBlock([current_line]) # pragma: no cover
transform_line = lambda current_line, mode, features: [current_line] # pragma: no cover
decode_bytes = lambda src: (src.decode('utf-8').strip(), '', '\n') # pragma: no cover
supports_feature = lambda versions, feature: False # pragma: no cover

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
