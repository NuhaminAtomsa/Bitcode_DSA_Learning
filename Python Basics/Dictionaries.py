K = int(input())
rooms = list(map(int, input().split()))

freq = {}

for room in rooms:
    if room in freq:
        freq[room] += 1
    else:
        freq[room] = 1

for room in freq:
    if freq[room] == 1:
        print(room)