try:
    fileRead = open('111.txt', encoding = 'UTF-8')
    reader = fileRead.read()
    reader = reader.replace("\n", "")
    list = reader.split(" ")
    
    result = []
    for i in list:
        if len(i) >=7:
            result.append(i)
    
    final ='\n'.join(result)

    
except:
    print("фвйл не найден")


fileRead.close()
file2 = open("333.txt", "w", encoding="utf-8")
file2.write(final)
file2.close()