# Примеры использования geometry generator в QGIS

- Файл проекта ```gg_examples.qgz```
- Файл с данными ```gg_examples.gpkg```
- Файл ```custom.py``` необходимо положить в папку ```~/.local/share/QGIS/QGIS3/profiles/default/python/expressions```

## Папка benchmarking

- ```create_poly_lyr.py``` - на основе точечного слоя создает полигоны с разным количеством узлов и разного "диаметра"
- ```expression_benchmarking.py``` - выполняет выражения (expressions) QGIS для построения "звездочек" для полигонов слоя
- ```python_benchmarking.py``` - строит "звездочки" для полигонов слоя на Python
