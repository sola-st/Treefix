# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
first_inner = template.make_template("i1", _inner_template)
second_inner = template.make_template("i2", _inner_template)
v1 = first_inner()
v2 = second_inner()
v3 = second_inner()
exit(((first_inner, second_inner), (v1, v2, v3)))
