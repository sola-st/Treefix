# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Compare two versions and return information on which is smaller vs. larger.

  Args:
    v1: String that is a version to be compared against `v2`.
    v2: String that is a version to be compared against `v1`.

  Returns:
    Dict that stores larger version with key `larger` and smaller version with
      key `smaller`.
      e.g. {`larger`: `1.5.0`, `smaller`: `1.2.0`}

  Raises:
    RuntimeError: If asked to compare `inf` to `inf`.
  """
# Throw error is asked to compare `inf` to `inf`.
if v1 == "inf" and v2 == "inf":
    raise RuntimeError("Cannot compare `inf` to `inf`.")

rtn_dict = {"smaller": None, "larger": None}
v1_list = v1.split(".")
v2_list = v2.split(".")
# Take care of cases with infinity (arg=`inf`).
if v1_list[0] == "inf":
    v1_list[0] = str(int(v2_list[0]) + 1)
if v2_list[0] == "inf":
    v2_list[0] = str(int(v1_list[0]) + 1)

# Determine which of the two lists are longer vs. shorter.
v_long = v1_list if len(v1_list) >= len(v2_list) else v2_list
v_short = v1_list if len(v1_list) < len(v2_list) else v2_list

larger, smaller = None, None
for i, ver in enumerate(v_short, start=0):
    if int(ver) > int(v_long[i]):
        larger = _list_to_string(v_short, ".")
        smaller = _list_to_string(v_long, ".")
    elif int(ver) < int(v_long[i]):
        larger = _list_to_string(v_long, ".")
        smaller = _list_to_string(v_short, ".")
    else:
        if i == len(v_short) - 1:
            if v_long[i + 1:] == ["0"]*(len(v_long) - 1 - i):
                larger = "equal"
                smaller = "equal"
            else:
                larger = _list_to_string(v_long, ".")
                smaller = _list_to_string(v_short, ".")
        else:
            # Go to next round.
            pass

    if larger:
        break

rtn_dict["smaller"] = smaller
rtn_dict["larger"] = larger

exit(rtn_dict)
