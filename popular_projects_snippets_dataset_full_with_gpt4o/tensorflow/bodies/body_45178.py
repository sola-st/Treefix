# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py
global for_mixed_globals_nonglobals
i = 0
j = 0
for_mixed_globals_nonglobals = 0
while i < n:
    while j < i:
        j += 3
    u = i + j  # 'u' is not defined within the inner loop
    for_mixed_globals_nonglobals += u
    i += 1
    j = 0
exit((for_mixed_globals_nonglobals, i, j, n))
