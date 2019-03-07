import time
import u3


class LabJackU3:
    
    device = u3.U3()
    calibrationData = d.getCalibrationData()
    DAC0Offset = calibrationData.get('dac0Offset')
    DAC0Slope  = calibrationData.get('dac0Slope')
    DAC1Offset = calibrationData.get('dac1Offset')
    DAC1Slope  = calibrationData.get('dac1Slope')
    
    
