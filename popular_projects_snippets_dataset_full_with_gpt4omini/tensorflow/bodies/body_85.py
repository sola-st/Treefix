# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Parses a requirement and stores information.

      `self.req` _initialized in `__init__` is called for retrieving the
      requirement.

      A requirement can come in two forms:
        [1] String that includes `range` indicating range syntax for defining
            a requirement.
              e.g. `range(1.0, 2.0) include(3.0) exclude(1.5)`
        [2] List that includes individual supported versions or items.
              e.g. [`1.0`, `3.0`, `7.1`]

      For a list type requirement, it directly stores the list to
      `self.include`.

      Call `get_status` for checking the status of the parsing. This function
      sets `self._initialized` to `False` and immediately returns with an error
      message upon encountering a failure. It sets `self._initialized` to `True`
      and returns without an error message upon success.
      """
# Regex expression for filtering requirement line. Please refer
# to docstring above for more information.
expr = r"(range\()?([\d\.\,\s]+)(\))?( )?(include\()?"
expr += r"([\d\.\,\s]+)?(\))?( )?(exclude\()?([\d\.\,\s]+)?(\))?"

# Check that arg `req` is not empty.
if not self.req:
    err_msg = "[Error] Requirement is missing. "
    err_msg += "(section = %s, " % str(self._section)
    err_msg += "config = %s, req = %s)" % (str(self.config), str(self.req))
    logging.error(err_msg)
    self._initialized = False
    self._error_message.append(err_msg)

    exit()

# For requirement given in format with `range`. For example:
# python = [range(3.3, 3.7) include(2.7)] as opposed to
# python = [2.7, 3.3, 3.4, 3.5, 3.6, 3.7]
if "range" in self.req[0]:
    self._req_type = "range"
    match = re.match(expr, self.req[0])
    if not match:
        err_msg = "[Error] Encountered issue when parsing the requirement."
        err_msg += " (req = %s, match = %s)" % (str(self.req), str(match))
        logging.error(err_msg)
        self._initialized = False
        self._error_message.append(err_msg)

        exit()
    else:
        match_grp = match.groups()
        match_size = len(match_grp)
        for i, m in enumerate(match_grp[0:match_size-1], start=0):
            # Get next index. For example:
            # |    idx     |  next_idx  |
            # +------------+------------+
            # |  `range(`  | `1.1, 1.5` |
            # | `exclude(` | `1.1, 1.5` |
            # | `include(` | `1.1, 1.5` |
            next_match = match_grp[i + 1]

            if m not in ["", None, " ", ")"]:
                if "range" in m:
                    # Check that the range definition contains only one comma.
                    # If more than one comma, then there is format error with the
                    # requirement config file.
                    comma_count = next_match.count(",")
                    if comma_count > 1 or comma_count == 0:
                        err_msg = "[Error] Found zero or more than one comma in range"
                        err_msg += " definition. (req = %s, " % str(self.req)
                        err_msg += "match = %s)" % str(next_match)
                        logging.error(err_msg)
                        self._initialized = False
                        self._error_message.append(err_msg)

                        exit()

                    # Remove empty space in range and separate min, max by
                    # comma. (e.g. `1.0, 2.0` => `1.0,2.0` => [`1.0`, `2.0`])
                    min_max = next_match.replace(" ", "").split(",")

                    # Explicitly define min and max values.
                    # If min_max = ['', ''], then `range(, )` was provided as
                    # req, which is equivalent to `include all versions`.
                    if not min_max[0]:
                        min_max[0] = "0"

                    if not min_max[1]:
                        min_max[1] = "inf"

                    self.range = min_max
                if "exclude" in m:
                    self.exclude = next_match.replace(" ", "").split(",")

                if "include" in m:
                    self.include = next_match.replace(" ", "").split(",")

                self._initialized = True

      # For requirement given in format without a `range`. For example:
      # python = [2.7, 3.3, 3.4, 3.5, 3.6, 3.7] as opposed to
      # python = [range(3.3, 3.7) include(2.7)]
else:
    self._req_type = "no_range"
    # Requirement (self.req) should be a list.
    if not isinstance(self.req, list):
        err_msg = "[Error] Requirement is not a list."
        err_msg += "(req = %s, " % str(self.req)
        err_msg += "type(req) = %s)" % str(type(self.req))
        logging.error(err_msg)
        self._initialized = False
        self._error_message.append(err_msg)
    else:
        self.include = self.req
        self._initialized = True

exit()
