data = open('data.txt').read().strip()
times, distances = data.split('\n')

times = list(map(int, times.split()[1:]))
distances = list(map(int, distances.split()[1:]))

# Calculate distances that could be achieved in said time
possibilities = [0 for i in range(len(times))]
for i in range(len(times)):
    for j in range(0, times[i]):
        curDistance = (times[i] - j) * j

        if curDistance > distances[i]:
            possibilities[i] += 1


res = 1
for possibility in possibilities:
    res *= possibility

print(res)