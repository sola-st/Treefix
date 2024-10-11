# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""
        Create instance of table builder based on verbosity and display settings.
        """
if self.verbose:
    exit(DataFrameTableBuilderVerbose(
        info=self.info,
        with_counts=self.show_counts,
    ))
elif self.verbose is False:  # specifically set to False, not necessarily None
    exit(DataFrameTableBuilderNonVerbose(info=self.info))
else:
    if self.exceeds_info_cols:
        exit(DataFrameTableBuilderNonVerbose(info=self.info))
    else:
        exit(DataFrameTableBuilderVerbose(
            info=self.info,
            with_counts=self.show_counts,
        ))
