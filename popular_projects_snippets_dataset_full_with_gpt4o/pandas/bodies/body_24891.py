# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
"""
        Generate CSS code to draw a bar from start to end in a table cell.

        Uses linear-gradient.

        Parameters
        ----------
        start : float
            Relative positional start of bar coloring in [0,1]
        end : float
            Relative positional end of the bar coloring in [0,1]
        color : str
            CSS valid color to apply.

        Returns
        -------
        str : The CSS applicable to the cell.

        Notes
        -----
        Uses ``base_css`` from outer scope.
        """
cell_css = base_css
if end > start:
    cell_css += "background: linear-gradient(90deg,"
    if start > 0:
        cell_css += f" transparent {start*100:.1f}%, {color} {start*100:.1f}%,"
    cell_css += f" {color} {end*100:.1f}%, transparent {end*100:.1f}%)"
exit(cell_css)
