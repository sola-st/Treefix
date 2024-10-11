# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Prints compatibility check status and failure or warning messages.

    Prints to console without using `logging`.

    Args:
      *args: String(s) that is one of:
              [`failures`,       # all failures
               `successes`,      # all successes
               `failure_msgs`,   # failure message(s) recorded upon failure(s)
               `warning_msgs`]   # warning message(s) recorded upon warning(s)
    Raises:
      Exception: If *args not in:
                   [`failures`, `successes`, `failure_msgs`, `warning_msg`]
    """

def _format(name, arr):
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

for p_item in args:
    if p_item == "failures":
        _format("Failures", self.failures)
    elif p_item == "successes":
        _format("Successes", self.successes)
    elif p_item == "failure_msgs":
        _format("Failure Messages", self.error_msg)
    elif p_item == "warning_msgs":
        _format("Warning Messages", self.warning_msg)
    else:
        raise Exception(
            "[Error] Wrong input provided for %s." % _get_func_name())
