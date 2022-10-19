import matplotlib.pyplot as plt
import numpy as np
from zigzag import peak_valley_pivots

from ._helpers import _plot_levels


def plot_with_pivots(df, levels, zigzag_percent=1, only_good=False, path=None):
    dates = df["Datetime"]
    close_values = df['Close'].values
    
    pivots = peak_valley_pivots(close_values, zigzag_percent / 100, -zigzag_percent / 100)
    # plt.xlim(0, len(close_values))
    plt.ylim(close_values.min() * 0.995, close_values.max() * 1.005)
    plt.plot(dates, close_values, 'k-', alpha=0.9)
    plt.plot(dates[pivots != 0], close_values[pivots != 0], 'k:', alpha=0.5)

    plt.scatter(dates[pivots == 1], close_values[pivots == 1], color='g')
    plt.scatter(dates[pivots == -1], close_values[pivots == -1], color='r')

    _plot_levels(plt, levels, only_good)
    if path:
        plt.savefig(path)
    else:
        plt.show()
    plt.close()
    
# def plot_with_pivots(X, levels, zigzag_percent=1, only_good=False, path=None):
#     pivots = peak_valley_pivots(X, zigzag_percent / 100, -zigzag_percent / 100)
#     plt.xlim(0, len(X))
#     plt.ylim(X.min() * 0.995, X.max() * 1.005)
#     plt.plot(np.arange(len(X)), X, 'k-', alpha=0.9)
#     plt.plot(np.arange(len(X))[pivots != 0], X[pivots != 0], 'k:', alpha=0.5)

#     plt.scatter(np.arange(len(X))[pivots == 1], X[pivots == 1], color='g')
#     plt.scatter(np.arange(len(X))[pivots == -1], X[pivots == -1], color='r')

#     _plot_levels(plt, levels, only_good)
#     if path:
#         plt.savefig(path)
#     else:
#         plt.show()
#     plt.close()
