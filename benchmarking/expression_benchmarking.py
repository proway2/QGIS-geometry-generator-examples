import time

from qgis.core import QgsExpression, QgsExpressionContext, QgsProject

POLY_LYR = "test_poly"

EXPRESSION = """
collect_geometries(
    array_foreach(
        generate_series(1, num_points($geometry)),
        make_line(
            centroid($geometry),
            point_n($geometry, @element)
        )
    )
)
"""

lyr_polys = QgsProject.instance().mapLayersByName(POLY_LYR)[0]

t0 = time.time()
for counter, poly in enumerate(lyr_polys.getFeatures()):
    exp = QgsExpression(EXPRESSION)
    context = QgsExpressionContext()
    context.setFeature(poly)
    star = exp.evaluate(context)

t1 = time.time()
print(f"EXPRESSIONS: run {counter + 1} times for {t1-t0:.2f} secs")
