from DataGenerator import*
from traitement import*
from filtre import*
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    ### In a first time, I will generate a motion with a specific speed
    x,y = generateData()

    """
    listePredictionX,listeCorrectionX = KALMAN(1, x)
    listePredictionY,listeCorrectionY =KALMAN(1, y)

    plt.scatter(x,y,color="red")
    plt.scatter(listePredictionX,listePredictionY,color="green")
    plt.scatter(listeCorrectionX,listePredictionY,color="blue")
    plt.legend(["original", "prediction", "correction"])
    plt.xlabel('X position')
    plt.ylabel('Y position')
    plt.title('Evolution of an object motion with a kalman filter')
    plt.show()"""


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
