import json
import PIL
from PIL import Image 
from pathlib import Path
with open('scratchproject/project.json') as whatsinhere:
    gamecode = json.load(whatsinhere)
    if ("children" in gamecode):
        AllObjects = gamecode['children']
        ObjectAmount = len(AllObjects)
        for i in range(ObjectAmount):
            if ("scripts" in CurrentObject):
                    AllScripts = json.dumps(CurrentObject['scripts'])
                    badchar = "[],:\""
                    for character in badchar:
                        AllScripts = AllScripts.replace(character,"")
                    AllScripts = AllScripts.split()
                    ScriptAmount = len(AllScripts)
                    print (str(AllScripts))
