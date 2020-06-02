from qgis.core import *
from qgis.gui import *


@qgsfunction(args="auto", group="Специальные")
def segments_between_sides_nums(sides, feature, parent):
    """
    Возвращает список с номерами сегментов полигона между самыми короткими
    сторнами.
    sides - список со списками вида (номер сегмента, длина сегмента)
    """
    sorted_sides = sorted(sides, key=lambda x: x[1])
    return list(range(int(sorted_sides[0][0]) + 1, int(sorted_sides[1][0])))
