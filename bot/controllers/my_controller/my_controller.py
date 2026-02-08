"""my_controller controller."""
from controller import Robot

def run_robot(robot):
    time_step = 32

    # Get the IR sensor (center)
    ir = robot.getDistanceSensor('ir3')
    ir.enable(time_step)

    while robot.step(time_step) != -1:
        ir_value = ir.getValue()
        print(f"IR: {ir_value:.2f}")

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)


