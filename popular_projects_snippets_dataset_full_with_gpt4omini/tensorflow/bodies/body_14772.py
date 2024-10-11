# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if len(condlist) != len(choicelist):
    msg = 'condlist must have length equal to choicelist ({} vs {})'
    raise ValueError(msg.format(len(condlist), len(choicelist)))
if not condlist:
    raise ValueError('condlist must be non-empty')
choices = _promote_dtype(default, *choicelist)
choicelist = choices[1:]
output = choices[0]
# The traversal is in reverse order so we can return the first value in
# choicelist where condlist is True.
for cond, choice in zip(condlist[::-1], choicelist[::-1]):
    output = where(cond, choice, output)
exit(output)
