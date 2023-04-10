#This is a part of the whole code and only has input taking and printing out the queues , I need to work on how to take the queues and working on them on how to put them in an cpu scheduling and algorithm and also I have to switch between queues of different algorithms every 10 seconds
 
queue1 = []  # high priority range (0-3) for Round Robin t q 4
queue2 = []  # medium priority range (4-6) for priority scheduling algorithm
queue3 = []  # lowest priority range (7-9) for First come first serve algorithm
 
# Taking user input from the user of process id and priority and burst time
num_processes = int(input("Enter the num of processes ,: "))
for i in range(num_processes):
    priority = int(input("Enter the priority of process , here the processes are divided into 3 queues as per their priority{}: ".format(i+1)))
    burst_time = int(input("Enter the burst time of process {}: ".format(i+1)))
    process = [i+1, priority, burst_time]  # Process id , and priority and birst time are stored in this order.
    if priority >= 0 and priority <= 3:
        queue1.append(process)
    elif priority >= 4 and priority <= 6:
        queue2.append(process)
    else:
        queue3.append(process)
#setting tq for each queue i.e 10
quantum_time = 10
 
#there is no certain priority so we are taking queue1 as the current/starting queue
current_queue = queue1
 
# Loop until all processes are executed
total_time = 0
while queue1 or queue2 or queue3:
    # Apply Round Robin time quantum 4 for Queue 1
    if current_queue == queue1:
        if queue1:
            process = queue1.pop(0)
            print("Executing process", process[0], "from Queue 1")
            if process[2] > 4:
                process[2] -= 4
                total_time += 4
                queue2.append(process)
                print("Process", process[0], "moved to Queue 2")
            else:
                total_time += process[2]
                print("Process", process[0], "finished execution")
    # Apply priority scheduling algorithm for Queue 2
    elif current_queue == queue2:
        if queue2:
            queue2.sort(key=lambda x: x[1])
            process = queue2.pop(0)
            print("Executing process", process[0], "from Queue 2")
            total_time += process[2]
            print("Process", process[0], "finished execution")
    # Apply First come first serve algorithm for Queue 3
    elif current_queue == queue3:
        if queue3:
            process = queue3.pop(0)
            print("Executing process", process[0], "from Queue 3")
            total_time += process[2]
            print("Process", process[0], "finished execution")
 
    # Shift the CPU to the next queue after 10 seconds as it is roung robin for priority scheduling algo
    if total_time % 10 == 0:
        if current_queue == queue1:
            current_queue = queue2
        elif current_queue == queue2:
            current_queue = queue3
        else:
            current_queue = queue1
 
# Print the total time taken to execute all processes
print("Total time taken to execute all processes:", total_time)
