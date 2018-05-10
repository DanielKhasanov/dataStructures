requests = [(930, 1105, 1),
            (830, 930, 2),
            (1630, 1700, 3),
            (1045, 1130, 4),
            (815, 1015, 5),
            (1530, 1645, 6),
            (1100, 1230, 7),
            (1715, 1830, 8),
            (1815, 1925, 9),
            (1210, 1320, 10),
            (945, 1045, 11),
            (1015, 1145, 12),
            (1330, 1415, 13),
            (915, 1120, 14),
            (2200, 2235, 15),
            (1515, 1630, 16),
            (1830, 1950, 17),
            (2135, 2230, 18),
            (2045, 2125, 19),
            (1740, 2015, 20)]

def driver():

    # Sort by end time
    endOrdered = sorted(requests, key=lambda x: x[1])

    # Add first finishing request
    greedyList = [endOrdered[0]]

    for i in range (len(requests)):
        # Filter out requests we cannot take
        possibleRequests = list(filter(lambda x: x[0] >= greedyList[i][1], requests))

        # Add earliest end time possible
        if possibleRequests:
            greedyList.append(min(possibleRequests, key=lambda x: x[1]))
        else:
            break

    print(" -> ".join([str(x[2]) for x in greedyList]))


if __name__ == "__main__":
    driver()
