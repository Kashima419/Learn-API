# -*- coding: UTF-8 -*-
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
curview = uidoc.ActiveGraphicalView
__doc__='Create Sheet with views'
__author__ = 'Дмитро Серебріян'

views = FilteredElementCollector(doc). \
    OfCategory(BuiltInCategory.OST_Views). \
    WhereElementIsElementType().ToElements()

views = FilteredElementCollector(doc). \
    OfCategory(BuiltInCategory.OST_Views). \
    WhereElementIsNotElementType().ToElements()
schedules = FilteredElementCollector(doc). \
    OfCategory(BuiltInCategory.OST_Schedules). \
    WhereElementIsNotElementType().ToElements()
title_blocks = FilteredElementCollector(doc). \
    OfCategory(BuiltInCategory.OST_TitleBlocks). \
    WhereElementIsElementType().ToElements()

block_type_name = 'A0 metric'
schedules_name = 'Multi-Category Schedule'
view_name = 'Level 1'
for block_type in title_blocks:
    block_name = block_type. \
    get_Parameter(BuiltInParameter.SYMBOL_NAME_PARAM).AsString()
    print(block_name)
    a = 10
    if block_name == block_type_name:
    	titleblock = block_type
        break

for s in schedules:
    name_s = s.get_Parameter(BuiltInParameter.VIEW_NAME).AsString()
    if name_s == schedules_name:
    	schedule_1 = s
        break

for v in views:
    name_v = v.get_Parameter(BuiltInParameter.VIEW_NAME).AsString()
    if name_v == view_name:
        view_l = v
        break

t = Transaction(doc,'3d reinforcement')
t.Start()

newsheet = ViewSheet.Create(doc, titleblock.Id)
newsheet.Name = 'Sheet 1'
newsheet.SheetNumber = str(10)

vp1 = Viewport.Create(doc, newsheet.Id, view_l.Id, XYZ(0,0,0))
sh = ScheduleSheetInstance.Create(doc, newsheet.Id, schedule_1.Id, XYZ(0,0,0))

t.Commit()