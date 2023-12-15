from random import randint

from nim_game.common.models import NimStateChange


STONE_AMOUNT_MIN = 1        # минимальное начальное число камней в кучке
STONE_AMOUNT_MAX = 10       # максимальное начальное число камней в кучке


class EnvironmentNim:
    """
    Класс для хранения и взаимодействия с кучками
    """

    _heaps: list[int]       # кучки

    def __init__(self, heaps_amount: int) -> None:
        if (not (2 <= heaps_amount <= 10)):
            raise ValueError
        self._heaps = [randint(1, 10) for _ in range(heaps_amount)]

    def get_state(self) -> list[int]:
        return [x for x in self._heaps]

    def change_state(self, state_change: NimStateChange) -> None:
        heap, taken = state_change.heap_id, state_change.decrease
        if (not (0 <= heap < len(self._heaps))):
            raise ValueError
        elif (not (1 <= taken <= self._heaps[heap])):
            raise ValueError
        self._heaps[state_change.heap_id] -= state_change.decrease
