# Extracted from https://stackoverflow.com/questions/43027980/purpose-of-matplotlib-inline
    manager = _pylab_helpers.Gcf.get_fig_manager(num)
    if manager is None:
        # not relevant stuff…
        manager = new_figure_manager(
            num, figsize=figsize, dpi=dpi,
            facecolor=facecolor, edgecolor=edgecolor, frameon=frameon,
            FigureClass=FigureClass, **kwargs)


import matplotlib.pyplot as plt
from matplotlib.image import imread
# %matplotlib inline

plt.rcParams["figure.dpi"] = 200
plt.imshow(imread("path_to_your_image"))
print(plt.rcParams["figure.dpi"])

