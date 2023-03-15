#ARENA SETTINGS
HOST = "mqtt.arenaxr.org"
NAMESPACE = "johnchoi"
SCENE = "NPC"

#DIALOGUE TREE FILE
DIALOGUE_FILENAME = "actions.json"

#ENTER/EXIT SPECIAL EVENT NODES 
ENTER_INTERVAL = 100
ENTER_DISTANCE = 10
ENTER_NODE = "Enter"
EXIT_NODE = "Exit"

#NPC (name Alphanumeric only plus '_', no spaces!)
NPC_NAME = "NPC_JunkoChan2"
NPC_GLTF_URL = "/store/users/johnchoi/Characters/JunkoChan/JunkoChan.glb"

#MISCELLANEOUS
UUID_LEN = 6
TRANSFORM_TIMER = 3000
DTR = 0.01745329251

#USE DEFAULT ACTIONS
USE_DEFAULT_ANIMATIONS = True
USE_DEFAULT_MORPHS = True
USE_DEFAULT_SOUNDS = True

#NPC ROOT TRANSFORM
ROOT_SCALE = (2,2,2)
ROOT_POSITION = (0,0,0)
ROOT_ROTATION = (0,0,0)
ROOT_COLOR = (255,100,16)
ROOT_OPACITY = 0.3

#NPC GLTF TRANSFORM
GLTF_SCALE = (.5,.5,.5)
GLTF_POSITION = (0,0,0)
GLTF_ROTATION = (0,180*DTR,0) #radians, not degrees??

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

CHOICE_BUBBLE_SCALE = (0.4, 0.08, 0.04)
CHOICE_TEXT_SCALE = (0.5, 2, 1)
