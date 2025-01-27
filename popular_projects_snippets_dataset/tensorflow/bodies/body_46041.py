# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/codegen.py
op = CompareSampler().sample()()
exit(gast.Compare(self.generate_Name(), [op], [self.generate_Name()]))
