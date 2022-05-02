import numpy as np


def transposeLineToVect (vect):

    vect2 = np.zeros((len(vect),1))

    for i in range(0,len(vect),1):

        vect2[i,0] = vect[i]

    return(vect2)

def transposeVectToLine(vect) :

    vect2 = np.zeros(len(vect))

    for i in range(0,len(vect),1):

        vect2[i] = vect[i,0]

    return(vect2)



def KALMAN(deltaT,Y):

    # matrice d'observation

    X_k_1 = np.array([[0],
                      [0]])

    H = np.array([1,0])




    P_k_1 = np.array([[0.01,0],
                      [0,1]])

    Q_k_1 = np.array([[0.1,0],
                      [0,0.1]])

    listePrediction = []
    listeCorrection = []

    for i in range(0,len(Y),1):
        F_k_1 = np.array([[1, i],
                          [0, 1]])

        # étape 1 - prédiction
        # prédiction de la position
        x_k = F_k_1 @ X_k_1
        # estimation de la covariance de l 'erreur
        p_k = F_k_1 @ P_k_1 @ np.transpose(F_k_1) + Q_k_1

        # étape 2 - Correction
        # Gain optimal ou gain de kalman
        K = p_k @ transposeLineToVect(H) * (H @ p_k @ transposeLineToVect(H) + 0.05)**(-1)
        # correction de la position avec l'estimation et la mesure

        #print(" ******* test n° : ", i , " '***** ")
        #print("prediction = ",x_k[0,0])

        listePrediction.append(x_k[0,0])

        X_k_1 = x_k + K * (Y[i] - H @ x_k)

        #print("correction = ", X_k_1[0,0])
        listeCorrection.append(X_k_1[0,0])

        #print("orginal = ",Y[i])
        # correction de la covarience de l'erreur
        P_k_1 = (1 - H @ K) * p_k

        # remarque: si l'objet disparait pendant un certain temps, on ne fait pas la correction

    return(listePrediction,listeCorrection)
