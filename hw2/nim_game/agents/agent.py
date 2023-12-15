from random import randint

from nim_game.common.enumerations import AgentLevels
from nim_game.common.models import NimStateChange


def is_correct_step(state_curr: list[int], taken: int, heap: int):
    return taken <= state_curr[heap]


def make_random_turn(state_curr: list[int]):
    heap = randint(0, len(state_curr)-1)
    while(state_curr[heap] == 0):
        heap = randint(0, len(state_curr)-1)
    taken = randint(1, state_curr[heap])
    return heap, taken


def calculate_nim_sum(state_curr: list[int]):
    res = state_curr[0]
    for i in range(1, len(state_curr)):
        res ^= state_curr[i]
    return res


def make_wise_turn(state_curr: list[int]):
    if (calculate_nim_sum(state_curr) == 0):
        return make_random_turn(state_curr)
    else:
        for i in range(len(state_curr)):
            for j in range(1, state_curr[i]+1):
                state_curr[i] -= j
                if (calculate_nim_sum(state_curr) == 0):
                    state_curr[i] += j
                    return i, j
                else:
                    state_curr[i] += j


class Agent:
    _level: AgentLevels         # уровень сложности

    def __init__(self, level: str) -> None:
        if (level not in [e.value for e in AgentLevels]):
            raise ValueError
        self._level = level

    def make_step(self, state_curr: list[int]) -> NimStateChange:
        heap, taken = 0, 0
        if (self._level == AgentLevels.EASY.value):
            heap, taken = make_random_turn(state_curr)
        elif (self._level == AgentLevels.NORMAL.value):
            if (randint(0, 1) == 0):
                heap, taken = make_random_turn(state_curr)
            else:
                heap, taken = make_wise_turn(state_curr)
        else:
            heap, taken = make_wise_turn(state_curr)
        return NimStateChange(heap_id=heap, decrease=taken)
