def knapsack(tasks, capacity):
    n = len(tasks)
    
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        task_time, task_priority = tasks[i - 1]
        for w in range(capacity + 1):
            if task_time <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - task_time] + task_priority)
            else:
                dp[i][w] = dp[i - 1][w]
    
    selected_tasks = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_tasks.append(i - 1)
            w -= tasks[i - 1][0]
    
    selected_tasks.reverse() 
    
    return dp[n][capacity], selected_tasks

n = int(input("Enter the number of tasks: ")) 
tasks = []

for i in range(n):
    task_time = int(input(f"Enter execution time for task {i + 1}: "))
    task_priority = int(input(f"Enter priority for task {i + 1}: "))
    tasks.append((task_time, task_priority))

capacity = int(input("Enter the total available CPU time: "))

max_priority, selected_tasks = knapsack(tasks, capacity)

print("\nMaximum Priority Achieved:", max_priority)
print("Selected Tasks (indices):", selected_tasks)
