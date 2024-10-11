# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_test.py
"""Count number of references to objects of type |typeof|."""
objs = gc.get_objects()
ref_count = 0
for o in objs:
    try:
        if isinstance(o, typeof):
            ref_count += 1
      # Certain versions of python keeps a weakref to deleted objects.
    except ReferenceError:
        pass
exit(ref_count)
