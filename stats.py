from collections import Counter
from typing import Union


class Stats:

    @staticmethod
    def mean(lst: list) -> float:
        return sum(lst) / len(lst)

    @staticmethod
    def median(lst: list) -> Union[int, float]:
        s = sorted(lst)
        ln = len(lst)
        if ln % 2 == 0:
            return (s[ln//2] + s[ln//2-1])/2
        return s[ln//2]

    @staticmethod
    def mode(lst: list) -> Union[int, float]:
        return Counter(lst).most_common(1)[0][0]

