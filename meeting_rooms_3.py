from heapq import heappify, heappush, heaapop
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        busy = []
        free = [i for i in range(n)]
        heappify(free)
        meetings = sorted(meetings)
        count = [0 for i in range(n)]
        
        # sort meetings by start time
        curr_time = meetings[0][0]
        for start, end in meetings:
            while busy and busy[0][1]<=start:
                end_time, room = heappop(busy)
                heappush(free, room)
            if free:
                room = heappop(free)
                heappush(busy, [end, room])
            else:
                end_time, room = heappop(busy)
                heappush(busy, [end_time + end - start, room])
            count[room]+=1

    return count.index(max(count))

