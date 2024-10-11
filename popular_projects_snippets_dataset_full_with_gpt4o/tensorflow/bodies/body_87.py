# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Parses all compatibility specifications listed in the `.ini` config file.

    Reads and parses each and all compatibility specifications from the `.ini`
    config file by sections. It then populates appropriate dicts that represent
    each section (e.g. `self.required`) and returns a tuple of the populated
    dicts.

    Returns:
      Dict of dict
        { `required`: Dict of `Required` configs and supported versions,
          `optional`: Dict of `Optional` configs and supported versions,
          `unsupported`: Dict of `Unsupported` configs and supported versions,
          `dependency`: Dict of `Dependency` configs and supported versions }
    """
# First check if file exists. Exit on failure.
try:
    open(self.req_file, "rb")
except IOError:
    msg = "[Error] Cannot read file '%s'." % self.req_file
    logging.error(msg)
    sys.exit(1)

# Store status of parsing requirements. For local usage only.
curr_status = True

# Initialize config parser for parsing version requirements file.
parser = configparser.ConfigParser()
parser.read(self.req_file)

if not parser.sections():
    err_msg = "[Error] Empty config file. "
    err_msg += "(file = %s, " % str(self.req_file)
    err_msg += "parser sectons = %s)" % str(parser.sections())
    self.error_msg.append(err_msg)
    logging.error(err_msg)
    curr_status = False

# Each dependency dict will have the following format.
# _dict = {
#   `<config_name>` : [_Reqs()],
#   `<config_name>` : [_Reqs()]
# }
required_dict = {}
optional_dict = {}
unsupported_dict = {}
dependency_dict = {}

# Parse every config under each section defined in config file
# and populate requirement dict(s).
for section in parser.sections():
    all_configs = parser.options(section)
    for config in all_configs:
        spec = parser.get(section, config)
        # Separately manage each section:
        #   `Required`,
        #   `Optional`,
        #   `Unsupported`,
        #   `Dependency`
        # One of the sections is required.
        if section == "Dependency":
            dependency_dict[config] = []
            spec_split = spec.split(",\n")
            # First dependency item may only or not have `[` depending
            # on the indentation style in the config (.ini) file.
            # If it has `[`, then either skip or remove from string.
            if spec_split[0] == "[":
                spec_split = spec_split[1:]
            elif "[" in spec_split[0]:
                spec_split[0] = spec_split[0].replace("[", "")
            else:
                warn_msg = "[Warning] Config file format error: Missing `[`."
                warn_msg += "(section = %s, " % str(section)
                warn_msg += "config = %s)" % str(config)
                logging.warning(warn_msg)
                self.warning_msg.append(warn_msg)

            # Last dependency item may only or not have `]` depending
            # on the indentation style in the config (.ini) file.
            # If it has `[`, then either skip or remove from string.
            if spec_split[-1] == "]":
                spec_split = spec_split[:-1]
            elif "]" in spec_split[-1]:
                spec_split[-1] = spec_split[-1].replace("]", "")
            else:
                warn_msg = "[Warning] Config file format error: Missing `]`."
                warn_msg += "(section = %s, " % str(section)
                warn_msg += "config = %s)" % str(config)
                logging.warning(warn_msg)
                self.warning_msg.append(warn_msg)

            # Parse `spec_split` which is a list of all dependency rules
            # retrieved from the config file.
            # Create a _Reqs() instance for each rule and store it under
            # appropriate class dict (e.g. dependency_dict) with a proper
            # key.
            #
            # For dependency definition, it creates one _Reqs() instance each
            # for requirement and dependency. For example, it would create
            # a list in the following indexing sequence:
            #
            # [`config', <`config` _Reqs()>, `dep', <`dep` _Reqs()>]
            #
            # For example:
            # [`python`, _Reqs(), `tensorflow`, _Reqs()] for
            # `python 3.7 requires tensorflow 1.13`
            for rule in spec_split:
                # Filter out only the necessary information from `rule` string.
                spec_dict = self.filter_dependency(rule)
                # Create _Reqs() instance for each rule.
                cfg_name = spec_dict["cfg"]  # config name
                dep_name = spec_dict["cfgd"]  # dependency name
                cfg_req = self._Reqs(
                    self.convert_to_list(spec_dict["cfg_spec"], " "),
                    config=cfg_name,
                    section=section
                )
                dep_req = self._Reqs(
                    self.convert_to_list(spec_dict["cfgd_spec"], " "),
                    config=dep_name,
                    section=section
                )
                # Check status of _Reqs() initialization. If wrong formats are
                # detected from the config file, it would return `False` for
                # initialization status.
                # `<_Reqs>.get_status` returns [_initialized, _error_message]
                cfg_req_status = cfg_req.get_status
                dep_req_status = dep_req.get_status
                if not cfg_req_status[0] or not dep_req_status[0]:
                    # `<_Reqs>.get_status()[1]` returns empty upon successful init.
                    msg = "[Error] Failed to create _Reqs() instance for a "
                    msg += "dependency item. (config = %s, " % str(cfg_name)
                    msg += "dep = %s)" % str(dep_name)
                    logging.error(msg)
                    self.error_msg.append(cfg_req_status[1])
                    self.error_msg.append(dep_req_status[1])
                    curr_status = False
                    break
                else:
                    dependency_dict[config].append(
                        [cfg_name, cfg_req, dep_name, dep_req])

          # Break out of `if section == 'Dependency'` block.
            if not curr_status:
                break

        else:
            if section == "Required":
                add_to = required_dict
            elif section == "Optional":
                add_to = optional_dict
            elif section == "Unsupported":
                add_to = unsupported_dict
            else:
                msg = "[Error] Section name `%s` is not accepted." % str(section)
                msg += "Accepted section names are `Required`, `Optional`, "
                msg += "`Unsupported`, and `Dependency`."
                logging.error(msg)
                self.error_msg.append(msg)
                curr_status = False
                break

            # Need to make sure `req` argument for _Reqs() instance is always
            # a list. If not, convert to list.
            req_list = self.convert_to_list(self.filter_line(spec), " ")
            add_to[config] = self._Reqs(req_list, config=config, section=section)
        # Break out of `for config in all_configs` loop.
        if not curr_status:
            break

      # Break out of `for section in parser.sections()` loop.
    if not curr_status:
        break

return_dict = {
    "required": required_dict,
    "optional": optional_dict,
    "unsupported": unsupported_dict,
    "dependency": dependency_dict
}

exit(return_dict)
