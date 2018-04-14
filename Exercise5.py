#ADARSHA SACHAN
#Exercise 5 Write a Python script that reads the Iris data set in and prints the four numerical values on each row in a nice format
import csv
with open("Data/irish.csv") as f:
    for line in  f:
        j=line.format()
        j=j[:3]+"0"+ "  " + j[4:7]+"0" + "  " + j[8:11]+"0" + "  " + j[12:15]+"0"
        print(j)


# one more way csv file to read file second method
with open ("Data/irish.csv")as f:
    test= csv.reader(f)
    read=f.read()
    print(read)