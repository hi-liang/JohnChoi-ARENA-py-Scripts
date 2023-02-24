from arena import *

#ARENA SETTINGS
HOST = "mqtt.arenaxr.org"
NAMESPACE = "johnchoi"
SCENE = "NPC"

#DIALOGUE TREE FILE
DIALOGUE_FILENAME = "cartoon_dialogue.json"

#ENTER/EXIT SPECIAL EVENT NODES 
ENTER_INTERVAL = 100
ENTER_DISTANCE = 10
ENTER_NODE = "Start"
EXIT_NODE = "Exit"

#NPC (name Alphanumeric only plus '_', no spaces!)
NPC_NAME = "NPC_cactus"
NPC_GLTF_URL = "/store/users/johnchoi/Characters/Cactus/Cactus.gltf"

#NPC ROOT TRANSFORM
ROOT_SCALE = (2,2,2)
ROOT_POSITION = (2,0,0)
ROOT_ROTATION = (0,0,0)
ROOT_COLOR = (255,100,16)
ROOT_OPACITY = 0.3

#NPC GLTF TRANSFORM
GLTF_SCALE = (1,1,1)
GLTF_POSITION = (0,0,0)
GLTF_ROTATION = (0,180,0)

#SPEECH SETTINGS
SPEECH_INTERVAL = 100
SPEECH_TEXT_COLOR = (100,100,100)
SPEECH_TEXT_POSITION = (0,1,0)
SPEECH_TEXT_SCALE = (0.4,0.4,0.4)

#CHOICE SETTINGS
CHOICE_TEXT_COLOR = (0,0,0)
CHOICE_BUBBLE_COLOR = (200,200,200)
CHOICE_BUBBLE_POSITION = (0,0.2,0.6)
CHOICE_BUBBLE_OFFSET_Y = 0.1

#DEFAULT SOUNDS (set these to None if you don't want default sound effects)
SOUND_NEXT = Sound(positional=True, poolSize=1, autoplay=True, src="store/users/wiselab/audio/september.mp3"),
SOUND_CHOICE = Sound(positional=True, poolSize=1, autoplay=True, src="store/users/wiselab/audio/september.mp3"),
SOUND_ENTER = Sound(positional=True, poolSize=1, autoplay=True, src="store/users/wiselab/audio/september.mp3"),
SOUND_EXIT = Sound(positional=True, poolSize=1, autoplay=True, src="store/users/wiselab/audio/september.mp3"),
SOUND_TALKING = Sound(positional=True, poolSize=1, autoplay=True, src="store/users/wiselab/audio/september.mp3")

#DEFAULT ANIMATIONS (set these to None if you don't want default animations)
ANIM_IDLE = AnimationMixer(clip="idle", loop="repeat"),
ANIM_WALK = AnimationMixer(clip="walk", loop="repeat"),
ANIM_TALK = AnimationMixer(clip="talk", loop="repeat")