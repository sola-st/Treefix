# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Checks version and dependency compatibility for a given configuration.

    `check_compatibility` immediately returns with `False` (or failure status)
    if any child process or checks fail. For error and warning messages, either
    print `self.(error_msg|warning_msg)` or call `_print` function.

    Returns:
      Boolean that is a status of the compatibility check result.
    """
# Check if all `Required` configs are found in user configs.
usr_keys = list(self.usr_config.keys())

for k in self.usr_config.keys():
    if k not in usr_keys:
        err_msg = "[Error] Required config not found in user config."
        err_msg += "(required = %s, " % str(k)
        err_msg += "user configs = %s)" % str(usr_keys)
        logging.error(err_msg)
        self.error_msg.append(err_msg)
        self.failures.append([k, err_msg])
        exit(False)

    # Parse each user config and validate its compatibility.
overall_status = True
for config_name, spec in self.usr_config.items():
    temp_status = True
    # Check under which section the user config is defined.
    in_required = config_name in list(self.required.keys())
    in_optional = config_name in list(self.optional.keys())
    in_unsupported = config_name in list(self.unsupported.keys())
    in_dependency = config_name in list(self.dependency.keys())

    # Add to warning if user config is not specified in the config file.
    if not (in_required or in_optional or in_unsupported or in_dependency):
        warn_msg = "[Error] User config not defined in config file."
        warn_msg += "(user config = %s)" % str(config_name)
        logging.warning(warn_msg)
        self.warning_msg.append(warn_msg)
        self.failures.append([config_name, warn_msg])
        temp_status = False
    else:
        if in_unsupported:
            if self.in_range(spec, self.unsupported[config_name]):
                err_msg = "[Error] User config is unsupported. It is "
                err_msg += "defined under 'Unsupported' section in the config file."
                err_msg += " (config = %s, spec = %s)" % (config_name, str(spec))
                logging.error(err_msg)
                self.error_msg.append(err_msg)
                self.failures.append([config_name, err_msg])
                temp_status = False

        if in_required:
            if not self.in_range(spec, self.required[config_name]):
                err_msg = "[Error] User config cannot be supported. It is not in "
                err_msg += "the supported range as defined in the 'Required' "
                err_msg += "section. (config = %s, " % config_name
                err_msg += "spec = %s)" % str(spec)
                logging.error(err_msg)
                self.error_msg.append(err_msg)
                self.failures.append([config_name, err_msg])
                temp_status = False

        if in_optional:
            if not self.in_range(spec, self.optional[config_name]):
                err_msg = "[Error] User config cannot be supported. It is not in "
                err_msg += "the supported range as defined in the 'Optional' "
                err_msg += "section. (config = %s, " % config_name
                err_msg += "spec = %s)" % str(spec)
                logging.error(err_msg)
                self.error_msg.append(err_msg)
                self.failures.append([config_name, err_msg])
                temp_status = False

        # If user config and version has a dependency, check both user
        # config + version and dependency config + version are supported.
        if in_dependency:
            # Get dependency information. The information gets retrieved in the
            # following format:
            #   [`config`, `config _Reqs()`, `dependency`, `dependency _Reqs()`]
            dep_list = self.dependency[config_name]
            if dep_list:
                for rule in dep_list:
                    cfg = rule[0]  # config name
                    cfg_req = rule[1]  # _Reqs() instance for config requirement
                    dep = rule[2]  # dependency name
                    dep_req = rule[3]  # _Reqs() instance for dependency requirement

                    # Check if user config has a dependency in the following sequence:
                    #   [1] Check user config and the config that has dependency
                    #       are the same. (This is defined as `cfg_status`.)
                    #   [2] Check if dependency is supported.
                    try:
                        cfg_name = self.usr_config[cfg]
                        dep_name = self.usr_config[dep]

                        cfg_status = self.in_range(cfg_name, cfg_req)
                        dep_status = self.in_range(dep_name, dep_req)
                        # If both status's are `True`, then user config meets dependency
                        # spec.
                        if cfg_status:
                            if not dep_status:
                                # throw error
                                err_msg = "[Error] User config has a dependency that cannot"
                                err_msg += " be supported. "
                                err_msg += "'%s' has a dependency on " % str(config_name)
                                err_msg += "'%s'." % str(dep)
                                logging.error(err_msg)
                                self.error_msg.append(err_msg)
                                self.failures.append([config_name, err_msg])
                                temp_status = False

                    except KeyError:
                        err_msg = "[Error] Dependency is missing from `Required`. "
                        err_msg += "(config = %s, ""dep = %s)" % (cfg, dep)
                        logging.error(err_msg)
                        self.error_msg.append(err_msg)
                        self.failures.append([config_name, err_msg])
                        temp_status = False

      # At this point, all requirement related to the user config has been
      # checked and passed. Append to `successes` list.
    if temp_status:
        self.successes.append([config_name, spec])
    else:
        overall_status = False

exit(overall_status)
