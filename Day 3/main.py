import sys

with open("input.txt", "r") as f:
#with open("example.txt", "r") as f:
	numbersList = f.readlines()


# Part 1
if sys.argv[1] == "1":
    ones = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0 }
    zeroes = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0 }

    for number in numbersList:
        for i in range(0,12):
            if number[i] == "0":
                zeroes[i] += 1
            if number[i] == "1":
                ones[i] += 1

    gamma = ""
    epsilon = ""
    for i in range(0,12):
        if ones[i] > zeroes[i]:
            gamma += "1"
            epsilon += "0"
        if zeroes[i] > ones[i]:
            gamma += "0"
            epsilon += "1"
    
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    
    print(gamma*epsilon)


# Part 2
if sys.argv[1] == "2":


    oxList = numbersList
    co2List = numbersList
    for i in range(0,12):
        zeroes = 0
        ones = 0

        zList = []
        oList = []

        # Oxygen
        for line in oxList:
            if len(oxList) == 1:
                break

            if line[i] == "0":
                zeroes += 1
                zList.append(line)
                continue
            ones += 1
            oList.append(line)

        if len(oxList) != 1:
            if ones >= zeroes:
                oxList = oList
            else:
                oxList = zList

        zList = []
        oList = []

        #####################

        zeroes = 0
        ones = 0

        # CO2
        for line in co2List:
            if len(co2List) == 1:
                break

            if line[i] == "0":
                zeroes += 1
                zList.append(line)
                continue
            ones += 1
            oList.append(line)
        if len(co2List) != 1:
            if ones < zeroes:
                co2List = oList
            else:
                co2List = zList
        zList = []
        oList = []
    
    oxygen = int(oxList[0],2)
    co2 = int(co2List[0],2)
    print("Oxygen")
    print(oxList)
    print(oxygen)
    print()
    print("CO2")
    print(co2List)
    print(co2)
    print()
    print("Life support")
    print(oxygen*co2)
