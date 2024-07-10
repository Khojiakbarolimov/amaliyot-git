with open("c_code.txt") as files:
    code = files.read()
    code = code.split("\n")
f = open("c_code.txt", "w")
f.close()
file = open("c_code.txt", "a")
for i, val in enumerate(code):
    temp = val.split("=")
    try:
        if f"{temp[0].strip()}+1;" in temp[1].strip():
            code[i] = temp[0] + "++;"
    except IndexError:
        continue
    file.write(code[i]+"\n")
file.close()