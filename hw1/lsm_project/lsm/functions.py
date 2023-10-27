"""
В этом модуле хранятся функции для применения МНК
"""


from typing import Optional
from numbers import Real       # раскомментируйте при необходимости

from lsm_project.event_logger.event_logger import EventLogger

from lsm_project.lsm.enumerations import MismatchStrategies
from lsm_project.lsm.models import (
    LSMDescription,
    LSMStatistics,
    LSMLines,
)


PRECISION = 3                   # константа для точности вывода
event_logger = EventLogger()    # для логирования


def get_lsm_description(
    abscissa: list[float], ordinates: list[float],
    mismatch_strategy: MismatchStrategies = MismatchStrategies.FALL
) -> LSMDescription:
    """
    Функции для получения описания рассчитаной зависимости

    :param: abscissa - значения абсцисс
    :param: ordinates - значение ординат
    :param: mismatch_strategy - стратегия обработки несовпадения

    :return: структура типа LSMDescription
    """
    global event_logger

    if not (isinstance(abscissa, list)) or not (isinstance(ordinates, list)):
        try:
            abscissa = list(abscissa)
            ordinata = list(ordinates)
        except TypeError:
            raise TypeError
    if not _is_valid_measurments(abscissa):
        raise ValueError
    if not _is_valid_measurments(ordinates):
        raise ValueError
    if len(abscissa) <= 2 or len(ordinates) <= 2:
        raise ValueError
    if len(abscissa) != len(ordinates):
        if mismatch_strategy == MismatchStrategies.FALL:
            raise RuntimeError
        elif mismatch_strategy == MismatchStrategies.CUT:
            abscissa = abscissa[:min(len(abscissa), len(ordinates))]
            ordinata = ordinata[:min(len(abscissa), len(ordinates))]
        else:
            raise ValueError
    return _get_lsm_description(abscissa, ordinates)


def get_lsm_lines(
    abscissa: list[float], ordinates: list[float],
    lsm_description: Optional[LSMDescription] = None
) -> LSMLines:
    """
    Функция для расчета значений функций с помощью результатов МНК

    :param: abscissa - значения абсцисс
    :param: ordinates - значение ординат
    :param: lsm_description - описание МНК

    :return: структура типа LSMLines
    """

    x, y = abscissa, ordinates
    if lsm_description is None:
        lsm_description = _get_lsm_description(x, y)
    elif not (isinstance(lsm_description, LSMDescription)):
        raise TypeError
    d = lsm_description
    line_predicted, line_above, line_under = [], [], []
    for i in range(len(ordinates)):
        line_predicted.append(x[i] * d.incline + d.shift)
        line_above.append((d.incline + d.incline_error) *
                          x[i] + d.shift + d.shift_error)
        line_under.append((d.incline - d.incline_error) *
                          x[i] + d.shift - d.shift_error)
    return LSMLines(
        abscissa=abscissa,
        ordinates=ordinates,
        line_predicted=line_predicted,
        line_above=line_above,
        line_under=line_under
    )


def printStr(FloatNumber, Precision):
    return "%0.*f" % (Precision, FloatNumber)


def get_report(
    lsm_description: LSMDescription, path_to_save: str = ''
) -> str:
    """
    Функция для формирования отчета о результатах МНК

    :param: lsm_description - описание МНК
    :param: path_to_save - путь к файлу для сохранения отчета

    :return: строка - отчет определенного формата
    """
    global PRECISION

    ans = '=' * 40 + 'LSM computing result' + '=' * 40 + '\n\n'
    ans += '[INFO]: incline: ' + \
        printStr(lsm_description.incline, PRECISION) + ';\n'
    ans += '[INFO]: shift: ' + \
        printStr(lsm_description.shift, PRECISION) + ';\n'
    ans += '[INFO]: incline error: ' + \
        printStr(lsm_description.incline_error, PRECISION) + ';\n'
    ans += '[INFO]: shift error: ' + \
        printStr(lsm_description.shift_error, PRECISION) + ';\n\n'
    ans += '=' * 100

    if path_to_save != '':
        f = open(path_to_save, 'w')
        f.write(ans)
    return ans


# служебная функция для валидации
def _is_valid_measurments(measurments: list[float]) -> bool:
    return all(isinstance(x, Real) for x in measurments)


# служебная функция для обработки несоответствия размеров
def _process_mismatch(
    abscissa: list[float], ordinates: list[float],
    mismatch_strategy: MismatchStrategies = MismatchStrategies.FALL
) -> tuple[list[float], list[float]]:
    global event_logger

    # ваш код
    # эту строчку можно менять
    return [], []


# служебная функция для получения статистик
def _get_lsm_statistics(
    abscissa: list[float], ordinates: list[float]
) -> LSMStatistics:
    global event_logger, PRECISION

    # ваш код
    # эту строчку можно менять
    return LSMStatistics(
        abscissa_mean=0,
        ordinate_mean=0,
        product_mean=0,
        abs_squared_mean=0
    )


# служебная функция для получения описания МНК
def _get_lsm_description(
    abscissa: list[float], ordinates: list[float]
) -> LSMDescription:
    global event_logger, PRECISION

    n, x, y = len(ordinates), abscissa, ordinates
    avg_xy = sum(x[i] * y[i] for i in range(n)) / n
    avg_x = sum(x) / n
    avg_y = sum(y) / n
    avg_x_square = sum(x[i] ** 2 for i in range(n)) / n

    a = (avg_xy - avg_x*avg_y) / (avg_x_square - avg_x ** 2)
    b = avg_y - a*avg_x
    y_dispertion = sum([(y[i]-a*x[i]-b) ** 2 for i in range(n)])/(n-2)
    a_dispertion = y_dispertion / (n*(avg_x_square - avg_x**2))
    b_dispertion = y_dispertion*avg_x_square / (n*(avg_x_square - avg_x**2))
    return LSMDescription(
        incline=a,
        shift=b,
        incline_error=a_dispertion ** 0.5,
        shift_error=b_dispertion ** 0.5
    )
