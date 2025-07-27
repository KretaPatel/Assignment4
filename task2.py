#Writing Data from file:

file=open("output.txt","w")

data=input("entter text to write to the file")

file.write(data+"\n")

print("Data successfully written to output.txt")


file.close()


#Appending data in file:

file=open("output.txt","a")

data=input("Enter Additional textt to append:")

file.write(data+"\n")

print("data Succesfully append")

file.close()

#Readig final content of file:

file=open("output.txt","r")

read=file.read()

print("Final content of output.txt:\n"+read)

file.close()

