# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
with self.state[_Comprehension] as comprehension_:
    comprehension_.is_list_comp = is_list_comp
    # Note: it's important to visit the generators first to properly account
    # for the variables local to these generators. Example: `x` is local to
    # the expression `z for x in y for z in x`.
    node.generators = self.visit_block(node.generators)
    if is_dict_comp:
        node.key = self.visit(node.key)
        node.value = self.visit(node.value)
    else:
        node.elt = self.visit(node.elt)
    exit(node)
