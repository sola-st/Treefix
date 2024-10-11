# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Prints compatibility check results with a format.

      Args:
        name: String that is the title representing list `arr`.
        arr: List of items to be printed in a certain format.
      """
title = "### All Compatibility %s ###" % str(name)
tlen = len(title)
print("-"*tlen)
print(title)
print("-"*tlen)
print(" Total # of %s: %s\n" % (str(name), str(len(arr))))
if arr:
    for item in arr:
        detail = ""
        if isinstance(item[1], list):
            for itm in item[1]:
                detail += str(itm) + ", "
            detail = detail[:-2]
        else:
            detail = str(item[1])
        print("  %s ('%s')\n" % (str(item[0]), detail))
else:
    print("  No %s" % name)
print("\n")
