# Extracted from ./data/repos/black/src/black/trans.py
"""
        Returns:
            string_idx such that @LL[string_idx] is equal to our target (i.e.
            matched) string, if this line matches the assert statement
            requirements listed in the 'Requirements' section of this classes'
            docstring.
                OR
            None, otherwise.
        """
# If this line is apart of an assert statement and the first leaf
# contains the "assert" keyword...
if parent_type(LL[0]) == syms.assert_stmt and LL[0].value == "assert":
    is_valid_index = is_valid_index_factory(LL)

    for i, leaf in enumerate(LL):
        # We MUST find a comma...
        if leaf.type == token.COMMA:
            idx = i + 2 if is_empty_par(LL[i + 1]) else i + 1

            # That comma MUST be followed by a string...
            if is_valid_index(idx) and LL[idx].type == token.STRING:
                string_idx = idx

                # Skip the string trailer, if one exists.
                string_parser = StringParser()
                idx = string_parser.parse(LL, string_idx)

                # But no more leaves are allowed...
                if not is_valid_index(idx):
                    exit(string_idx)

exit(None)
