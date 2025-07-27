
try:

    file = open("sample.txt", "r")
    read1=file.readline()
    print("Line1:",read1)

    read2=file.readline()
    print("Line2: ",read2)

    file.close()
except FileNotFoundError:
        print("Error:The file 'sample.txt' was not found")

#finally:
    #print("The code is being executed")