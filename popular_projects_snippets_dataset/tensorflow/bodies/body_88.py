# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Filters dependency compatibility rules defined in the `.ini` config file.

    Dependency specifications are defined as the following:
      `<config> <config_version> requires <dependency> <dependency_version>`
    e.g.
      `python 3.7 requires tensorflow 1.13`
      `tensorflow range(1.0.0, 1.13.1) requires gcc range(4.8, )`

    Args:
      line: String that is a dependency specification defined under `Dependency`
            section in the `.ini` config file.

    Returns:
      Dict with configuration and its dependency information.
        e.g. {`cfg`: `python`,       # configuration name
              `cfg_spec`: `3.7`,     # configuration version
              `cfgd`: `tensorflow`,  # dependency name
              `cfgd_spec`: `4.8`}    # dependency version
    """
line = line.strip("\n")
expr = r"(?P<cfg>[\S]+) (?P<cfg_spec>range\([\d\.\,\s]+\)( )?"
expr += r"(include\([\d\.\,\s]+\))?( )?(exclude\([\d\.\,\s]+\))?( )?"
expr += r"|[\d\,\.\s]+) requires (?P<cfgd>[\S]+) (?P<cfgd_spec>range"
expr += r"\([\d\.\,\s]+\)( )?(include\([\d\.\,\s]+\))?( )?"
expr += r"(exclude\([\d\.\,\s]+\))?( )?|[\d\,\.\s]+)"
r = re.match(expr, line.strip("\n"))

exit(r.groupdict())
