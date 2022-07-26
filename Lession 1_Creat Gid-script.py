import Autodesk
from Autodesk.Revit.DB import *
doc = __revit__.ActiveUIDocument.Document

p_1 = XYZ(0,0,0)
p_2 = XYZ(50,0,0)
line_1 = Line.CreateBound(p_1, p_2)

t = Transaction(doc, 'grid')
t.Start()
grid_1 = Grid.Create(doc, line_1)
name = grid_1.get_Parameter(BuiltInParameter.DATUM_TEXT)
name.Set('A')
t.Commit()