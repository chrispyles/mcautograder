################################################
##### Utils for mcautograder Demo Notebook #####
################################################

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

def q2_plot():
    x = np.random.normal(size=1000)
    plt.hist(x, bins=25)