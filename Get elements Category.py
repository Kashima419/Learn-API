from Autodesk.Revit.DB import Element
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
selection = [doc.GetElement(x) for x in uidoc.Selection.GetElementIds()]


#get category
for i in selection:
	print(i.Category.Name)
print('=================================================================')

#get category list => error unicode
category_name = []
for i in selection:
	category_name.append(i.Category.Name)
print(category_name)

print('=================================================================')
#get category set
for i in set(category_name):
	print(i)
