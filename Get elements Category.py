
from Autodesk.Revit.DB import Element
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
selection = [doc.GetElement(x) for x in uidoc.Selection.GetElementIds()]

#parameter 1
lst1 = []
for i in selection:
	lst1.append(i.Category.Name)

print(lst1)