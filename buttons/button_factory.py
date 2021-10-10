from enum import Enum

from buttons.add_to_poll_button import AddToPollButton


class ButtonType(Enum):
    ADD_TO_POLL_BUTTON = "AddToPollButton"


class ButtonFactory:
    @staticmethod
    def create_button(button_type, *args, **kwargs):
        if button_type == "AddToPollButton":
            return AddToPollButton(*args, **kwargs)
