
import wpilib
import wpilib.drive
from wpilib.command import Scheduler
from src.python.frc.robot.subsystems.ArmSubsystem import ArmSubsystem
from src.python.frc.robot.subsystems.DriveTrainSubsystem import DriveTrainSubsystem
from src.python.frc.robot.subsystems.IntakeSubsystem import IntakeSubsystem
from src.python.frc.robot.subsystems.PneumaticsSubsystem import PneumaticsSubsystem
from src.python.frc.robot.subsystems.WristSubsystem import WristSubsystem
from src.python.frc.robot.OI import OI

from wpilib.robotbase import RobotBase
from wpilib import TimedRobot

 
class SpartanRobot(TimedRobot):
    
    def robotInit(self):
        self.drivetrain = DriveTrainSubsystem()  
        self.oi = OI()
        self.drivetrain.updateMotorOutputs()
    
    def robotPeriodic(self):
        self.drivetrain.updateMotorOutputs()

    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        self.Scheduler.getInstance().run()
        
    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.Scheduler.getInstance().run()


if __name__ == "__main__":
    wpilib.run(SpartanRobot)