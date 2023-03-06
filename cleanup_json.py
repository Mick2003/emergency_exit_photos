json = ""

def readText(path_to_json):
    
        with open(path_to_json, "r") as f:
            return f.read()

# Remove array(' ')
def removeArray(json):
    return json.replace("array(", "").replace(")", "")

# Replace all ' with "
def replaceQuotes(json):
    return json.replace("'", '"')


json = readText("boxes.json")
json = removeArray(json)
json = replaceQuotes(json)

print(json)