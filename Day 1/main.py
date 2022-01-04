import sys

with open("input.txt", "r") as f:
	measurements = f.readlines()
	measurements = list(map(int, measurements))


# Part 1
if sys.argv[1] == "1":

    lastMeasurement = measurements[0]
    increasedCount = 0

    for m in measurements:
        if m == lastMeasurement:
            continue
        if m > lastMeasurement:
            increasedCount += 1

        lastMeasurement = m

    print(increasedCount)


# Part 2
if sys.argv[1] == "2":

    lastTriplet = measurements[0] + measurements[1] + measurements[2]
    increasedCount = 0

    for index in range(0,len(measurements)-2):
        currentTriplet = measurements[index] + measurements[index+1] + measurements[index+2]

        if currentTriplet > lastTriplet:
            increasedCount += 1

        lastTriplet = currentTriplet

    print(increasedCount)
