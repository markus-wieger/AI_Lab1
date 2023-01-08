#   AI_Lab1 Documentation

1.  Task Description:

The Task was to write a Program that solves 8-Puzzles with random start states, using an A*-Algorithm with two different heuristics.
After we should compare the perfomance of those two heuristics.


2.  Software architecture:

The Software consists of three Classes: main, Puzzle and State. In the main the UI is being presented and any User input is being processed. 
The main then creates a Puzzle object based on the user input, where the solving begins. The Puzzle class creates an initial state as an array and converts the goal state into a usable array.
The heart function of the Programm is the where_to_go() function it decides based on the index of the "blank" space where the blank thile should be moved.
It also creates a new State Object containing the new array aswell as Index data, the goal array and it calculates the f_value. 
Last but not least it adds the State to our priority queue based on the f_value as instructed by the A*-Algorithm.
It does this until the first state of the priority queue matches the goal state.

More in depth documentation can be found in the code!!!

3.  Modules and Interfaces

Numpy:
We used numpy to create the gameboard as a 3 by 3 array and save the dfferent states on it.

Heapq:
Heapq is a module which makes it possible to use a heap in fashion of a priority queue.

4.  Explain Design Decisions

Heuristics:
We decided on using the manhattan and the Hamming heuristic.
The Manhattan heuristic calculates the h value based on the missplaced tiles on the gameboard.
The Hamming heuristic is a little more complex, as it measures the distance from every tile to its goal postiton. 
It forms the h value by summing up all the distances. So a lower number means shorter distance.

Datastructure:
For our Datastructure we used a priority queue which prioritizes based on the lowest f value of the added states. 


5.  Discussion and Conclusion
Experience:
At first, we had problems to start coding because we had no idea where to start. 
Once we got familiar with the topic and the heuristics, we started by creating the random initial state and performing a solvability check on it. 
Then we had to make a method that decides where the blank space could go. 
After we figured that out and wrote the core part of our program, we had to choose a fitting data structure to save the states we created. 
We picked a priority queue. Then we had to implement the two heuristics, but that wasn’t very hard. 
Last but not least, we made the Console UI as well as the Output into a text file.

Complexity:

For us the comparison between the two heuristics is not very easy because of the hamming heuristic’s poor performance. 
Depending on the initial state, one run of the hamming heuristic could take up to 20 - 60 minutes. 
Also the memory usage would increase as the depth increases, eventually leading to 12GB of RAM being used. 
That is why we could not provide 100 runs with the hamming heuristic. 
Nevertheless a table of the 7 runs we did is provided.

To see that Manhattan is way better than Hamming we don't need 100 Runs. 
In those few runs we did, it was obvious that Hamming is not feasible at depths higher than 20.
Hamming, on the other hand, has no problem even with higher depths.

Future Improvements:

Performance:
For an improvement performance wise we could add multithreading to the main method, so that multiple runs could compute at the same time instead of one after the other, depending on the number of threads available. 
There is also the possibility to implement the priority queue as a multithreaded pq which should save a lot of time during the solving process.



Feedback:
To get a better look at the solving procedure a visual feedback could be implemented, so that every step that leads to the eventual goal will be displayed visually.


Testing:
To reduce the possibility of bugs in the code and ensure its security, efficiency and      reliability, we would implement unit testing in the next phases.
