import board
import digitalio
from kmk import KMKKeyboard
from kmk.keys import KC
from kmk.modules import ModTap
from kmk.modules import Layer

keyboard = KMKKeyboard()

modtap = ModTap()
keyboard.modules.append(modtap)

switch1 = digitalio.DigitalInOut(board.D5)
switch1.switch_to_input(pull=digitalio.Pull.UP)

switch2 = digitalio.DigitalInOut(board.D6)
switch2.switch_to_input(pull=digitalio.Pull.UP)

switch3 = digitalio.DigitalInOut(board.D7)
switch3.switch_to_input(pull=digitalio.Pull.UP)

switch4 = digitalio.DigitalInOut(board.D8)
switch4.switch_to_input(pull=digitalio.Pull.UP)

keyboard.pins = {
    board.D5: KC.W(mt=KC.UP),     # Tap: W, Hold: Up Arrow
    board.D6: KC.D(mt=KC.RIGHT),  # Tap: D, Hold: Right Arrow
    board.D7: KC.A(mt=KC.LEFT),   # Tap: A, Hold: Left Arrow
    board.D8: KC.S(mt=KC.DOWN),   # Tap: S, Hold: Down Arrow
}

layer1 = Layer([KC.LSFT, KC.LCTL, KC.LALT])
keyboard.modules.append(layer1)

if __name__ == "__main__":
    while True:
        keyboard.poll()
