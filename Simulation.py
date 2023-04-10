#This is a part of the whole code and only has input taking and printing out the queues , I need to work on how to take the queues and working on them on how to put them in an cpu scheduling and algorithm and also I have to switch between queues of different algorithms every 10 seconds
 
queue1 = []  # high priority range (0-3) for Round Robin q t 4
queue2 = []  # medium priority range (4-6) for priority scheduling algorithm
queue3 = []  # lowest priority range (7-9) for First come first serve algorithm
 
# Taking user input from the user of process id and priority and burst time
num_processes = int(input("Enter the num of processes: "))
for i in range(num_processes):
    priority = int(input("Enter the priority of process {}: ".format(i+1)))
    burst_time = int(input("Enter the burst time of process {}: ".format(i+1)))
    process = [i+1, priority, burst_time]  # Process id , and priority and birst time are stored in this order.
    if priority >= 0 and priority <= 3:
        queue1.append(process)
    elif priority >= 4 and priority <= 6:
        queue2.append(process)
    else:
        queue3.append(process)
