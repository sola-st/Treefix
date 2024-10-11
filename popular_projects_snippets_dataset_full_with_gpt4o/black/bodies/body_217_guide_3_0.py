from typing import Optional, List # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, type, value, prefix=''): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
        self.prefix = prefix # pragma: no cover
        self.parent = None # pragma: no cover
    def remove(self): # pragma: no cover
        return 0  # Mock implementation # pragma: no cover
 # pragma: no cover
class Node: # pragma: no cover
    def __init__(self, leaves: List[Leaf]): # pragma: no cover
        self._leaves = leaves # pragma: no cover
    def leaves(self): # pragma: no cover
        return self._leaves # pragma: no cover
    def insert_child(self, index: int, child: Leaf): # pragma: no cover
        print(f'Inserted child at index {index}: {child}')  # Mock implementation # pragma: no cover
 # pragma: no cover
class Comment: # pragma: no cover
    def __init__(self, value, consumed=0, newlines=0, type='COMMENT'): # pragma: no cover
        self.value = value # pragma: no cover
        self.consumed = consumed # pragma: no cover
        self.newlines = newlines # pragma: no cover
        self.type = type # pragma: no cover
 # pragma: no cover
def list_comments(prefix, is_endmarker, preview): # pragma: no cover
    return [ # pragma: no cover
        Comment('# fmt: off', 10, 1, 'COMMENT'), # pragma: no cover
        Comment('# fmt: skip', 15, 1, 'COMMENT')  # This will trigger an uncovered path # pragma: no cover
    ] # pragma: no cover
 # pragma: no cover
def preceding_leaf(leaf): # pragma: no cover
    return Leaf(type='WHITESPACE', value=' ', prefix=' ') # pragma: no cover
 # pragma: no cover
def generate_ignored_nodes(leaf, comment, preview): # pragma: no cover
    ignored_leaf = Leaf('COMMENT', 'ignored_value', '') # pragma: no cover
    ignored_leaf.parent = leaf # pragma: no cover
    return [ignored_leaf] # pragma: no cover
 # pragma: no cover
FMT_PASS = {'# fmt: off', '# fmt: on', '# fmt: skip'} # pragma: no cover
FMT_OFF = {'# fmt: off'} # pragma: no cover
FMT_SKIP = {'# fmt: skip'} # pragma: no cover
STANDALONE_COMMENT = 'COMMENT' # pragma: no cover
WHITESPACE = {'WHITESPACE'} # pragma: no cover
node = Node([Leaf(type='COMMENT', value='# fmt: off', prefix=' '), Leaf(type='CODE', value='some_code', prefix=' '), Leaf(type='COMMENT', value='# fmt: skip', prefix=' ')]) # pragma: no cover
preview = False # pragma: no cover
aux = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Convert content of a single `# fmt: off`/`# fmt: on` into a standalone comment.

    Returns True if a pair was converted.
    """
for leaf in node.leaves():
    _l_(16470)

    previous_consumed = 0
    _l_(16430)
    for comment in list_comments(leaf.prefix, is_endmarker=False, preview=preview):
        _l_(16469)

        if comment.value not in FMT_PASS:
            _l_(16433)

            previous_consumed = comment.consumed
            _l_(16431)
            continue
            _l_(16432)
        # We only want standalone comments. If there's no previous leaf or
        # the previous leaf is indentation, it's a standalone comment in
        # disguise.
        if comment.value in FMT_PASS and comment.type != STANDALONE_COMMENT:
            _l_(16440)

            prev = preceding_leaf(leaf)
            _l_(16434)
            if prev:
                _l_(16439)

                if comment.value in FMT_OFF and prev.type not in WHITESPACE:
                    _l_(16436)

                    continue
                    _l_(16435)
                if comment.value in FMT_SKIP and prev.type in WHITESPACE:
                    _l_(16438)

                    continue
                    _l_(16437)

        ignored_nodes = list(generate_ignored_nodes(leaf, comment, preview=preview))
        _l_(16441)
        if not ignored_nodes:
            _l_(16443)

            continue
            _l_(16442)

        first = ignored_nodes[0]  # Can be a container node with the `leaf`.
        _l_(16444)  # Can be a container node with the `leaf`.
        parent = first.parent
        _l_(16445)
        prefix = first.prefix
        _l_(16446)
        if comment.value in FMT_OFF:
            _l_(16448)

            first.prefix = prefix[comment.consumed :]
            _l_(16447)
        if comment.value in FMT_SKIP:
            _l_(16452)

            first.prefix = ""
            _l_(16449)
            standalone_comment_prefix = prefix
            _l_(16450)
        else:
            standalone_comment_prefix = (
                prefix[:previous_consumed] + "\n" * comment.newlines
            )
            _l_(16451)
        hidden_value = "".join(str(n) for n in ignored_nodes)
        _l_(16453)
        if comment.value in FMT_OFF:
            _l_(16455)

            hidden_value = comment.value + "\n" + hidden_value
            _l_(16454)
        if comment.value in FMT_SKIP:
            _l_(16457)

            hidden_value += "  " + comment.value
            _l_(16456)
        if hidden_value.endswith("\n"):
            _l_(16459)

            # That happens when one of the `ignored_nodes` ended with a NEWLINE
            # leaf (possibly followed by a DEDENT).
            hidden_value = hidden_value[:-1]
            _l_(16458)
        first_idx: Optional[int] = None
        _l_(16460)
        for ignored in ignored_nodes:
            _l_(16464)

            index = ignored.remove()
            _l_(16461)
            if first_idx is None:
                _l_(16463)

                first_idx = index
                _l_(16462)
        assert parent is not None, "INTERNAL ERROR: fmt: on/off handling (1)"
        _l_(16465)
        assert first_idx is not None, "INTERNAL ERROR: fmt: on/off handling (2)"
        _l_(16466)
        parent.insert_child(
            first_idx,
            Leaf(
                STANDALONE_COMMENT,
                hidden_value,
                prefix=standalone_comment_prefix,
            ),
        )
        _l_(16467)
        aux = True
        _l_(16468)
        exit(aux)
aux = False
_l_(16471)

exit(aux)
