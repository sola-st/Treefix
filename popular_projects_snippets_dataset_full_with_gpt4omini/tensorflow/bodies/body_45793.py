# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
for i in range(len(names)):
    qn = qual_names.QN(names[i])
    if qn in self.name_map:
        names[i] = str(self.name_map[qn])
exit(names)
