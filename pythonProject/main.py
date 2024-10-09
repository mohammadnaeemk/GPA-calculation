import csv
# For the average
from statistics import mean

def calculate():
    GPAlist = list()
    with open("numbers.csv", mode="r") as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            GPAlist.append((line[0] , mean(list(map(float, line[1:])))))
        csvfile.close()
    for i in GPAlist:
        print("%s , %s"  %(i[0], i[1]))
    with open("sorted.csv", mode="w", newline='') as sortedcsvfile:
        writer = csv.writer(sortedcsvfile)
        sorted_file = sorted(GPAlist ,key=lambda x: x[1], reverse=True)
        for i in sorted_file:
            writer.writerow(i)
        sortedcsvfile.close()
calculate()
print("---------------------------------------------------")

def calculate_sorted_averages():
     with open("sorted.csv", mode="r") as SortedFile:
        reader = csv.reader(SortedFile)
        for line in reader:
            print(line[0]," , ",line[1])
        SortedFile.close()

calculate_sorted_averages()
print("---------------------------------------------------")

def calculate_three_best():
    with open("sorted.csv", mode="r") as SortedFile:
        reader = csv.reader(SortedFile)
        counter = 0
        for line in reader:
            if counter == 3:
                break
            print(line[0],",",line[1])
            counter += 1
        SortedFile.close()
calculate_three_best()
print("---------------------------------------------------")
def calculate_three_worst():
    with open("sorted.csv", mode="r") as SortedFile:
        reader = csv.reader(SortedFile)
        counter = 0
        li_reader = list(reader)
        for line in  li_reader[-3:]:
            if counter == 3:
                break
            print([0],",",line[1])
            counter += 1
        SortedFile.close()
calculate_three_worst()
print("---------------------------------------------------")
def calculate_average_of_averages():
    counter,sum =0, float()
    with open("sorted.csv", mode="r") as SortedFile:
        reader = csv.reader(SortedFile)
        for line in reader:
            sum += float(line[1])
            counter +=1
        SortedFile.close()
    print("AVG is : ", sum/counter)
calculate_average_of_averages()