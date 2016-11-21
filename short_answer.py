    """ 
1. When calculating the Big O notation for a particular algorithm, it’s necessary to consider the length of time it takes for the algorithm to run as the algorithm’s workload approaches infinity. You can think of the workload as the number of tasks required to complete a job. What determines the workload of figuring out whether your box of animal crackers contains an elephant?

    a.) Number of crackers, number of elephants, and type of search employed on the box of crackers.


2. Order the following runtimes in descending order of efficiency (that is, fastest runtimes first, slowest last) as n approaches infinity:
        a.) O(1)
        b.) O(log n)
        c.) O(n)
        d.) O(n log n)
        e.) O(n2)
        f.) O(2n) (i.e. 2 to the n-th power)


Stacks and Queues

1. In the following cases, would a stack or queue be a more appropriate data structure?
        1. The process of loading and unloading pallets onto a flatbed truck
            a.) stack
        2. Putting bottle caps on bottles of beer as they roll down an assembly line
            b.) queue
        3. Calculating the solution to this mathematical expression: 2 + (7 * 4) - (3 / 2)
            a.) stack
2. Describe two more situations where a queue would be an appropriate data structure.
    a.) Deciding who gets priority for a new work assignment based on tenure(earlier employees)
    b.) How a host seats guest at a restaurant
3. Describe two more situations where a stack would be an appropriate data structure.
    a.) A stack would be appropriate if you had to have layoffs and fire the employees with the least amount of tenure.
    b.) A stack would be useful for git commits if you wanted to go back to recent commits.  
Linked Lists

1. Given the linked list below, which are the nodes? What is the data for each node? Where 
    is the head? Where is the tail? (Please be as specific as possible — exactly which 
    parts of the diagram correspond to each part? Arrows? Boxes? Text?)
        a.) The nodes are the squares with "Apple", "Berry", and "Cherry" inside them which are the data for each node (strings). The head is pointing to the node containing "Apple". Currently the LLIST class does not have a tail specified, but if there was a tail it would be the node square containing "Cherry".


2. What’s the difference between doubly- and singly-linked lists?
    a.) Doubly-linked lists have next and previous nodes that allow upwards and downwards traversal of a list. Singly-linked do only have next. 

3. Why is it faster to append to a linked list if we keep track of the tail as an attribute?
    a.) Because we don't have to traverse the list every time we add a new node to it. 

Trees

1. Given the tree above, in what order would a Breadth First Search (BFS) algorithm visit each node until finding burrito (starting at food)? Just list the order of nodes visited; no need to recreate the state of the algorithm data in your answer.
        a.) food to italian, indian, mexican, lasagna, pizza, tikka masala, saag, burrito!


2. Given the tree above, in what order would a Depth First Search (DFS) algorithm visit each node until finding Chicago-style (starting at food)? Just list the order of nodes visited; no need to recreate the state of the algorithm data in your answer.
        b.) food to mexican, enchiladas, tacos, burrito, Indian, saag, tikka masala, Italian, pizza, Sicilian, New York-Style, Chicago-style!

3. How is a binary search tree different from other trees?
        c.) Each node can only have at most two children (a left and right child) and the right child is larger than the left child and the parent. The left child is smaller than the parent.

    """

