from config import PIN_MAP

class Motor:

    def __init__(self, hi_pin, lo_pin, en_pin):
        self.hi_pin = hi_pin
        self.lo_pin = lo_pin
        self.en_pin = en_pin
        self.direction = 'forward'
        self.speed = 0

    def forward(self, speed):
        self.direction = 'forward'
        self.speed = speed
    def backward(self, speed):
        self.direction = 'backward'
        self.speed = speed

    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        # TODO: Actually set direction
        self._direction = direction

    direction = property(get_direction, set_direction)

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        # TODO: Actually set speed
        self._speed = speed

    speed = property(get_speed, set_speed)

class Motors: 
    """Shortcut class to do the same thing to both motors"""
    
    def __init__(self, *motors):
        self.motors = motors

    def __getattr__(self, method_name):
        """Calls the method on all motors"""
        def method(*args):
            for motor in self.motors:
                motor.__getattr__(method_name)(args)
        return method

left_motor = Motor() # TODO: Pass in the correct pins
right_motor = Motor()
motors = Motors([left_motor, right_motor])
