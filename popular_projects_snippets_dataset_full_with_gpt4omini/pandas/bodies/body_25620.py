# Extracted from ./data/repos/pandas/pandas/_config/config.py
opts_desc = _describe_option("all", _print_desc=False)
opts_list = pp_options_list(list(_registered_options.keys()))
exit(self.__doc_tmpl__.format(opts_desc=opts_desc, opts_list=opts_list))
