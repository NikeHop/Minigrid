# Enumeration of possible actions
from __future__ import annotations

from enum import IntEnum


class Actions(IntEnum):
    # Turn left, turn right, move forward
    left = 0
    right = 1
    forward = 2
    # Pick up an object
    pickup = 3
    # Drop an object
    drop = 4
    # Toggle/activate an object
    toggle = 5

    # Done completing task
    done = 6

    # Step diagonal left 
    diagonal_left = 7

    # Step diagonal right 
    diagonal_right = 8
    
    # Turn and go left
    right_move = 9
    down_move = 10
    left_move = 11
    up_move = 12

    # Turn 180 degrees
    turn_around = 13



class ActionSpace(IntEnum):
    # Standard 
    standard = 0

    # No left turns
    no_left = 1

    # No right turns 
    no_right = 2

    # Diagonal steps possible 
    diagonal = 3

    # WSAD movement (up down left right) turn + move with single action
    wsad = 4

    def get_legal_actions(self) -> tuple(Actions, ...):
        if self == ActionSpace.standard:
            return (Actions.left, Actions.right, Actions.forward, Actions.pickup, Actions.drop, Actions.toggle, Actions.done)
        elif self == ActionSpace.no_left:
            return (Actions.right, Actions.forward, Actions.pickup, Actions.drop, Actions.toggle, Actions.done)
        elif self == ActionSpace.no_right:
            return (Actions.left, Actions.forward, Actions.pickup, Actions.drop, Actions.toggle, Actions.done)
        elif self == ActionSpace.diagonal:
            return (Actions.left, Actions.right, Actions.forward, Actions.pickup, Actions.drop, Actions.toggle, Actions.done, Actions.diagonal_left, Actions.diagonal_right)
        elif self == ActionSpace.wsad:
            return (Actions.right_move, Actions.down_move, Actions.left_move, Actions.up_move)#, Actions.pickup, Actions.drop, Actions.toggle, Actions.done)
        else:
            raise RuntimeError(f'Unknown actionspace {self}')

