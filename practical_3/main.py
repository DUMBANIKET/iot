import time
import matplotlib.pyplot as plt

from drawnow import *
import Adafruit_ADS1x15
adc=Adafruit_ADS1x15.ADS1115()
GAIN=1
val=[]
cnt=0
plt.ion()
adc.start_adc(0,gain=GAIN)
print("reading ADS1x15 Channel 0")

def makeFig():
    plt.ylim(-5000,5000)
    plt.title("Discover Lab occiloscope")
    plt.grid(True)
    plt.ylabel("ADC Outputs")
    plt.plot(val,'ro-',label="Channel 0")
    plt.legend(loc='lower right')

while (True):
    value=adc.get_last_result()
    print('cahnnel 0 :{0}'.format(value))
    time.sleep(0.1)
    val.append(int(value))
    drawnow(makeFig)
    plt.pause(.000001)
    cnt+=1
    if(cnt>50):
        val.pop(0)
