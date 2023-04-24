from machine import Pin, PWM

"""
Class to represent our robot car
"""
class RobotCar():
    def __init__(self, enable_pins, motor_pins, speed):
        self.right_motor_enable_pin = PWM(Pin(enable_pins[0]), freq=2000)
        self.left_motor_enable_pin = PWM(Pin(enable_pins[1]), freq=2000)
        
        self.right_motor_control_1 = Pin(motor_pins[0], Pin.OUT)
        self.right_motor_control_2 = Pin(motor_pins[1], Pin.OUT)
        
        self.left_motor_control_1 = Pin(motor_pins[2], Pin.OUT)
        self.left_motor_control_2 = Pin(motor_pins[3], Pin.OUT)
        
        self.speed = speed
        
    def stop(self):
        print('Car stopping')
        self.right_motor_control_1.value(0)
        self.right_motor_control_2.value(0)
        self.left_motor_control_1.value(0)
        self.left_motor_control_2.value(0)
        self.right_motor_enable_pin.duty_u16(0)
        self.left_motor_enable_pin.duty_u16(0)
        
    def forward(self):
        print('Move forward')
        self.right_motor_enable_pin.duty_u16(self.speed)
        self.left_motor_enable_pin.duty_u16(self.speed)
        
        self.right_motor_control_1.value(1)
        self.right_motor_control_2.value(0)
        self.left_motor_control_1.value(1)
        self.left_motor_control_2.value(0)

    
    def reverse(self):
        print('Move reverse')
        self.right_motor_enable_pin.duty_u16(self.speed)
        self.left_motor_enable_pin.duty_u16(self.speed)
        
        self.right_motor_control_1.value(0)
        self.right_motor_control_2.value(1)
        self.left_motor_control_1.value(0)
        self.left_motor_control_2.value(1)
    
    def turnLeft(self):
        print('Turning Left')
        self.right_motor_enable_pin.duty_u16(self.speed)
        self.left_motor_enable_pin.duty_u16(self.speed)
        
        self.right_motor_control_1.value(1)
        self.right_motor_control_2.value(0)
        self.left_motor_control_1.value(0)
        self.left_motor_control_2.value(0)
    
    def turnRight(self):
        print('Turning Right')
        self.right_motor_enable_pin.duty_u16(self.speed)
        self.left_motor_enable_pin.duty_u16(self.speed)
        
        self.right_motor_control_1.value(0)
        self.right_motor_control_2.value(0)
        self.left_motor_control_1.value(1)
        self.left_motor_control_2.value(0)
        
    def set_speed(self, new_speed):
        self.speed = new_speed
        
    def cleanUp(self):
        print('Cleaning up pins')
        self.right_motor_enable_pin.deinit()
        self.left_motor_enable_pin.deinit()
