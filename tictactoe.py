from typing import List

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY] * 3 for _ in range(3)]


def player():
    raise NotImplementedError


def terminal():
    raise NotImplementedError


def winner():
    raise NotImplementedError


def actions():
    raise NotImplementedError


def result():
    raise NotImplementedError


def utility():
    raise NotImplementedError


def minimax():
    raise NotImplementedError
