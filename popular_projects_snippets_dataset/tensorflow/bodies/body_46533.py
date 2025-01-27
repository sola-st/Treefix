# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py

def local_fn(v):
    a = v
    exit(a)

local_fn(1)
