from naoqi import ALProxy
import time
from qi import Session
from robot.constants import JOINT_NAMES, NAO_PORT, NAO_IP
from robot.search import NaoNode, NaoState, NaoProblem, StandZero
# animations
# from animations import pensive_pose, relaxation_pose, rest_pose, scratchBottom_pose, scratchHead_pose, scratchHand_pose
# from animations import crying_pose, desperate_pose, desperate2_pose, desperate3_pose, disappointed_pose, embarassed_pose, crying_pose
from animations import excited_pose, excited2_pose, stretch1_pose, stretch2_pose, stretch3_pose
from animations import happy_seated_pose, excited_seated_pose, thinking5_seated_pose, thinking7_seated_pose, scratchHead_seated_pose
from animations import relieved_seated_pose, IdontKnow_seated_pose, hesitation_seated_pose
from animations import happy_pose, happy2_pose, happy3_pose, proud_pose, showMuscles1_pose, showMuscles2_pose, winner_pose, winner2_pose

from animations import disco_right_hand, disco_left_hand, two_hand_air_pose, one_hand_air_pose, shaking_head_pose, kisses_pose
from animations import sprinkler_pose, shaking_booty,hands_up_down_pose,introduction_pose, hello_wave, one_hand_air_rock_pose
from animations import wave_move, egyptian_twist_move, robot_dance_move, squats_dance_move, duck_dance_move, wipe_forehead
from animations import hand_near_eyes_retro_left, hand_near_eyes_retro_right, hand_near_eyes_retro, leg_twist_move, rolling_hands_left
from animations import rolling_hands_right, snap_right_move, snap_left_move, clapping_in_the_air, dance_move1,leg_hand_slip_dance_move
from animations import hand_swinging, stamp_foot_move, two_hand_air_rock_pose, bow_closing_move

class RobotManager:

	def __init__(self):
		self.connected = False
		self.session = Session()
		self.movePool1 = [kisses_pose,  introduction_pose, stretch1_pose, stretch2_pose, stretch3_pose,showMuscles1_pose, showMuscles2_pose] # before starting
		self.movePool2 = [sprinkler_pose, shaking_booty, hands_up_down_pose, one_hand_air_rock_pose, hand_near_eyes_retro, leg_hand_slip_dance_move]
		self.movePool3 = [wave_move, egyptian_twist_move, squats_dance_move, duck_dance_move,  disco_right_hand, disco_left_hand,  rolling_hands_right , rolling_hands_left]
		self.movePool4 = [hand_near_eyes_retro_left, hand_near_eyes_retro_right, hand_near_eyes_retro, leg_twist_move, rolling_hands_left, rolling_hands_right]
		self.movePool5 = [rolling_hands_right, snap_right_move, snap_left_move, clapping_in_the_air, dance_move1, leg_hand_slip_dance_move, shaking_head_pose]
		self.movePool6 = [hand_swinging, stamp_foot_move, two_hand_air_rock_pose, robot_dance_move, two_hand_air_pose, one_hand_air_pose]
		self.movePool7 = [ kisses_pose,  introduction_pose, winner_pose, winner2_pose, excited_pose,excited2_pose, lookHand_pose,proud_pose,happy_pose ] # for exiting

	def robotConnect(self):
		print("robot trying to connect")
		try:
			self.textSpeakProxy = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
			self.postureProxy = ALProxy("ALRobotPosture", NAO_IP, NAO_PORT)
			self.motionProxy = ALProxy("ALMotion", NAO_IP, NAO_PORT)
			self.session.connect("tcp://" + NAO_IP + ":" + str(NAO_PORT))
			self.connected = True
			print("robot connected")

		except RuntimeError:
			print ("Can't connect to Naoqi at ip \"" + NAO_IP + "\" on port " + str(NAO_PORT) + ".\n")


	def initRobot(self):
		if self.connected:
			self.postureProxy.goToPosture("StandInit", 1.0)
			self.textSpeakProxy.post.say("Hello")
			self.motionProxy.setFallManagerEnabled(True)

## Dance timeline:
## StandInit -> A1(introductory moves) -> hello_wave -> A2(dance)-> StandZero ->
## -> A3(dance with squat)-> Sit -> A4(sitted poses)-> SitRelax -> A5(dances) ->
## -> Stand -> A6(last dance moves)-> wipe_forehead -> A7(finishing moves) -> Crouch
##
	def planning(self):
		print(self.postureProxy.getPostureList())
		# listOfMoves = ["Stand", "StandZero", "Sit", "SitRelax"]
		# for move in listOfMoves:
		# 	time.sleep(1)
		# 	self.postureProxy.goToPosture(move, 0.7)
		# self.textSpeakProxy.post.say("Tired")
		self.runMotion(introduction_pose)
		self.runMotion(bow_closing_move)

	def onFinish(self):
		self.textSpeakProxy.post.say("Bye!")
		self.postureProxy.goToPosture("Crouch", 0.5)

	def runMotion(self, pose, post = True):
		# launch animation
		# if post == True:
		# 	self.motionProxy.post.angleInterpolationBezier(pose.names, pose.times, pose.keys)
		# else:
		self.motionProxy.angleInterpolationBezier(pose.names, pose.times, pose.keys)
