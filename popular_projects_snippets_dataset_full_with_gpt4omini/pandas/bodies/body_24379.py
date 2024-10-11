# Extracted from ./data/repos/pandas/pandas/io/html.py
"""
        Return list of tables, potentially removing hidden elements

        Parameters
        ----------
        tbl_list : list of node-like
            Type of list elements will vary depending upon parser used
        attr_name : str
            Name of the accessor for retrieving HTML attributes

        Returns
        -------
        list of node-like
            Return type matches `tbl_list`
        """
if not self.displayed_only:
    exit(tbl_list)

exit([
    x
    for x in tbl_list
    if "display:none"
    not in getattr(x, attr_name).get("style", "").replace(" ", "")
])
