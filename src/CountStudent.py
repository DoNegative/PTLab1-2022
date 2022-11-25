# -*- coding: utf-8 -*-
from Types import DataType

RatingType = dict[str, float]


class CountStudent:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}
        self.countStudent: int = 0

    def calc(self) -> any:

        for key in self.data:
            x = 0
            for subject in self.data[key]:
                if subject[1] >= 90:
                    x += 1
            if x == len(self.data[key]):
                self.countStudent += 1
        return self
