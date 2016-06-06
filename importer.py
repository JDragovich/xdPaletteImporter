import zipfile
import json
import tempfile
import re
import os
import argparse

# parser arguments
parser = argparse.ArgumentParser()
parser.add_argument("target", help="file where color pallete is transfered to")
parser.add_argument("source", help="file where color pallete is transfered from")
parser.add_argument("-a","--append", help="file where color pallete is transfered from", action="store_true")
args = parser.parse_args()

if(os.path.isfile(args.target) and os.path.isfile(args.source)):
    # temp files system
    tmpdir = tempfile.mkdtemp()
    tempdest = tempfile.mkdtemp()
    
    ## open zip files for editing.
    source = zipfile.ZipFile(args.source,'r')
    target = zipfile.ZipFile(args.target, 'r')
    outputZip = zipfile.ZipFile(tempdest + os.path.basename(args.target), 'w')

    # extract target file to temp directory
    target.extractall(tmpdir)

    # open the target's config file for editing
    configFile = open(tmpdir + "/resources/graphics/graphicContent.agc", "r+")
    resourceFile = configFile.read()
    targetSwatchData = json.loads(resourceFile)
    
    # open source config file for reading
    sourcereSourceFile = source.read("resources/graphics/graphicContent.agc")
    sourceSwatchData = json.loads(sourcereSourceFile)   
    
    # edit target file and see what 
    if(args.append):
        for swatch in sourceSwatchData["resources"]["meta"]["ux"]["colorSwatches"]:
            targetSwatchData["resources"]["meta"]["ux"]["colorSwatches"].append(swatch)
    else:
        targetSwatchData["resources"]["meta"]["ux"]["colorSwatches"] = sourceSwatchData["resources"]["meta"]["ux"]["colorSwatches"]
    
    # overwrite target's config file with new data
    configFile.seek(0)
    configFile.write(json.dumps(targetSwatchData))
    configFile.truncate()
    configFile.close()
    outputZip.writestr("mimetype","application/vnd.adobe.sparkler.project+dcx")

    # iterively write new xd file in temp location. 
    for path in os.walk(tmpdir):
        for filePath in path[2]:
            if filePath != 'mimetype':
                fullPath = path[0]+'/'+filePath
                outputZip.write(fullPath, re.sub(tmpdir+'/', '', fullPath)) #dont know if i like string surury, but this is quick and dirty
    
    # once its edited in the item directory replace the old file (this needs refactoring if using this on windows)
    os.rename(tempdest + os.path.basename(args.target),args.target)
            
    print("done")
    
else:
    print("Either the target or source are not valid file paths")
