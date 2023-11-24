from typing import Iterable, Union
from numbers import Real

from regressors.regressor_abc import RegressorABC


class RegressorLSM(RegressorABC):
    def __init__(self):
        ...

    def fit(self, abscissa: Iterable, ordinates: Iterable) -> None:
        self.abscissa = abscissa
        self.ordinates = ordinates
        pass

    def predict(self, abscissa: Union[Real, Iterable]) -> list:
        prediction = []
        self._compute_coefs()
        for x in abscissa:
            prediction.append(self._compute_prediction(x))

        return prediction
    
    def _compute_prediction(self, x):
        return self.a * x + self.b
    
    def _compute_coefs(self):
        avg_y = sum(self.ordinates) / len(self.ordinates)
        avg_x = sum(self.abscissa) / len(self.abscissa)
        avg_xy = sum([self.abscissa[i] * self.ordinates[i] for i in range(len(self.abscissa))]) / len([self.abscissa[i] * self.ordinates[i] for i in range(len(self.abscissa))])
        avg_x_square = sum([x**2 for x in self.abscissa]) / len([x**2 for x in self.abscissa])

        self.a = (avg_xy - avg_x * avg_y) / (avg_x_square - avg_x **2)
        self.b = avg_y - self.a * avg_x



