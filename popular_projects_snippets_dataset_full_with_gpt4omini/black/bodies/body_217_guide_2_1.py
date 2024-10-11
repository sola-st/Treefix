from typing import Optional, List # pragma: no cover

class Leaf: # pragma: no cover
    def __init__(self, type, value, prefix=''): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
        self.prefix = prefix # pragma: no cover
        self.parent = None # pragma: no cover
    def remove(self): # pragma: no cover
        return 0 # pragma: no cover
class Parent: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.children = [] # pragma: no cover
    def insert_child(self, index, child): # pragma: no cover
        self.children.insert(index, child) # pragma: no cover
def list_comments(prefix, is_endmarker=False, preview=False): # pragma: no cover
    return [type('Comment', (object,), {'value': '# fmt: off', 'consumed': 0, 'newlines': 1, 'type': 'STANDALONE_COMMENT'})()] # pragma: no cover
def preceding_leaf(leaf): # pragma: no cover
    return Leaf('whitespace', 'value') # pragma: no cover
def generate_ignored_nodes(leaf, comment, preview=False): # pragma: no cover
    return [Leaf('IGNORE', 'ignored_value')] # pragma: no cover
FMT_PASS = ['# fmt: off', '# fmt: on'] # pragma: no cover
FMT_OFF = ['# fmt: off'] # pragma: no cover
FMT_SKIP = ['# fmt: skip'] # pragma: no cover
WHITESPACE = ['whitespace'] # pragma: no cover
node = type('MockNode', (object,), {'leaves': lambda self: [Leaf('mock', 'value', '    ')]})() # pragma: no cover
leaf = node.leaves()[0] # pragma: no cover
parent_node = Parent() # pragma: no cover
leaf.parent = parent_node # pragma: no cover
preview = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Convert content of a single `# fmt: off`/`# fmt: on` into a standalone comment.

    Returns True if a pair was converted.
    """
for leaf in node.leaves():
    _l_(4817)

    previous_consumed = 0
    _l_(4777)
    for comment in list_comments(leaf.prefix, is_endmarker=False, preview=preview):
        _l_(4816)

        if comment.value not in FMT_PASS:
            _l_(4780)

            previous_consumed = comment.consumed
            _l_(4778)
            continue
            _l_(4779)
        # We only want standalone comments. If there's no previous leaf or
        # the previous leaf is indentation, it's a standalone comment in
        # disguise.
        if comment.value in FMT_PASS and comment.type != STANDALONE_COMMENT:
            _l_(4787)

            prev = preceding_leaf(leaf)
            _l_(4781)
            if prev:
                _l_(4786)

                if comment.value in FMT_OFF and prev.type not in WHITESPACE:
                    _l_(4783)

                    continue
                    _l_(4782)
                if comment.value in FMT_SKIP and prev.type in WHITESPACE:
                    _l_(4785)

                    continue
                    _l_(4784)

        ignored_nodes = list(generate_ignored_nodes(leaf, comment, preview=preview))
        _l_(4788)
        if not ignored_nodes:
            _l_(4790)

            continue
            _l_(4789)

        first = ignored_nodes[0]  # Can be a container node with the `leaf`.
        _l_(4791)  # Can be a container node with the `leaf`.
        parent = first.parent
        _l_(4792)
        prefix = first.prefix
        _l_(4793)
        if comment.value in FMT_OFF:
            _l_(4795)

            first.prefix = prefix[comment.consumed :]
            _l_(4794)
        if comment.value in FMT_SKIP:
            _l_(4799)

            first.prefix = ""
            _l_(4796)
            standalone_comment_prefix = prefix
            _l_(4797)
        else:
            standalone_comment_prefix = (
                prefix[:previous_consumed] + "\n" * comment.newlines
            )
            _l_(4798)
        hidden_value = "".join(str(n) for n in ignored_nodes)
        _l_(4800)
        if comment.value in FMT_OFF:
            _l_(4802)

            hidden_value = comment.value + "\n" + hidden_value
            _l_(4801)
        if comment.value in FMT_SKIP:
            _l_(4804)

            hidden_value += "  " + comment.value
            _l_(4803)
        if hidden_value.endswith("\n"):
            _l_(4806)

            # That happens when one of the `ignored_nodes` ended with a NEWLINE
            # leaf (possibly followed by a DEDENT).
            hidden_value = hidden_value[:-1]
            _l_(4805)
        first_idx: Optional[int] = None
        _l_(4807)
        for ignored in ignored_nodes:
            _l_(4811)

            index = ignored.remove()
            _l_(4808)
            if first_idx is None:
                _l_(4810)

                first_idx = index
                _l_(4809)
        assert parent is not None, "INTERNAL ERROR: fmt: on/off handling (1)"
        _l_(4812)
        assert first_idx is not None, "INTERNAL ERROR: fmt: on/off handling (2)"
        _l_(4813)
        parent.insert_child(
            first_idx,
            Leaf(
                STANDALONE_COMMENT,
                hidden_value,
                prefix=standalone_comment_prefix,
            ),
        )
        _l_(4814)
        aux = True
        _l_(4815)
        exit(aux)
aux = False
_l_(4818)

exit(aux)
