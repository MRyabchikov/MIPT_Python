import json

from nim_game.environments.environment_nim import EnvironmentNim
from nim_game.common.models import NimStateChange, GameState
from nim_game.agents.agent import Agent
from nim_game.common.enumerations import Players


class GameNim:
    _environment: EnvironmentNim        # состояния кучек
    _agent: Agent                       # бот

    def __init__(self, path_to_config: str) -> None:
        data = json.load(open(path_to_config))
        self._environment = EnvironmentNim(data['heaps_amount'])
        self._agent = Agent(data['opponent_level'])

    def make_steps(self, player_step: NimStateChange) -> GameState:
        self._environment.change_state(player_step)
        if (self.is_game_finished()):
            return GameState(winner=Players.USER)
        else:
            return GameState(opponent_step=self._agent.make_step
                             (self.heaps_state), heaps_state=self.heaps_state)

    def is_game_finished(self) -> bool:
        return all(x == 0 for x in self.heaps_state)

    @property
    def heaps_state(self) -> list[int]:
        return self._environment.get_state()
