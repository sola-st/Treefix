# Extracted from https://stackoverflow.com/questions/432842/how-do-you-get-the-logical-xor-of-two-variables-in-python
%timeit  (not a) ^  (not b)   # 47 ns
%timeit  (not a) != (not b)   # 44.7 ns
%timeit truth(a) != truth(b)  # 116 ns
%timeit  bool(a) != bool(b)   # 190 ns

