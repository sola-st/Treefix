# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_scoping_test.py
s = 0
for i in l:
    if i == l[0]:
        x = 0
    else:
        x += 1
    s = s * 10 + x
exit(s)
