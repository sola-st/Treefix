# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
exit(re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower())
