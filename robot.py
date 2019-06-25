
import wpilib
import wpilib.drive
#from wpilib.command import Scheduler
#from src.python.frc.robot.subsystems.ArmSubsystem import ArmSubsystem as arm
from subsystems.DriveTrainSubsystem import DriveTrainSubsystem as drive
#from src.python.frc.robot.subsystems.IntakeSubsystem import IntakeSubsystem as intake
#from src.python.frc.robot.subsystems.PneumaticsSubsystem import PneumaticsSubsystem as pneumatics
#from src.python.frc.robot.subsystems.WristSubsystem import WristSubsystem as wrist
from OI import OI

from wpilib.robotbase import RobotBase
from wpilib import TimedRobot

 
class THICC(TimedRobot):
    
    def robotInit(self):
        self.drivetrain = drive()  
        self.oi = OI()
        self.drivetrain.updateMotorOutputs()
    
    def robotPeriodic(self):
        self.drivetrain.updateMotorOutputs()

    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        pass
        
    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(THICC)