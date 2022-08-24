doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
selection = [doc.GetElement(x) for x in uidoc.Selection.GetElementIds()]

for i in range(len(selection)):
	print(selection[i].Id)
