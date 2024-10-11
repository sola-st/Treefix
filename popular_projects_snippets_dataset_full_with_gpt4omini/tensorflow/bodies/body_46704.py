# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
for i in a:
    for j in i:
        x = i
        y += x
        z = j
exit((y, z))
