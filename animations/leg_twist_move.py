# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.52, 1.32, 2.12, 2.52, 2.92, 3.72, 4.52])
keys.append([0.11194, 0.208583, 0.223922, -0.0698132, 0.190175, 0.233125, -0.326783])

names.append("HeadYaw")
times.append([0.52, 1.32, 2.12, 2.92, 3.72, 4.52])
keys.append([-0.366584, 0.337438, 0.504645, -0.368202, -0.575292, -0.397349])

names.append("LAnklePitch")
times.append([0.44, 0.84, 1.24, 1.64, 2.04, 2.44, 2.84, 3.24, 3.64, 4.04, 4.44, 4.84])
keys.append([-0.0139626, 0.0383972, 0.022968, 0.066004, 0.024502, 0.066004, 0.022968, 0.066004, 0.024502, 0.066004, 0.022968, 0.066004])

names.append("LAnkleRoll")
times.append([0.44, 0.84, 1.24, 1.64, 2.04, 2.44, 2.84, 3.24, 3.64, 4.04, 4.44, 4.84])
keys.append([0.164061, 0.246091, 0.164061, 0.246091, 0.153589, 0.246091, 0.164061, 0.246091, 0.164061, 0.246091, 0.164061, 0.246091])

names.append("LElbowRoll")
times.append([0.48, 0.88, 1.28, 1.68, 2.08, 2.48, 2.88, 3.28, 3.68, 4.08, 4.48, 4.88])
keys.append([-1.50336, -1.48794, -1.47106, -1.47567, -1.47106, -1.54462, -1.38516, -1.54462, -1.03694, -1.50174, -0.77923, -1.31613])

names.append("LElbowYaw")
times.append([0.48, 0.88, 1.28, 1.68, 2.08, 2.48, 2.88, 3.28, 3.68, 4.08, 4.48, 4.88])
keys.append([-1.46646, -0.917375, -1.92522, -0.845275, -1.85925, -1.11066, -2.01418, -1.11066, -1.37757, -1.08765, -1.30854, -1.04623])

names.append("LHand")
times.append([0.48, 0.88, 1.28, 1.68, 2.08, 2.48, 2.88, 3.28, 3.68, 4.08, 4.48, 4.88])
keys.append([0.7932, 0.7924, 0.7924, 0.7932, 0.7944, 0.7944, 0.7944, 0.7932, 0.7932, 0.7936, 0.794, 0.794])

names.append("LHipPitch")
times.append([0.44, 0.84, 1.24, 1.64, 2.04, 2.44, 2.84, 3.24, 3.64, 4.04, 4.44, 4.84])
keys.append([0.445059, 0.199378, 0.438765, 0.199378, 0.445059, 0.199378, 0.438765, 0.199378, 0.445059, 0.199378, 0.438765, 0.199378])

names.append("LHipRoll")
times.append([0.44, 0.84, 1.24, 1.64, 2.04, 2.44, 2.84, 3.24, 3.64, 4.04, 4.44, 4.84])
keys.append([0.147306, -0.200996, 0.145772, -0.200996, 0.147306, -0.200996, 0.145772, -0.200996, 0.147306, -0.200996, 0.145772, -0.200996])

names.append("LHipYawPitch")
times.append([0.44, 0.84, 1.24, 1.64, 2.04, 2.44, 2.84, 3.24, 3.64, 4.04, 4.44, 4.84])
keys.append([-0.802851, -0.338973, -0.802241, -0.338973, -0.802851, -0.338973, -0.802241, -0.338973, -0.802851, -0.338973, -0.802241, -0.338973])

names.append("LKneePitch")
times.append([0.44, 0.84, 1.24, 1.64, 2.04, 2.44, 2.84, 3.24, 3.64, 4.04, 4.44, 4.84])
keys.append([-0.090548, -0.091998, -0.090548, -0.091998, -0.090548, -0.091998, -0.090548, -0.091998, -0.090548, -0.091998, -0.090548, -0.091998])

names.append("LShoulderPitch")
times.append([0.48, 0.88, 1.28, 1.68, 2.08, 2.48, 2.88, 3.28, 3.68, 4.08, 4.48, 4.88])
keys.append([1.86232, 1.73184, 2.01563, 1.626, 1.87297, 1.53703, 1.85611, 1.38363, 1.63213, 1.22102, 1.4864, 1.06149])

names.append("LShoulderRoll")
times.append([0.48, 0.88, 1.28, 1.68, 2.08, 2.48, 2.88, 3.28, 3.68, 4.08, 4.48, 4.88])
keys.append([0.14884, 0.176367, 0.11961, 0.085862, 0.0643861, 0.013764, -0.027654, 0.01223, 0.177901, 0.159494, 0.167164, 0.151824])

names.append("LWristYaw")
times.append([0.48, 0.88, 1.28, 1.68, 2.08, 2.48, 2.88, 3.28, 3.68, 4.08, 4.48, 4.88])
keys.append([1.17355, 1.17807, 1.175, 1.07989, 1.07529, 1.07529, 1.10444, 0.977116, 1.28698, 1.12745, 1.05842, 1.09217])

names.append("RAnklePitch")
times.append([0.44, 0.84, 1.24, 1.64, 2.04, 2.44, 2.84, 3.24, 3.64, 4.04, 4.44, 4.84])
keys.append([0.614356, -0.127409, 0.681137, -0.127409, 0.680678, -0.127409, 0.681137, -0.127409, 0.680678, -0.127409, 0.681137, -0.127409])

names.append("RAnkleRoll")
times.append([0.44, 0.84, 1.24, 1.64, 2.04, 2.44, 2.84, 3.24, 3.64, 4.04, 4.44, 4.84])
keys.append([0.208666, 0.37272, 0.208666, 0.37272, 0.208666, 0.37272, 0.208666, 0.37272, 0.208666, 0.37272, 0.208666, 0.37272])

names.append("RElbowRoll")
times.append([0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.6, 4, 4.4, 4.8])
keys.append([0.972513, 0.943452, 0.938849, 1.25639, 1.09532, 1.10145, 1.10145, 0.874422, 1.37451, 0.745566, 1.24718, 0.584497])

names.append("RElbowYaw")
times.append([0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.6, 4, 4.4, 4.8])
keys.append([1.25179, 0.570606, 1.55697, 0.748551, 1.40203, 0.724006, 1.7932, 0.961776, 1.53856, 1.02314, 1.66281, 0.88661])

names.append("RHand")
times.append([0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.6, 4, 4.4, 4.8])
keys.append([0.6364, 0.6356, 0.6356, 0.6356, 0.6356, 0.6356, 0.6356, 0.6348, 0.6348, 0.6348, 0.6348, 0.6348])

names.append("RHipPitch")
times.append([0.44, 0.84, 1.24, 1.64, 2.04, 2.44, 2.84, 3.24, 3.64, 4.04, 4.44, 4.84])
keys.append([-0.418879, -0.292952, -0.420357, -0.292952, -0.418879, -0.292952, -0.420357, -0.292952, -0.418879, -0.292952, -0.420357, -0.292952])

names.append("RHipRoll")
times.append([0.44, 0.84, 1.24, 1.64, 2.04, 2.44, 2.84, 3.24, 3.64, 4.04, 4.44, 4.84])
keys.append([0.0785398, -0.293036, 0.0798099, -0.293036, 0.0785398, -0.293036, 0.0798099, -0.293036, 0.0785398, -0.293036, 0.0798099, -0.293036])

names.append("RKneePitch")
times.append([0.44, 0.84, 1.24, 1.64, 2.04, 2.44, 2.84, 3.24, 3.64, 4.04, 4.44, 4.84])
keys.append([1.01862, 0.823715, 1.01862, 0.823715, 1.01862, 0.823715, 1.01862, 0.823715, 1.01862, 0.823715, 1.01862, 0.823715])

names.append("RShoulderPitch")
times.append([0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.6, 4, 4.4, 4.8])
keys.append([1.20261, 1.22111, 1.38218, 1.26559, 1.34843, 1.3699, 1.41286, 1.48495, 1.13213, 1.42359, 0.980268, 1.29474])

names.append("RShoulderRoll")
times.append([0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.6, 4, 4.4, 4.8])
keys.append([-0.033706, 0.0183661, -0.11049, -0.029188, -0.162646, -0.019984, -0.092082, -0.084412, 0.021434, -0.016916, 0.0199001, -0.0429939])

names.append("RWristYaw")
times.append([0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8, 3.2, 3.6, 4, 4.4, 4.8])
keys.append([-1.21335, -1.17048, -1.22417, -1.15668, -1.16895, -1.06004, -1.16895, -1.15361, -1.08305, -1.10299, -1.02782, -1.07998])
