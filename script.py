import sys
import json

query = sys.argv[1]

warpFile = open('/Users/jannis/.warprc', 'r+')
warpPoints = warpFile.readlines()
warps = {}
for w in warpPoints:
    w1 = w.split(":")[0]
    w2 = w.split(":")[1][:-1]
    warps[w1] = w2

result = {"items":[]}
for key,val in warps.items():
    if(len(query) >= 1):
        if not query.lower() in key.lower():
            continue
    result["items"].append({
        "uid":key,
        "type":"file",
        "title":key,
        "subtitle":val,
        "arg": val,
        "autocomplete": key,
           "icon": {
                "type": "fileicon",
                "path": val
            }
})

rVal = json.dumps(result)
warpFile.close()
sys.stdout.write(rVal)
