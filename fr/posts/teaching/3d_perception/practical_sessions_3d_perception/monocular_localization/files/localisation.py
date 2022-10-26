# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 00:35:00 2019

@author: thgerm
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

import matTools
import utils

EPS = 0.5
nb_segments = 5


def transform_and_draw_model(edges_Ro, intrinsic, extrinsic, fig_axis):
    # ********************************************************************* #
    # A COMPLETER.                                                          #
    # UTILISER LES FONCTIONS :                                              #
    #   - perspective_projection                                            #
    #   - transform_point_with_matrix                                       #
    # Input:                                                                #
    #   edges_Ro : ndarray[Nx6]                                              #
    #             N = nombre d'aretes dans le modele                        #
    #             6 = (X1, Y1, Z1, X2, Y2, Z2) les coordonnees des points   #
    #                 P1 et P2 de chaque arete                              #
    #   intrinsic : ndarray[3x3] - parametres intrinseques de la camera     #
    #   extrinsic : ndarray[4x4] - parametres extrinseques de la camera     #
    #   fig_axis : figure utilisee pour l'affichage                         #
    # Output:                                                               #
    #   Pas de retour de fonction, mais calcul et affichage des points      #
    #   transformes (u1, v1) et (u2, v2)                                    #
    # ********************************************************************* #

    P1_Rc = matTools.transform_point_with_matrix(extrinsic, edges_Ro[:, 0:3])
    P2_Rc = matTools.transform_point_with_matrix(extrinsic, edges_Ro[:, 3:6])
    [u1_Ri, v1_Ri] = perspective_projection(intrinsic, P1_Rc)
    [u2_Ri, v2_Ri] = perspective_projection(intrinsic, P2_Rc)

    for p in range(edges_Ro.shape[0]):
        fig_axis.plot([u1_Ri[p], u2_Ri[p]], [v1_Ri[p], v2_Ri[p]], 'k')


def perspective_projection(intrinsic, P_c):
    # ***************************************************** #
    # A COMPLETER.                                          #
    # Fonction utile disponible :                           #
    #   np.dot                                              #
    # Input:                                                #
    #   intrinsic : ndarray[3x3] - parametres intrinseques  #
    #   P_c : ndarray[Nx3],                                 #
    #         N = nombre de points à transformer            #
    #         3 = (X, Y, Z) les coordonnees des points      #
    # Output:                                               #
    #   u, v : deux ndarray[N] contenant les                #
    #          coordonnees Ri des points P_c transformes    #
    # ***************************************************** #

    s = P_c[:, 2]
    P_c[:, 0] = P_c[:, 0] / s
    P_c[:, 1] = P_c[:, 1] / s
    P_c[:, 2] = 1.0

    P_i = np.dot(intrinsic, P_c.T).T

    su = P_i[:, 0]
    sv = P_i[:, 1]

    return su, sv


def calculate_normal_vector(p1_Ri, p2_Ri, intrinsic):
    # ********************************************************* #
    # A COMPLETER.                                              #
    # Fonctions utiles disponibles :                            #
    #   np.dot, np.cross, np.linalg.norm, np.linalg.inv         #
    # Input:                                                    #
    #   p1_Ri : list[3]                                         #
    #           3 = (u, v, 1) du premier point selectionne      #
    #   p2_Ri : list[3]                                         #
    #           3 = (u, v, 1) du deuxieme point selectionne     #
    #   intrinsic : ndarray[3x3] des intrinseques               #
    # Output:                                                   #
    #   normal_vector : ndarray[3] contenant la normale aux     #
    #                   segments L1_c et L2_c deduits des       #
    #                   points image selectionnes               #
    # ********************************************************* #

    p1_Rc = np.dot(np.linalg.inv(intrinsic), p1_Ri)
    p2_Rc = np.dot(np.linalg.inv(intrinsic), p2_Ri)

    l1 = p1_Rc - 0
    l2 = p2_Rc - p1_Rc

    normal_vector = np.cross(l1, l2) / np.linalg.norm(np.cross(l1, l2))

    return normal_vector


def calculate_error(nb_segments, normal_vectors, segments_Rc):
    # ***************************************************************** #
    # A COMPLETER.                                                      #
    # Input:                                                            #
    #   nb_segments : par defaut 5 = nombre de segments selectionnes    #
    #   normal_vectors : ndarray[Nx3] - normales aux plans              #
    #                    d'interpretation des segments selectionnes     #
    #                    N = nombre de segments                         #
    #                    3 = coordonnees (X,Y,Z) des normales dans Rc   #
    #   segments_Rc : ndarray[Nx6] = segments selectionnes dans Ro      #
    #                 et transformes dans Rc                            #
    #                 N = nombre de segments                            #
    #                 6 = (X1, Y1, Z1, X2, Y2, Z2) des points P1 et     #
    #                 P2 des aretes transformees dans Rc                #
    # Output:                                                           #
    #   err : float64 - erreur cumulee des distances observe/attendu    #
    # ***************************************************************** #
    P1 = segments_Rc[:, 0:3].T
    P2 = segments_Rc[:, 3:6].T
    err = 0
    for p in range(nb_segments):
        # Partie a completer avec le calcul de l'erreur cumulee
        err = err + np.power(np.dot(normal_vectors[p], P1[:, p]), 2)
        err = err + np.power(np.dot(normal_vectors[p], P2[:, p]), 2)

    return np.sqrt(err / 2 * nb_segments)


def partial_derivatives(normal_vector, P_c):
    # ********************************************************************* #
    # A COMPLETER.                                                          #
    # Input:                                                                #
    #   normal_vector : ndarray[3] contenant la normale pour le segment     #
    #                   auquel appartient P_c                               #
    #   P_c : ndarray[3] le point de l'objet transformé dans Rc             #
    # Output:                                                               #
    #   partial_derivative : ndarray[6] derivee partielle du critere        #
    #               d'erreur pour chacun des parametres extrinseques        #
    #   crit_X0 : float64 - valeur du critere pour les parametres           #
    #               courants, qui servira de valeur initiale avant          #
    #               la mise a jour et le recalcul de l'erreur               #
    # ********************************************************************* #

    X, Y, Z = P_c[0], P_c[1], P_c[2]
    partial_derivative = np.zeros((6))
    # **************************************
    partial_derivative[0] = np.dot(normal_vector, np.array([0, -Z, Y]))
    partial_derivative[1] = np.dot(normal_vector, np.array([Z, 0, -X]))
    partial_derivative[2] = np.dot(normal_vector, np.array([-Y, X, 0]))
    partial_derivative[3] = normal_vector[0]
    partial_derivative[4] = normal_vector[1]
    partial_derivative[5] = normal_vector[2]
    # ********************************************************************
    crit_X0 = normal_vector[0] * X + normal_vector[1] * Y + normal_vector[2] * Z
    return partial_derivative, crit_X0


if __name__ == "__main__":

    pick_lines_Ro, normal_vectors, image, image_2, model3D_Ro, model3D_Ro_final, intrinsic_matrix, \
    Rc_to_Rc2_matrix = utils.select_segments()


    im_height, im_width, _ = image.shape

    print('Start optimization ...')

    param_solution = np.array([-2.1, 0.7, 2.7, 3.1, 1.3, 18])
    extrinsic_matrix = matTools.construct_matrix_from_vec(param_solution)

    # Homogeneous transformation
    pick_lines_Rc = np.copy(pick_lines_Ro)

    pick_lines_Rc[:, [0, 1, 2]] = matTools.transform_point_with_matrix(extrinsic_matrix, pick_lines_Ro[:, [0, 1, 2]])
    pick_lines_Rc[:, [3, 4, 5]] = matTools.transform_point_with_matrix(extrinsic_matrix, pick_lines_Ro[:, [3, 4, 5]])

    # Shows a projection of the selected (clicked) edges according to the initial pose value
    fig3 = plt.figure(3)
    ax3 = fig3.add_subplot(111)
    plt.imshow(image)
    transform_and_draw_model(model3D_Ro, intrinsic_matrix, extrinsic_matrix, ax3)  # 3D model
    # drawing
    plt.show(block=False)

    initial_error = calculate_error(nb_segments, normal_vectors, pick_lines_Rc)
    print('Initial criteria : ' + str(initial_error))

    l = 0.0001  # lambda value
    it = 0
    while True:
        J = np.zeros((2 * nb_segments, 6))
        F = np.zeros((2 * nb_segments))
        lig = 0

        pick_lines_Rc[:, [0, 1, 2]] = matTools.transform_point_with_matrix(extrinsic_matrix, pick_lines_Ro[:, [0, 1, 2]])
        pick_lines_Rc[:, [3, 4, 5]] = matTools.transform_point_with_matrix(extrinsic_matrix, pick_lines_Ro[:, [3, 4, 5]])

        for p in range(nb_segments):
            normal_vector = np.copy(normal_vectors[p, [0, 1, 2]])
            [partial_deriv, crit_X0] = partial_derivatives(normal_vector, pick_lines_Rc[p, [0, 1, 2]])
            J[lig, :] = partial_deriv.T
            F[lig] = -crit_X0
            lig = lig + 1

            [partial_deriv, crit_X0] = partial_derivatives(normal_vector, pick_lines_Rc[p, [3, 4, 5]])
            J[lig, :] = partial_deriv.T
            F[lig] = -crit_X0
            lig = lig + 1

        JJ = np.dot(J.T, J)
        for i in range(JJ.shape[0]):
            JJ[i, i] = JJ[i, i] * (1.0 + l)

        # ********************************************************************* #
        # A COMPLETER.
        delta_solution = np.dot(np.linalg.inv(JJ), np.dot(J.T, F))
        delta_extrinsic = matTools.construct_matrix_from_vec(delta_solution)
        extrinsic_matrix = np.dot(delta_extrinsic, extrinsic_matrix)
        # *******************************************************************

        param_solution = matTools.construct_vec_from_matrix(extrinsic_matrix)
        pick_lines_Rc[:, [0, 1, 2]] = matTools.transform_point_with_matrix(extrinsic_matrix, pick_lines_Ro[:, [0, 1, 2]])
        pick_lines_Rc[:, [3, 4, 5]] = matTools.transform_point_with_matrix(extrinsic_matrix, pick_lines_Ro[:, [3, 4, 5]])

        new_error = calculate_error(nb_segments, normal_vectors, pick_lines_Rc)
        if new_error < EPS or abs(initial_error - new_error) < 10 ** -10:
            break

        plt.imshow(image)
        transform_and_draw_model(pick_lines_Ro, intrinsic_matrix, extrinsic_matrix, ax3)  # 3D model drawing
        plt.show(block=False)

        print('Iteration[' + str(it) + '] : ' + str(new_error))
        it = it + 1
        initial_error = new_error

    print('6-tuplet solution : ' + str(param_solution))
    print('Error after convergence : ' + str(new_error))

    fig4 = plt.figure(4)
    ax4 = fig4.add_subplot(111)
    plt.imshow(image)
    transform_and_draw_model(model3D_Ro, intrinsic_matrix, extrinsic_matrix, ax4)  # 3D model drawing
    plt.show(block=False)

    fig5 = plt.figure(5)
    ax5 = fig5.add_subplot(111)
    ax5.set_xlim(0,720)
    ax5.set_ylim(480)
    plt.imshow(image_2)

    # A completer avec la matrice de passage du repere Ro vers Rc2, avec les matrices
    # Ro -> Rc et Rc -> Rc2
    Ro_to_Rc2 = np.dot(Rc_to_Rc2_matrix, extrinsic_matrix)

    transform_and_draw_model(model3D_Ro[12:], intrinsic_matrix, Ro_to_Rc2, ax5)
    plt.show(block = False)



    # A decommenter une fois la boucle d'optimisation codée
    fig6 = plt.figure(6)
    ax6, lines = utils.plot_3d_model(model3D_Ro_final, fig6)

    fig7 = plt.figure(7)
    ax7 = fig7.add_subplot(111)
    ax7.set_xlim(0, 720)
    plt.imshow(image)
    transform_and_draw_model(model3D_Ro_final[12:], intrinsic_matrix, extrinsic_matrix, ax7)  # 3D model drawing
    plt.show()