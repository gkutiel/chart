import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
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


def text(s: str):
    res = get_display(s)
    assert isinstance(res, str)
    return res


if __name__ == '__main__':
    print('Running main.py')

    data = pd.read_csv('data.csv')

    font_prop = fm.FontProperties(fname='hebrew.otf')

    plt.xkcd()
    plt.figure(figsize=(WIDTH_INCH, HEIGHT_INCH), dpi=DPI)
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.style.use('grayscale')

    x = data['Coffee']
    y = data['Sleep']
    plt.scatter(x, y)

    plt.xlabel(
        text('קפה'),
        font_properties=font_prop,
        fontsize=FONT_SIZE,
        labelpad=LABEL_PAD)

    plt.ylabel(
        text('שינה'),
        font_properties=font_prop,
        fontsize=FONT_SIZE,
        labelpad=LABEL_PAD)

    plt.xticks(
        range(x.min(), x.max() + 1),
        font_properties=font_prop,
        fontsize=FONT_SIZE)

    plt.yticks(
        range(y.min(), y.max() + 1),
        font_properties=font_prop,
        fontsize=FONT_SIZE)

    # plt.title(
    #     text('קפה ושינה'),
    #     font_properties=font_prop,
    #     fontsize=FONT_SIZE)

    plt.tight_layout()

    plt.savefig('plot.jpg')

    print('Done')
