# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py
all_types = set()
for s in elt_types:
    all_types |= s
exit({List[t] for t in all_types})
