from math import sin, cos, radians
from matplotlib import pyplot as plt

def left(trtl, angle):
    trtl['azimuth'] += angle
    
def right(trtl, angle):
    trtl['azimuth'] -= angle
    
def forward(trtl, r):
    x, y = trtl['X'][-1], trtl['Y'][-1]
    azimuth = trtl['azimuth']
    x += r * cos(radians(azimuth))
    y += r * sin(radians(azimuth))
    trtl['X'].append(x)
    trtl['Y'].append(y)

def set_turtle(x=0, y=0, azimuth=0):
    return {'X': [x],
            'Y': [y],
            'azimuth': azimuth}

def draw(trtl, **kwargs):
    plt.plot(trtl['X'], trtl['Y'], **kwargs)

def polygon_with_stop(position, side, angle):
    ang_sum = 0
    while True:
        forward(position, side)
        left(position, angle)
        ang_sum += angle
        
        if ang_sum % 360 == 0:
            return
        
position = set_turtle(50, 40, 45)
polygon_with_stop(position, 5, 100)
plt.figure(figsize=(6, 6))
draw(position, color='green', ls='--')
plt.show()
