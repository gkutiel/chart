
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bidi.algorithm import get_display

FONT_SIZE = 18
ASPECT_RATIO = 16 / 9
WIDTH_PXL = 800
HEIGHT_PXL = int(WIDTH_PXL / ASPECT_RATIO)
DPI = 100
WIDTH_INCH = WIDTH_PXL / DPI
HEIGHT_INCH = HEIGHT_PXL / DPI
LABEL_PAD = 10
DATA_SIZE = 15


def text(s: str):
    res = get_display(s)
    assert isinstance(res, str)
    return res


def ticks(series, up=1):
    return range(int(series.min()), int(series.max() + up))


if __name__ == '__main__':
    print('Running main.py')

    np.random.seed(42)
    x = np.random.randint(1, 12, size=DATA_SIZE)
    x = x.astype(float)
    x /= 2
    noise = np.random.normal(0, 0.5, size=DATA_SIZE)
    y = 9 - 1 * x + noise

    data = pd.DataFrame({'Coffee': x, 'Sleep': y})

    # data = pd.read_csv('data.csv')

    font_prop = fm.FontProperties(fname='hebrew.otf')

    plt.xkcd()
    plt.figure(figsize=(WIDTH_INCH, HEIGHT_INCH), dpi=DPI)
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.style.use('grayscale')

    x = data['Coffee']
    y = data['Sleep']

    plt.scatter(x, y, marker='x', color='#444')

    plt.xlabel(
        text('כוסות קפה'),
        font_properties=font_prop,
        fontsize=FONT_SIZE,
        labelpad=LABEL_PAD)

    plt.ylabel(
        text('שעות שינה'),
        font_properties=font_prop,
        fontsize=FONT_SIZE,
        labelpad=LABEL_PAD)

    plt.xticks(
        ticks(x),
        font_properties=font_prop,
        fontsize=FONT_SIZE)

    plt.yticks(
        ticks(y, up=2),
        font_properties=font_prop,
        fontsize=FONT_SIZE)

    # plt.title(
    #     text('קפה ושינה'),
    #     font_properties=font_prop,
    #     fontsize=FONT_SIZE)

    plt.tight_layout()

    plt.savefig('plot.jpg')

    print('Done')
