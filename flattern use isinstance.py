a = ["slab","footing",[2,3,5],[6,1],[9,6],3,9,["floor","doors"]]
flat = []
for i in a:
    if isinstance(i,list):
        for x in i:
            flat.append(x)
    else:
        flat.append(i)
print(flat)

#Convert input to list
def ptslist(obj1):
    if hasattr(obj1,"__iter__"): return obj1
    else: return [obj1]
