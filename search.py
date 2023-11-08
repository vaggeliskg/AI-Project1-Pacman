# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
   
    stack=util.Stack()                                      # create the stack (initially empty)
    
    actions = []
    first =problem.getStartState()                          # starting node
    stack_element = {"state": first, "actions": actions}
    stack.push(stack_element)                               # stack has dictionaries containing the states and the actions required
                                                            # initially the actions are an empty list
    
    visited = []                                            # list containing the nodes that have been visited
    while not stack.isEmpty():   
        current_stack_element = stack.pop()
        if problem.isGoalState(current_stack_element["state"]):             # if goal is reached return the actions 
            return current_stack_element["actions"]                          
        if current_stack_element["state"] not in visited:
            visited.append(current_stack_element["state"])                  # if the node is unvisited mark him as visited
            
            for successor_node,successor_action, successor_cost in problem.getSuccessors(current_stack_element["state"]):   # get the successors of the
                if successor_node not in visited:                                                                           # current node calculate
                    new_actions = current_stack_element["actions"] + [successor_action]                                     # the actions needed and push the dictionary 
                    new_stack_element = {"state":successor_node, "actions": new_actions}                                    # to continue
                    stack.push(new_stack_element)                              
                                                                       
 
def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
   
    # algorithm implemented below is quite similar to the dfs algorithm but it instead uses a queue  
    # which is a FIFO structure to explore the nodes breadth first, other than that the logic behind the
    # implementation is the same
    
    queue = util.Queue()        

    actions = []
    first = problem.getStartState()     
    queue_element = {"state": first, "actions": actions}
    queue.push(queue_element)

    visited = []
    while not queue.isEmpty():
        current_queue_element = queue.pop()
        if problem.isGoalState(current_queue_element["state"]):
            return current_queue_element["actions"]
        if current_queue_element["state"] not in visited:
            visited.append(current_queue_element["state"])
            
            for successor_node,successor_action, successor_cost in problem.getSuccessors(current_queue_element["state"]):
                if successor_node not in visited:
                    new_actions = current_queue_element["actions"] + [successor_action]
                    new_queue_element = {"state":successor_node, "actions": new_actions}
                    queue.push(new_queue_element)
            

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""

    # The concept of this algorithm is the same as the bfs algorithm with the only difference being the
    # priority given to each node in order to search the node with the least total cost first

    pqueue = util.PriorityQueue()

    actions = []
    first = problem.getStartState()
    cost = 0
    pqueue_element = {"state": first, "actions": actions, "costs": cost}
    pqueue.push(pqueue_element,0)                                           # the pqueue has dictionaries that are now consisted of 3 parts
                                                                            # the nodes,the actions and the cost. By holding dictionaries in the pqueue
    visited = []                                                            # we make sure that we have an efficient way of storing and accessing  
    while not pqueue.isEmpty():                                             # the state,actions and cost  
        current_pqueue_element = pqueue.pop()     
        if problem.isGoalState(current_pqueue_element["state"]):
            return current_pqueue_element["actions"]
        if current_pqueue_element["state"] not in visited:
            visited.append(current_pqueue_element["state"])
            
            for successor_node,successor_action, successor_cost in problem.getSuccessors(current_pqueue_element["state"]):
                if successor_node not in visited:
                    new_actions = current_pqueue_element["actions"] + [successor_action]
                    new_cost = current_pqueue_element["costs"] + successor_cost
                    new_pqueue_element = {"state": successor_node, "actions": new_actions, "costs": new_cost}
                    pqueue.push(new_pqueue_element,new_cost)
   

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    # quite similar to the ucs algorithm although now we also use the heuristic cost 
    # as part of the priotiy assigned to each node, a good way of doing that is storing
    # the cost inside a dictionary as shown previously and then using it to calculate the 
    # heuristic cost which is used to provide a priority to each node 
    
    pqueue = util.PriorityQueue()

    actions = []
    first = problem.getStartState()
    cost = 0
    pqueue_element = {"state": first, "actions": actions, "costs": cost}
    pqueue.push(pqueue_element,0)

    visited = []
    while not pqueue.isEmpty():                                    
        current_pqueue_element = pqueue.pop()
        if problem.isGoalState(current_pqueue_element["state"]):
            return current_pqueue_element["actions"]
        if current_pqueue_element["state"] not in visited:
            visited.append(current_pqueue_element["state"])
            for successor_node,successor_action, successor_cost in problem.getSuccessors(current_pqueue_element["state"]):
                if successor_node not in visited:
                    new_actions = current_pqueue_element["actions"] + [successor_action]
                    new_cost = current_pqueue_element["costs"] + successor_cost
                    f_cost = new_cost + heuristic(successor_node,problem)
                    new_pqueue_element = {"state": successor_node, "actions": new_actions, "costs": new_cost}
                    pqueue.push(new_pqueue_element,f_cost)
    
    util.raiseNotDefined()


# Abbreviationsf
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
