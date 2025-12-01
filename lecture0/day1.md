# Search Problem
## Lecture 0

1. agent -> any person or a medium thats acts upon environment

2. state -> current condition of environment

3. actions -> choices made on any state
    - **actions(s)** returns set of actions that can be executed on sets of state(s)

4. transition model -> a description of resultant state after performing actions on any state
    - e.g. *RESULT(a,s)* returns state resulting from action *a* performed on state *s*

5. state space -> set of all states reachable from initial state by any sequence of actions

6. goal test -> way to determine whether given sate is a goal state

7. path cost -> numerical cost (value) sociated with a given path
    -  e.g. to reach from A to B we may have 4 paths of *5km*, *6km*, *2km* and *10km*.

8. Solution -> Sequences of actions that leads initial state to goal state  

9. Optimal solution -> solution wich cost lowest path cost


10. node -> a data structure that keeps track of
    - a state 
    - parent (node that generated this node)
    - an action (ction applied to parent to get the node)
    - a path cost

 *Here to solve a search problem we need **Optimal Solution***

### Approach
- start with a frontier that contains the initial state.
- Repeat:
    - if frontier is empty there is no solution
    - remove a node from frontier 
    - if node contains goal state, return the solution
    - expand the node, add resulting node to frontier


### Revised Approach
- start with a frontier that contains the initial state.\
- start with a empty explored set
- Repeat:
    - if frontier is empty there is no solution
    - remove a node from frontier 
    - if node contains goal state, return the solution
    - add the node to explored set
    - expand the node, add resulting node to frontier if they doesn't exist in explored set or frontier


### Dept-first search(DFS) => search algorithm that always expands the deepest node in the frontier uses *stack*
### Breadth-first search(BFS) => search algorithm that always expands the shallowest node in the frontier uses *queue*

### Uninformed Search -> search strategy that uses no problem-specific knowledge

### Informed Search -> search strategy that uses problem-specific knowledge to get solution more efficiently. Types:-
1. greedy best-first search(GBFS): search algorithm that expands node closest to goal, as estimated by *heuristic function h(n)*
2. 
