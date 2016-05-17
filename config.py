
PIN_MAP = {
    'MOTOR_A_HI', 26
    'MOTOR_A_LO', 13
    'MOTOR_A_EN', 19
    'MOTOR_B_HI', 5
    'MOTOR_B_LO', 6
    'MOTOR_B_EN', 12
}

used_pins = PIN_MAP.values()
assert len(set(used_pins)) == len(used_pins)

LEFT_MOTOR = 'A'
RIGHT_MOTOR = 'B'

