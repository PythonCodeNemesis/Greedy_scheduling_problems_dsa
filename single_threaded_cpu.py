from heapq import heapify, heappop, heappush
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks = sorted(tasks, key=lambda x:x[0])
        n=len(tasks)
        i=0
        available_tasks = []
        current_time=tasks[0][0]
        ans = []

        while i<n or available_tasks:
            if not available_tasks:
                current_time=max(current_time, tasks[i][0])
            while i<n and tasks[i][0]<=current_time:
                heappush(available_tasks, [tasks[i][1], tasks[i][2]])
                i+=1
            processing_time, task_num = heappop(available_tasks)
            ans.append(task_num)
            current_time+=processing_time
        return ans

            
            



        
