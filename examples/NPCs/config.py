#DIALOGUE TREE FILE
DIALOGUE_FILENAME = "actions.json"

#ARENA SETTINGS
FILESTORE = "https://arenaxr.org/" #main server
HOST = "mqtt.arenaxr.org"          #main server
NAMESPACE = "johnchoi"
SCENE = "NPC"

#DEVELOPER DEBUG SETTINGS
USE_DEV_ARENAPY = True
ARENAPY_DEV_PATH = "D:/Github/arena-py/"  # Linux/Mac (Civilized)
ARENAPY_DEV_PATH = "D:\\Github\\arena-py" # Windows   (Uncivilized)

USE_DEV_SERVER = False
if(USE_DEV_SERVER):
    HOST = "arena-dev1.conix.io" #dev server
if(USE_DEV_SERVER):
    FILESTORE = "https://arena-dev1.conix.io/" #dev server

PRINT_VERBOSE = False

#NPC (name Alphanumeric only plus '_', no spaces!)
NPC_NAME = "NPC_JunkoChan2"
NPC_GLTF_URL = FILESTORE+"store/users/johnchoi/Characters/JunkoChan/JunkoChan.glb"

#ENTER/EXIT SPECIAL EVENT NODES 
ENTER_INTERVAL = 100
ENTER_DISTANCE = 10
ENTER_NODE = "Enter"
EXIT_NODE = "Exit"

#NO ACTIVITY RESET
RESET_INTERVAL = 100
RESET_TIME = 300000 #5 min of no activity resets interaction.

#MISCELLANEOUS
TRANSFORM_TIMER = 3000
UUID_LEN = 6

#USE DEFAULT ACTIONS
USE_DEFAULT_ANIMATIONS = True
USE_DEFAULT_MORPHS = True
USE_DEFAULT_SOUNDS = True

#NPC ROOT TRANSFORM
ROOT_SCALE = (1,1,1)
ROOT_POSITION = (0,0,0)
ROOT_ROTATION = (0,0,0)
ROOT_COLOR = (255,100,16)
ROOT_OPACITY = 0.5

#NPC GLTF TRANSFORM
GLTF_SCALE = (1,1,1)
GLTF_POSITION = (0,0,0)
GLTF_ROTATION = (0,0,0) #radians, not degrees??

#NPC PLANE SETTINGS (for both images and videos)
PLANE_SCALE = 1.2
PLANE_SCALE_DURATION = 500
PLANE_POSITION = (1.5,1.2,0)
PLANE_ROTATION = (0,-15,0) #radians, not degrees??
PLANE_OPACITY = 0.9

#SPEECH SETTINGS
SPEECH_INTERVAL = 100
SPEECH_SPEED = 3
SPEECH_TEXT_COLOR = (50,120,100)
SPEECH_TEXT_POSITION = (0,2.2,0)
SPEECH_TEXT_SCALE = (0.6,0.7,0.7)

#CHOICE SETTINGS
CHOICE_TEXT_COLOR = (255,255,255)
CHOICE_BUBBLE_COLOR = (0,0,200)
CHOICE_BUBBLE_OPACITY = 0.5

CHOICE_BUBBLE_POSITION = (-0.9,0.2,0.7)
CHOICE_BUBBLE_ROTATION = (0,15,0)
CHOICE_BUBBLE_OFFSET_Y = 0.25

CHOICE_BUBBLE_SCALE = (1, 0.2, 0.08)
CHOICE_TEXT_SCALE = (0.3, 2, .5)

CHOICE_SCALE_DURATION = 500