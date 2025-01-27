# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
# GH#28150 setitem shouldn't swap the underlying data
view1 = data.view()
view2 = data[:]

data[0] = data[1]
assert view1[0] == data[1]
assert view2[0] == data[1]
