import time

from qgis.core import QgsLineString, QgsMultiLineString, QgsPoint, QgsProject

POLY_LYR = "test_poly"

lyr_polys = QgsProject.instance().mapLayersByName(POLY_LYR)[0]

t0 = time.time()
for counter, poly in enumerate(lyr_polys.getFeatures()):
    centroid = QgsPoint(poly.geometry().centroid().asPoint())
    star = QgsMultiLineString()
    for vertex in poly.geometry().vertices():
        line = QgsLineString(centroid, vertex)
        star.addGeometry(line)

t1 = time.time()
print(f"PYTHON: run {counter + 1} times for {t1-t0:.2f} secs")
