# Enumeration of possible actions
from __future__ import annotations
from enum import IntEnum

from itertools import combinations

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

    diagonal_backwards_left = 14
    diagonal_backwards_right = 15
    left_move_no_turn = 16
    right_move_no_turn = 17
    backward = 18


class ActionSpace(object):
    def __init__(self, legal_actions: tuple[Actions, ...]):
        self.legal_actions = legal_actions

    def get_legal_actions(self) -> tuple[Actions, ...]:
        return self.legal_actions

    @staticmethod
    def get_all_action_spaces_with_n_sample_actions(n_sample_actions)-> list[ActionSpace]:
        fixed_actions = list(Actions)[3:7]  # pickup, drop, toggle, done
        sample_actions = list(Actions)[1:3] + list(Actions)[7:]
        all_action_combs = list(combinations(sample_actions, n_sample_actions))
        all_action_spaces = []
        for asp_i in range(len(all_action_combs)):
            all_action_spaces.append(ActionSpace(legal_actions=all_action_combs[asp_i] + tuple(fixed_actions)))
        return all_action_spaces

    def is_named_action_space(self) -> bool:
        return set(self.legal_actions) in (set(asp.legal_actions) for asp in NamedActionSpace)

    def get_agent_color(self) -> tuple[int, int, int]:
        return 255, 0, 0



class NamedActionSpace(ActionSpace, IntEnum):
    # Standard 
    standard = 0, (Actions.left, Actions.right, Actions.forward, Actions.pickup, Actions.drop, Actions.toggle, Actions.done)
    # No left turns
    no_left = 1, (Actions.right, Actions.forward, Actions.pickup, Actions.drop, Actions.toggle, Actions.done)
    # No right turns 
    no_right = 2, (Actions.left, Actions.forward, Actions.pickup, Actions.drop, Actions.toggle, Actions.done)
    # Diagonal steps possible 
    diagonal = 3, (Actions.left, Actions.right, Actions.forward, Actions.pickup, Actions.drop, Actions.toggle, Actions.done, Actions.diagonal_left, Actions.diagonal_right)
    # WSAD movement (up down left right) turn + move with single action
    wsad = 4, (Actions.right_move, Actions.down_move, Actions.left_move, Actions.up_move, Actions.pickup, Actions.drop, Actions.toggle, Actions.done)
    # All adjacent cells (includes diagonals) + right turn for turning
    dir8 = 5, (Actions.right_move_no_turn, Actions.backward,
                Actions.left_move_no_turn,
                Actions.forward,
                Actions.diagonal_backwards_left,
                Actions.diagonal_backwards_right,
                Actions.diagonal_right,
                Actions.diagonal_left,
                Actions.right,
                Actions.pickup,
                Actions.drop,
                Actions.toggle,
                Actions.done
            )

    def __new__(cls, value, legal_actions):
        member = int.__new__(cls)
        member._value_ = value
        member.legal_actions = legal_actions
        return member

    def __init__(self, _, legal_actions: tuple[Actions, ...]):
        super().__init__(legal_actions=legal_actions)


    def get_agent_color(self) -> tuple[int, int, int]:
        if self == NamedActionSpace.standard:
            return (255, 0, 0)
        elif self == NamedActionSpace.no_left:
            return (0, 255, 0)
        elif self == NamedActionSpace.no_right:
            return (0, 0, 255)
        elif self == NamedActionSpace.diagonal:
            return (255, 255, 0)
        elif self == NamedActionSpace.wsad:
            return (0, 255, 255)
        elif self == NamedActionSpace.dir8:
            return (255, 0, 255)
        else:
            raise RuntimeError(f'Unknown actionspace {self}')


