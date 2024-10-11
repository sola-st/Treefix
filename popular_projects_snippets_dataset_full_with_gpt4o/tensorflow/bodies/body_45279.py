# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
l = [1, 2, 3]
res = 0
for x in l:
    res += x
    if flag:
        break
else:
    res += 1
exit(res)
