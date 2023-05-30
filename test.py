
def updateSaves(fileName, changedVars: dict) -> None:
    path = f'{fileName}'
    with open(path, "r") as input:
        contents = input.read()
        lines = contents.split("\n")
        for i, line in enumerate(lines):
            for varName, varValue in changedVars.items():
                if varName in line:
                    lines[i] = f"{varName} = {varValue}"
                    break
    with open(path, "w") as output:    
        output.write("\n".join(lines))


updateSaves("abelha.py", {"a": "abc", "b": "def"})


