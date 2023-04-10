<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<h3 align="center">Operating System Simulation Based Assignment Report</h3>

  <p align="center">
    Simulation Based Report
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the Report »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Code</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Report

This project based on the report for the simulation based project on operating systems priority based scheduling queue.


Question 6
Write a program for multilevel queue scheduling algorithm. There must be three queues
generated. There must be specific range of priority associated with every queue. Now prompt
the user to enter number of processes along with their priority and burst time. Each process
must occupy the respective queue with specific priority range according to its priority. Apply
Round Robin algorithm with quantum time 4 on queue with highest priority range. Apply
priority scheduling algorithm on the queue with medium range of priority and First come first
serve algorithm on the queue with lowest range of priority. Each and every queue should get
a quantum time of 10 seconds. CPU will keep on shifting between queues after every 10
seconds.

Approach

Multilevel Queue Scheduling Algorithm Implementation

In this implementation, we have three queues with different priority levels and scheduling algorithms:

Queue 1: Highest priority range (0-3) - Round Robin algorithm with quantum time 4
Queue 2: Medium priority range (4-6) - Priority scheduling algorithm
Queue 3: Lowest priority range (7-9) - First come first serve algorithm


Code Explanation:

At First we are Defining three empty lists representing the queues for each priority range
Prompt the user to input the number of processes.
Loop through each process, prompting the user for its priority and burst time.
Based on the priority, assign the process to its respective queue.
Set a quantum time of 10 seconds for each queue.
Initialize the current_queue variable to queue1.
Create a while loop to execute the processes in each queue until all the queues are empty.
If the current_queue is queue1, execute the Round Robin algorithm with quantum time 4. Processes are executed for 4 units of time and then moved to queue2 if they have remaining burst time.
If the current_queue is queue2, execute the Priority scheduling algorithm. Sort the queue based on priority and execute the process with the highest priority.
If the current_queue is queue3, execute the First come first serve algorithm. Execute the processes in the order they appear in the queue.
Every 10 seconds, shift the CPU to the next queue.
Calculate and display the total time taken to execute all processes.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the Branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request



<!-- CONTACT -->
## Contact



Project Link: [https://github.com/hacktronicsraj/316-Simulation-Based-Assignment](https://github.com/hacktronicsraj/316-Simulation-Based-Assignment)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



