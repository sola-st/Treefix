# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference_test.py
str_name = str(name)
if str_name == 'int':
    exit(({int}, int))
exit(({type(ns[str_name])}, ns[str_name]))
