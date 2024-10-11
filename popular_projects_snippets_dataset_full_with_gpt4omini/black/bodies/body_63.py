# Extracted from ./data/repos/black/src/black/trans.py
"""
        Yields:
            * Ok(new_line) where new_line is the new transformed line.
                OR
            * Err(CannotTransform) if the transformation failed for some reason. The
            `do_match(...)` template method should usually be used to reject
            the form of the given Line, but in some cases it is difficult to
            know whether or not a Line meets the StringTransformer's
            requirements until the transformation is already midway.

        Side Effects:
            This method should NOT mutate @line directly, but it MAY mutate the
            Line's underlying Node structure. (WARNING: If the underlying Node
            structure IS altered, then this method should NOT be allowed to
            yield an CannotTransform after that point.)
        """
