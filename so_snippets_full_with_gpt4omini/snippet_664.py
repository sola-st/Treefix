# Extracted from https://stackoverflow.com/questions/9295026/how-to-remove-axis-legends-and-white-padding
    plot.axis('off')
    ax = plot.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

