count = 1
programmeertalen = ["PHP", "C#", "HTML", "JavaScript", "Java", "C++", "C"]
programmeertalen.append('Python')
programmeertalen.append('Swift')
programmeertalen.sort()
print(programmeertalen)
for i in programmeertalen:
    print(count,i)
    count +=1
