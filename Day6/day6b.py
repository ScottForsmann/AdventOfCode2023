from math import ceil, floor

data = open('data.txt').read().strip()
times, distances = data.split('\n')

time = int(''.join(list(times.split()[1:])))
distance = int(''.join(list(distances.split()[1:])))

# Calculate distances that could be achieved in said time with binary searches
lowerBound = (time - (time ** 2 - 4 * distance) ** .5) / 2
upperBound = (time + (time ** 2 - 4 * distance) ** .5) / 2

if upperBound == int(upperBound):
    upperBound -= 1
else:
    upperBound = floor(upperBound)

if lowerBound == int(lowerBound):
    lowerBound += 1
else:
    lowerBound = ceil(lowerBound)

print(upperBound - lowerBound + 1)