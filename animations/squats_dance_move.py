# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.48, 0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.96])
keys.append([0.247837, -0.0690719, -0.0706059, -0.150374, -0.0706059, -0.0874799, 0.0183661, -0.0798099, -0.073674, -0.150374, -0.319395, 0.49544])

names.append("HeadYaw")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.96])
keys.append([-0.032256, -0.0414599, -0.038392, -0.0414599, -0.027654, -0.250085, -0.038392, -0.047596, -0.038392, 0.446352])

names.append("LAnklePitch")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.96])
keys.append([0.024502, 0.032172, -0.714885, 0.032172, 0.030638, 0.0812601, 0.033706, 0.033706, -0.714885, -0.224006, -0.2102])

names.append("LAnkleRoll")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.96])
keys.append([-0.013764, -0.016832, 0.075208, -0.016832, -0.016832, 0.104354, -0.0199001, -0.0199001, 0.075208, -0.05058, 0.019984])

names.append("LElbowRoll")
times.append([0.48, 0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.56, 5.96])
keys.append([-1.28107, -1.39897, -1.38363, -1.38363, -1.38363, -1.37902, -1.36062, -1.36062, -1.38209, -1.38363, -0.921534, -0.249999])

names.append("LElbowYaw")
times.append([0.48, 0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.56, 5.96])
keys.append([-0.60912, -0.0798099, -0.0706059, -0.0966839, -0.0706059, -0.0629359, 0.116542, -0.032256, -4.19617e-05, -0.0966839, -0.0314159, -0.994838, -1.3653])

names.append("LHand")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.56, 5.96])
keys.append([0.3, 0.3036, 0.3032, 0.3036, 0.302, 0.3024, 0.3024, 0.3024, 0.3032, 0.5, 0.7312])

names.append("LHipPitch")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.96])
keys.append([0.395814, 0.397349, -0.578276, 0.397349, 0.397349, 0.236277, 0.392746, 0.392746, -0.578276, 0.0951499, -0.558334])

names.append("LHipRoll")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.96])
keys.append([0.029188, 0.0337899, -0.041376, 0.0337899, 0.0337899, -0.332836, 0.038392, 0.038392, -0.041376, 0.104354, 0.131966])

names.append("LHipYawPitch")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.96])
keys.append([-0.282215, -0.283749, -0.645772, -0.283749, -0.283749, -0.302157, -0.28068, -0.28068, -0.645772, -0.366584, -0.71787])

names.append("LKneePitch")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.96])
keys.append([-0.0923279, -0.092082, 1.7119, -0.092082, -0.090548, -0.090548, -0.092082, -0.092082, 1.7119, 0.415673, 0.866668])

names.append("LShoulderPitch")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.56, 5.96])
keys.append([0.059784, 0.0797261, -0.153442, -0.0785398, -0.058334, -0.174919, -0.0506639, -0.0429939, -0.153442, -0.443314, -0.18326, 1.50021])

names.append("LShoulderRoll")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.96])
keys.append([-0.314159, -0.296104, -0.300706, -0.296104, -0.29457, -0.314159, -0.314159, -0.311444, -0.300706, 0.325165])

names.append("LWristYaw")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.56, 5.96])
keys.append([0.0643861, 0.068988, -0.0353239, 0.068988, 0.068988, -0.082878, 0.05825, 0.0475121, -0.0353239, -0.907571, 0.519984])

names.append("RAnklePitch")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.96])
keys.append([0.0414599, 0.038392, -0.748551, 0.038392, 0.039926, -0.401866, 0.0429939, 0.0429939, -0.748551, -0.091998, 0.121228])

names.append("RAnkleRoll")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.96])
keys.append([-0.0475121, -0.0459781, -0.078192, -0.0459781, -0.0444441, 0.0767419, -0.0444441, -0.0444441, -0.078192, -0.0260361, 0.0245859])

names.append("RElbowRoll")
times.append([0.48, 0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.56, 5.96])
keys.append([1.09258, 1.21344, 1.19349, 1.2027, 1.23395, 1.20883, 1.50643, 1.22111, 1.22878, 1.2027, 0.780162, 0.075208])

names.append("RElbowYaw")
times.append([0.48, 0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.56, 5.96])
keys.append([0.844739, -0.066004, -0.0782759, -0.055266, 0.010472, -0.00157596, 0.351244, -0.00924597, -0.016916, -0.055266, -0.481711, 1.08036, 1.0845])

names.append("RHand")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.56, 5.96])
keys.append([0.3, 0.3024, 0.3024, 0.3024, 0.3028, 0.3028, 0.3028, 0.3028, 0.3024, 0.5, 0.8156])

names.append("RHipPitch")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.96])
keys.append([0.38806, 0.386526, -0.605971, 0.386526, 0.386526, -0.372804, 0.392662, 0.392662, -0.605971, 0.199378, 0.289883])

names.append("RHipRoll")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.96])
keys.append([0.0261199, 0.023052, -0.010696, 0.023052, 0.023052, -0.29602, 0.0184499, 0.0184499, -0.010696, 0.0337899, 0.233209])

names.append("RKneePitch")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.96])
keys.append([-0.087396, -0.087396, 1.758, -0.087396, -0.0889301, 0.929646, -0.0923279, -0.091998, 1.758, 0.200996, -0.0923279])

names.append("RShoulderPitch")
times.append([0.48, 0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.16, 5.56, 5.96])
keys.append([0.860447, 0.527739, 0.559952, 0.289967, 0.417134, 0.449504, 0.900499, 0.513931, 0.570689, 0.289967, -0.18326, 0.1309, 1.14747])

names.append("RShoulderRoll")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.96])
keys.append([0.288349, 0.259204, 0.279146, 0.259204, 0.260738, 0.0352401, 0.223922, 0.194775, 0.279146, 0.217786])

names.append("RWristYaw")
times.append([0.96, 1.16, 1.76, 2.36, 2.56, 3.16, 3.76, 3.96, 4.56, 5.56, 5.96])
keys.append([-0.270526, -0.291501, -0.365133, -0.291501, -0.26389, -0.934249, -0.30224, -0.335988, -0.365133, 0.551524, -0.527739])
