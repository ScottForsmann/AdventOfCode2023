from functools import reduce

def transformIntervals(intervals, mapping):
    newIntervals = []

    i = len(mapping) - 1
    while intervals and i >= 0:
        interval = intervals.pop()

        newBegin, begin, dataRange = mapping[i]
        offset = newBegin - begin

        # Interval is after seed range, doesn't ever intersect
        if interval[0] > begin + dataRange:
            newIntervals.append(interval)

        # Interval is before, decrement i, add back interval
        elif interval[1] < begin:
            intervals.append(interval)
            i -= 1

        # Intersection
        else:
            # Find intersection, add it to newIntervals
            interStart = max(begin, interval[0])
            if interval[0] < begin:
                intervals.append([interval[0], begin - 1])
                i -= 1

            interEnd = min(begin+dataRange, interval[1])
            if interval[1] > begin + dataRange:
                intervals.append([begin + dataRange + 1, interval[1]])

            newIntervals.append([interStart + offset, interEnd + offset])


    newIntervals += intervals
    return sorted(newIntervals)


def reduceSortedIntervals(intervals):
    res = [intervals[0]]

    for i in range(1, len(intervals)):
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(intervals[i][1], res[-1][1])
        else:
            res.append(intervals[i])

    return res


def main():
    seeds, *mappings = open('day5Input.txt').read().strip().split('\n\n')
    seeds = list(map(int, seeds.split()[1:]))

    intervals = []
    for i in range(0, len(seeds), 2):
        intervals.append([seeds[i], seeds[i] + seeds[i + 1]])
    intervals.sort()

    for i in range(len(mappings)):
        mappingList = mappings[i].split('\n')
        mappingString = mappingList[1:]

        mappingList = []
        for mapping in mappingString:
            destStart, sourceStart, startRange = map(int, mapping.split(' '))
            mappingList.append([destStart, sourceStart, startRange])
        mappings[i] = mappingList

        mappings[i].sort(key = lambda x: x[1] + x[2])


    for mapping in mappings:
        intervals = reduceSortedIntervals(transformIntervals(intervals, mapping))

    print(intervals)


if __name__ == "__main__":
    main()