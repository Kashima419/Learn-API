#coding: UTF-8
import sys
import System
from cStringIO import StringIO
# redirect the sys.stdout 
sys.stdout  = StringIO()

from Autodesk.Revit.DB import Element
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
selection = [doc.GetElement(x) for x in uidoc.Selection.GetElementIds()]

#get category list => error unicode
a_list = []
for i in selection:
	a_list.append(i.Category.Name)
print(a_list,type(a_list))
print('check length',len(a_list))
print('check index 0',a_list[0] == '構造柱')
print('convert to set_list:unique',set(a_list))

# set to result to OUT variable
sys.stdout.seek(0)
OUT = sys.stdout.read().decode("unicode-escape").replace("u'","'")
# reset the sys.stdout
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
# print the result in console
print(OUT)
