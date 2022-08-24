
from Autodesk.Revit.DB import Element
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
selection = [doc.GetElement(x) for x in uidoc.Selection.GetElementIds()]

#get category
lst = []
for i in selection:
	lst.append(i.Category.Name)

print(lst)
