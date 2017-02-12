"""
# Copyright Nick Cheng, 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from salboard import SALboard
from salbnode import SALBnode

# Add your functions here.

def salb2salbLL(salb):
    # This is where I get the number of squares
    NumOfSquares = salb.numSquares
    # This is a dictionary which contains the snakes and ladders positions
    Snadders = salb.snadders
    # Create the head
    head = SALBnode()
    # In the beginning the head and the tail are one
    tail = head  
    # Loop one less than the total number of squares (since we already
    # created one)
    for i in range(1, NumOfSquares):
        # Create a new node
        new_node = SALBnode()
        # Make the previous node point to the new node
        tail.next = new_node
        # Make the new node the tail
        tail = new_node
    # Make the linked list circular
    tail.next = head
    # Iterate through the items in the dictionary
    for start, finish in Snadders.items():
        # Create the node for the source        
        startNode = head
        # Loop through the nodes till you get to the index
        for i in range(start-1):
            startNode = startNode.next
        # Create the node for the destination
        finishNode = head
        # Loop through the nodes till you get to the index
        for i in range(finish-1):
            finishNode = finishNode.next
        # Link the source node to the destination
        startNode.snadder = finishNode
    # Return the linked list
    return head   

def willfinish(first, stepsize):
    # Create pointers
    player = first
    curr = first.next
    finish = first
    # To get # of tiles
    counter = 1
    # Counters to see if you can't win
    snadCount = 0
    repetitive = 0
    moves = 0
    result = False
    # Get the total number of squares on the board
    while(curr != player):
        curr = curr.next
        counter += 1
    # Set the finish pointer to the final pointer so we can compare later
    for i in range(counter-1):
        finish = finish.next
    # Set the player in the correct position
    for i in range(stepsize-1):
        player = player.next
    # Hold the original position of the player (to check for endless loops)
    player_pos = player
    # Check whether the player is on the finish tile
    if (player == finish):
        result = True
    else:
        # Run this as long as the player isn't on the finish tile
        # AND the player hasn't landed on the same tile more than twice
        # meaning you can't complete it AND you haven't done too many moves
        while(player != finish and repetitive < 2 and moves < counter*5 and
              snadCount < 20):
            # Count the number of moves
            moves += 1
            # This is to see if you're stuck in an endless loop of climbing
            # a snadder
            while (player.snadder != None and snadCount < 20):
                snadCount += 1
                player = player.snadder
            # Move the player 'stepsize' amount of steps
            for i in range(stepsize):
                player = player.next
            # Check if there is a snadder, if there is, follow it
            if (player.snadder != None):
                player = player.snadder
            # If the player lands on the original position it was add, increase
            # the counter by 1, if it lands on it twice and the game hasn't
            # ended, clearly you can't win
            if (player == player_pos):
                repetitive += 1
            # If the player is on the finish tile, return True
            if (player == finish):
                result = True
    # Return the result (it's set to None by default)
    return result

def numMoves(first, stepsize):
    # Create pointers
    player = first
    curr = first.next
    finish = first
    # To get # of tiles
    counter = 1
    # To see if you can't win
    snadCount = 0
    repetitive = 0
    moves = 0
    result = False
    # Get the total number of squares on the board
    while(curr != player):
        curr = curr.next
        counter += 1
    # Set the finish pointer to the final pointer so we can compare later
    for i in range(counter-1):
        finish = finish.next
    # Set the player in the correct position
    for i in range(stepsize-1):
        player = player.next
    # Hold the original position of the player (to check for endless loops)
    player_pos = player
    # Check whether the player is on the finish tile
    if (player == finish):
        result = True
    else:
        # Run this as long as the player isn't on the finish tile
        # AND the player hasn't landed on the same tile more than twice
        # meaning you can't complete it AND you haven't done too many moves
        while(player != finish and repetitive < 2 and moves < counter*5 and
              snadCount < 20):
            # Count the number of moves
            moves += 1
            while (player.snadder != None and snadCount < 20):
                snadCount += 1
                player = player.snadder
            # Move the player 'stepsize' amount of steps
            for i in range(stepsize):
                player = player.next
            # Check if there is a snadder, if there is, follow it
            if (player.snadder != None):
                player = player.snadder
            # If the player lands on the original position it was add, increase
            # the counter by 1, if it lands on it twice and the game hasn't
            # ended, clearly you can't win
            if (player == player_pos):
                repetitive += 1
            # If the player is on the finish tile, return True
            if (player == finish):
                result = True
    # Return the total number of moves done
    return moves

def whowins(first, step1, step2):
    # Check if Player 1 will finish
    Player1 = willfinish(first, step1)
    # Get the # of moves Player 1 made
    Player1Moves = numMoves(first, step1)
    # Check if Player 2 will finish
    Player2 = willfinish(first, step2)
    # Get the # of moves Player 2 made
    player2Moves = numMoves(first, step2)
    # If both players don't finish, player 2 wins (as per the rules)
    if (Player1 == False and Player2 == False):
        result = 2
    # If Player 1 wins and Player 2 doesn't
    elif (Player1 == True and Player2 == False):
        result = 1
    # If Player 1 loses and Player 2 wins
    elif (Player1 == False and Player2 == True):
        result = 2
    # If Player 1 AND Player 2 wins
    elif (Player1 == True and Player2 == True):
        # If Player 1 made more moves than Player 2, Player 2 is the winner
        if (Player1Moves > Player2Moves):
            result = 2
        # If Player 1 made less moves than Player 2 or equal amount, Player 1
        # will win since that player moves first
        elif (Player1Moves <= Player2Moves):
            result = 1
    # Return the winner
    return result

def dualboard(first):
    # Create the necessary pointers
    curr = first
    squareCounter = first.next
    # Create a new node to start making the dualboard
    head = SALBnode()
    tail = head
    counter = 1
    j = 0
    # Count the number of squares in the original game board
    while(squareCounter != curr):
        squareCounter = squareCounter.next
        counter += 1
    # Based on how much squares were in the original game board, create an
    # empty board with the same amount of squares
    for i in range(counter-1):
        new_node = SALBnode()
        tail.next = new_node
        tail = new_node
    # Set the tail to the head to make the linked list circular
    tail.next = head
    # Start to create the snadders on the copy board
    for i in range(counter-1):
        # Create the needed pointers, two which point to the head of the copy
        # board and one which points to the head of the original board
        checker = first
        currNew = head
        destination = head
        # Check if the node in the original board has a snadder, if it doesn't
        # move onto the next
        if (curr.snadder == None):
            curr = curr.next
        else:
            # If there is a snadder (source) on this node, begin searching for
            # the destination 
            while (curr.snadder != checker):
                j += 1
                checker = checker.next
            # Once you find the destination, re-create the same thing on the
            # copy board, but swap the destination and source
            if (curr.snadder == checker):
                for k in range(i):
                    # This will be the new destination
                    currNew = currNew.next
                for l in range(j):
                    # This will be the new source
                    destination = destination.next
                # Swap the source and the destination
                destination.snadder = currNew
                # Move onto the next node in the original board to keep going
                # through the rest of the nodes
                curr = curr.next
    # Return the copy board (original board stays unaffected)
    return head


'''This function is here to simply draw out the board in a nice way so you can
visually see if you did it right, it doesn't affect the code at all
'''
def testing(__salb1__, size):
    
    # first node is the output of the salb2salbLL function
    __head__ = __salb1__
    # get the max width by rounding down the square root of numSquares
    __maxwidth__ = math.floor(math.sqrt(size))

    try:
        # copy the nodes into a list
        __squares__ = []
        # set node to be the head of the list
        __node__ = __head__
        # for every node
        for o in range(0, size):
            # append it to the list
            __squares__.append(__node__)
            # move one forward
            if __node__.next is not None:
                __node__ = __node__.next
            else:
                print("Null pointer at node.next\n One of your links is not",
                      "pointing to the right place :O")
        # empty start:end dict
        __snadders__ = {}
        # run through the list and copy the start:end pairs from the nodes
        for p in range(0, len(__squares__)):
            if __squares__[p].snadder is not None:
                __snadders__[p + 1] = __squares__.index(
                    __squares__[p].snadder) + 1
        # keep records of the start and end of each snadder from the dict
        __start__ = list(__snadders__.keys())
        #__start__.sort()
        __end__ = list(__snadders__.values())
        #__end__.sort()

    except (IndexError, TypeError) as ex:
        print(
            "Oh no! Something broke, double check your code!")
    else:
        if list(__snadders__.keys()) != __start__:
            print("Your linked list snadders and your dictionary snadders",
                  "don't match 0_0\n")

    # counter to reference the current square's number
    __counter__ = 1
    try:
        # for each row in the board
        for k in range(0, int(math.ceil(size / __maxwidth__))):
            # make a string to add the squares into
            row = ""
            # for each column in the board
            for j in range(int(k * __maxwidth__), int((k + 1) * __maxwidth__)):
                # if the square has a snadder
                if __counter__ in __start__:
                    # print a square with the number of the index in it
                    row += ("[_" + str(__start__.index(__counter__)) + "S_]")
                elif __counter__ in __end__:
                    # print a square with the number of the index in it
                    row += ("[_" + str(__end__.index(__counter__)) + "E_]")
                elif __counter__ <= size:
                    # print an empty square
                    row += ("[____]")
                # add one to the counter
                __counter__ += 1
                # move to the next node
                __node__ = __node__.next
            # print the row
            print(row, "\n\n")
    except IndexError:
        print("Graph failed :(\nDouble check your code!")

if __name__ == "__main__":
    import math
    import doctest
    
    print("NORMAL BOARD")
    # Create a new board with 9 squares, and snadders from 2 -> 6 and 5 -> 3
    board = salb2salbLL(SALboard(9, {2:6, 5:3}))
    testing(board, 9)
    print("\n")
    print("DUAL BOARD")
    testing(dualboard(board), 9)

#if __name__ == "__main__":
    #a = salb2salbLL(SALboard(4, {2:3}))
    #b = dualboard(a)
    #print(willfinish(a, 2))
    ##print(numMoves(a, 2))
    #print(willfinish(b, 2))
    ##print(numMoves(b, 2))    
    