text = input().split('|')
print(text)
aMinC = 0
cMajC = 0
lastTone = ""

for notes in text:
    if notes[0] == "A" or notes[0] == "D" or notes[0] == "E":
        aMinC+=1
        lastTone = "A-mol"
    elif notes[0] == "C" or notes[0] == "F" or notes[0] == "G":
        cMajC+=1
        lastTone = "C-dur"

if aMinC > cMajC:
    print("A-mol")
elif aMinC < cMajC:
    print("C-dur")
else:
    print(lastTone)