from qgis.core import (
    QgsExpression,
    QgsExpressionContext,
    QgsFeature,
    QgsProject,
    edit,
)

SRC_POINTS_LYR = "test_points"
DST_POLY_LYR = "test_poly"

EXPRESSION = """
make_regular_polygon(
    $geometry,
    project(
        $geometry,
        rand(5000, 30000),
        0
    ),
    rand(3,20)
)
"""

lyr_points = QgsProject.instance().mapLayersByName(SRC_POINTS_LYR)[0]
lyr_polys = QgsProject.instance().mapLayersByName(DST_POLY_LYR)[0]

with edit(lyr_polys):
    for point in lyr_points.getFeatures():
        exp = QgsExpression(EXPRESSION)
        context = QgsExpressionContext()
        context.setFeature(point)
        new_poly = QgsFeature(lyr_polys.fields())
        new_poly.setGeometry(exp.evaluate(context))
        lyr_polys.addFeature(new_poly)
