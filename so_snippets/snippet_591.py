# Extracted from https://stackoverflow.com/questions/21971449/how-do-i-increase-the-cell-width-of-the-jupyter-ipython-notebook-in-my-browser
.container {
    width: 99%;
    min-width: 1110px;
}   

 * important so that it also works when cell is in edit mode*/
div.cell.selected {
    border-left-width: 1px;
}

