# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
y = 0
while x:
    x += i
    if i:
        break
else:
    y = 1
exit((x, y))
