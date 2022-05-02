import numpy as np
import math as mt
import matplotlib.pyplot as plt


def MRUA(a: int, v: int, d: int, t: int, cst: int):
    """
    MRUA = Mouvement rectiligne uniforme accelérée
    :param a: is the acceleration
    :param v: is the speed
    :param d: is the start position
    :param t: is a time in second
    :return: dataX,dataY: it's a list of point
    """
    n = t
    temps = np.linspace(0, t, n)
    dataX = []
    dataY = []

    for i in range(0, n, 1):
        X = a * (temps[i] ** (2)) + v * temps[i] + d
        dataX.append(X)
        dataY.append(cst)

    return(dataX,dataY)


def angMRUA(liste: list ,angle: float , startX: int, startY: int, stateX:int, stateY:int):
    """
    function used for inclinate a MRUA on the space
    :param liste:  data
    :param angle:  angle uses for the inclinaison of the translation
    :param startX: last position of X before the motion
    :param startY: last position of Y before the motion
    :param stateX:
    :param stateY:
    :return:
    """
    listeX,listeY = [],[]

    for i in range(0,len(liste),1):
        listeX.append(startX + stateX*liste[i] * np.sin(angle))
        listeY.append(startY + stateY*liste[i] * np.cos(angle))

    return(listeX,listeY)


def MCUA(w: int, O: int, r: int, t: int, startX: int, startY: int):
    """
    MCU = Mouvement circulaire uniforme
    :param w: is the speed in rad/s
    :param 0: is the start inclinaison
    :param t: is a time in second
    :param n: is the number of sample
    :param r: is the radius of the circle
    :return:
    """
    n = t
    temps = np.linspace(0, t, n)
    dataX = []
    dataY = []

    for i in range(0, n, 1):
        dataX.append(startX + r * mt.cos(w * temps[i] + O))
        dataY.append(startY + r * mt.sin(w * temps[i] + O))

    return (dataX,dataY)


def inv(liste):

    newListe =[]

    for i in range(1,len(liste)+1,1):
        newListe.append(liste[len(liste)-i])

    return(newListe)




def generateData():

    x,y = MRUA(0, 30, 0, 60, 250)

    ybis, xbis = MCUA(0.1, 0 , 250 ,20 , 0,x[-1])
    x,y = x + xbis, y + ybis

    xbis,ybis = MRUA(0, 40, 0, 60, 0)
    xbis,ybis = angMRUA(xbis,np.pi/3 + np.pi,x[-1],y[-1],1,1)
    x,y = x + xbis, y + ybis

    ybis, xbis = MCUA(0.1, np.pi, 250, 20, y[-1] - 100,x[-1])
    x,y = x + xbis, y + inv(ybis)

    xbis,ybis = MRUA(0, 20, x[-1], 10, y[-1])
    x,y = x + xbis, y + ybis



    ### tourth, I plot some data on a graph
    plt.title("Motion of the object on the X/Y surface")
    plt.scatter(x,y)
    plt.show()

    return(x,y)
