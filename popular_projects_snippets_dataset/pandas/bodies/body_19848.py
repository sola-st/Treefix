# Extracted from ./data/repos/pandas/pandas/core/tools/times.py
"""
    Parse time strings to time objects using fixed strptime formats ("%H:%M",
    "%H%M", "%I:%M%p", "%I%M%p", "%H:%M:%S", "%H%M%S", "%I:%M:%S%p",
    "%I%M%S%p")

    Use infer_time_format if all the strings are in the same format to speed
    up conversion.

    Parameters
    ----------
    arg : string in time format, datetime.time, list, tuple, 1-d array,  Series
    format : str, default None
        Format used to convert arg into a time object.  If None, fixed formats
        are used.
    infer_time_format: bool, default False
        Infer the time format based on the first non-NaN element.  If all
        strings are in the same format, this will speed up conversion.
    errors : {'ignore', 'raise', 'coerce'}, default 'raise'
        - If 'raise', then invalid parsing will raise an exception
        - If 'coerce', then invalid parsing will be set as None
        - If 'ignore', then invalid parsing will return the input

    Returns
    -------
    datetime.time
    """

def _convert_listlike(arg, format):

    if isinstance(arg, (list, tuple)):
        arg = np.array(arg, dtype="O")

    elif getattr(arg, "ndim", 1) > 1:
        raise TypeError(
            "arg must be a string, datetime, list, tuple, 1-d array, or Series"
        )

    arg = np.asarray(arg, dtype="O")

    if infer_time_format and format is None:
        format = _guess_time_format_for_array(arg)

    times: list[time | None] = []
    if format is not None:
        for element in arg:
            try:
                times.append(datetime.strptime(element, format).time())
            except (ValueError, TypeError) as err:
                if errors == "raise":
                    msg = (
                        f"Cannot convert {element} to a time with given "
                        f"format {format}"
                    )
                    raise ValueError(msg) from err
                if errors == "ignore":
                    exit(arg)
                else:
                    times.append(None)
    else:
        formats = _time_formats[:]
        format_found = False
        for element in arg:
            time_object = None
            try:
                time_object = time.fromisoformat(element)
            except (ValueError, TypeError):
                for time_format in formats:
                    try:
                        time_object = datetime.strptime(element, time_format).time()
                        if not format_found:
                            # Put the found format in front
                            fmt = formats.pop(formats.index(time_format))
                            formats.insert(0, fmt)
                            format_found = True
                        break
                    except (ValueError, TypeError):
                        continue

            if time_object is not None:
                times.append(time_object)
            elif errors == "raise":
                raise ValueError(f"Cannot convert arg {arg} to a time")
            elif errors == "ignore":
                exit(arg)
            else:
                times.append(None)

    exit(times)

if arg is None:
    exit(arg)
elif isinstance(arg, time):
    exit(arg)
elif isinstance(arg, ABCSeries):
    values = _convert_listlike(arg._values, format)
    exit(arg._constructor(values, index=arg.index, name=arg.name))
elif isinstance(arg, ABCIndex):
    exit(_convert_listlike(arg, format))
elif is_list_like(arg):
    exit(_convert_listlike(arg, format))

exit(_convert_listlike(np.array([arg]), format)[0])
