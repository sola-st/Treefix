# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/cond_basic_test.py
i = 0
l = 0
if i < n1:
    j = 0
    s = 0
    if j < n2:
        s = s * 10 + i * j
        j += 1
    else:
        s = s * 11 + i * j
        j += 2
    l = l * 1000 + s
    i += 1
else:
    j = 0
    s = 0
    if j < n2:
        s = s * 12 + i * j
        j += 3
    else:
        s = s * 13 + i * j
        j += 4
    l = l * 2000 + s
    i += 1
exit(l)
