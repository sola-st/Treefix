# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
"""
        Take a conversion function and possibly recreate the frame.
        """
if filt is None:
    filt = lambda col, c: True

obj = self.obj
assert obj is not None  # for mypy

needs_new_obj = False
new_obj = {}
for i, (col, c) in enumerate(obj.items()):
    if filt(col, c):
        new_data, result = f(col, c)
        if result:
            c = new_data
            needs_new_obj = True
    new_obj[i] = c

if needs_new_obj:

    # possibly handle dup columns
    new_frame = DataFrame(new_obj, index=obj.index)
    new_frame.columns = obj.columns
    self.obj = new_frame
