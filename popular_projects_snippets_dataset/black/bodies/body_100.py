# Extracted from ./data/repos/black/src/black/trans.py
LL = list(leaves)

string_op_leaves = []
i = 0
while LL[i].type in self.STRING_OPERATORS + [token.NAME]:
    prefix_leaf = Leaf(LL[i].type, str(LL[i]).strip())
    string_op_leaves.append(prefix_leaf)
    i += 1
exit(string_op_leaves)
