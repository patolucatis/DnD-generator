import secrets

from typing import Optional, Callable, Any


def rolldices():
    rolls = [0, 0, 0]
    i = 0
    while i < 3:
        rolls[i] = secrets.randbelow(6)+1
        i = i + 1
    minroll = 6
    suma = 0
    for roll in rolls:
        suma += roll
        if roll < minroll:
            minroll = roll
    suma -= minroll
    return suma


def modifier(stat):
    return (stat - 10) / 2


class InputGetter:
    def __init__(self, empty_message: Optional[str] = None, invalid_message: Optional[str] = None) -> None:
        self.empty_message = empty_message
        self.invalid_message = invalid_message
        self.handler: Optional[Callable] = None

    def set_invalid_handler(self, handler: Callable[..., bool]) -> None:
        """Set a custom handler."""
        self.handler = handler

    def _default_text_handler(self, _txt: Any) -> bool:
        """Checks that the input isn't empty."""
        if not _txt:
            print(self.empty_message or "Error: empty input. Try again!")
            return False

        return True

    def _default_number_handler(self, _num: Any, amount: int = 0) -> bool:
        """Checks that the input isn't empty, and that it's a valid number.

        Also, optionally checks if the number is within a given range.
        """
        if not self._default_text_handler(_num):
            return False

        try:
            num = int(_num)
        except ValueError:
            print(self.invalid_message or "Error: invalid input. Try again!")
            return False

        if amount != 0:
            if num < 1 or num > amount:
                print(self.invalid_message or "Error: invalid input. Try again!")
                return False

        return True

    def string(self) -> str:
        handler = self.handler or self._default_text_handler
        while True:
            inputter = input(">> ")
            if handler(inputter):
                return inputter

    def int(self, amount: int) -> int:
        handler = self.handler if self.handler else self._default_number_handler
        while True:
            inputter = input(">> ")
            if handler(inputter, amount):
                return int(inputter)
