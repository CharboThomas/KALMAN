import numpy as np
import math as mt
import matplotlib.pyplot as plt


def MRUA(a: int, v: int, d: int, t: int, n: int):
    """
    MRUA = Mouvement rectiligne uniforme
    :param a: is the acceleration
    :param v: is the speed
    :param d: is the start position
    :param t: is a time in second
    :param n: is the number of sample
    :return:
    """

    temps = np.linspace(0, t, n)

    position = []

    for i in range(0, len(temps), 1):
        X = a * (temps[i] ** (2)) + v * temps[i] + d

        position.append(X)

    return (position)


def liste0(n: int, data: int):
    liste = []

    for i in range(0, n, 1):
        liste.append(data)

    return (liste)


def MCUA(a: int, w: int, O: int, r: int, t: int, n: int):
    """
    MCU = Mouvement circulaire uniforme
    :param a: is the acceleration
    :param w: is the speed in rad/s
    :param 0: is the start inclinaison
    :param t: is a time in second
    :param n: is the number of sample
    :param r: is the radius of the circle
    :return:
    """

    temps = np.linspace(0, t, n)

    positionX = []
    positionY = []

    for i in range(0, len(temps), 1):
        positionY.append(r * mt.cos(w * temps[i] + O))

        positionX.append(r * mt.sin(w * temps[i] + O))

    return (positionX, positionY)


def updateDistance(listeX, listeY, startX, startY):

    for i in range(0, len(listeX), 1):
        listeX[i] = listeX[i] + startX
        listeY[i] = listeY[i] + startY

    return (listeX, listeY)


def angMRUA(liste,angle):

    listeX = []
    listeY = []

    for i in range(0,len(liste),1):

        listeX.append(liste[i] * np.cos(angle))
        listeY.append(liste[i] * np.sin(angle))

    return(listeX,listeY)


def generateData():

    MRUX = MRUA(0, 30, 0, 60, 60)
    MRUY = liste0(len(MRUX), 250)

    MCUAx, MCUAy = MCUA(0, 0.1, 0, 250, 10, 10)
    MCUAx, MCUAy = updateDistance(MCUAx, MCUAy, MRUX[-1], 0)
    x,y = MRUX + MCUAx, MRUY + MCUAy

    Diag = MRUA(0, 50, 0, 120, 120)
    MRUX,MRUY = angMRUA(Diag,-3.14/3)
    MRUX,MRUY = updateDistance(MRUX,MRUY, x[-1], y[-1])
    x,y = x + MRUX, y + MRUY

    MRUY = MRUA(0, 5, y[-1], 120, 120)
    MRUX = liste0(len(MRUY), x[-1])
    x,y = x + MRUX , y + MRUY

    MCUAx, MCUAy = MCUA(0, 1, 0, 250, 3, 10)
    MCUAx, MCUAy = updateDistance(MCUAx, MCUAy, MRUX[-1], 0)
    x,y =  MCUAx, MCUAy

    print(x)
    print(y)

    ### tourth, I plot some data on a graph
    plt.title("Motion of the object on the X/Y surface")
    plt.scatter(x,y)
    plt.show()

    return(x,y)
