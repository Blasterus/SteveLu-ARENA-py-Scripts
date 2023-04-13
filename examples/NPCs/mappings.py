from config import *

import sys
if(USE_DEV_ARENAPY):
    sys.path.append(ARENAPY_DEV_PATH)

from arena import *

#---PRE-DEFINED DEFAULT ACTIONS (triggered when talking/moving/clicking/etc)---#

#DEFAULT SOUNDS (set these to None if you don't want default sound effects, or set USE_DEFAULT_SOUNDS = False)
SOUND_NEXT    = Sound(volume=1.0, autoplay=True, positional=True, src=FILESTORE+"store/users/johnchoi/Sounds/NPC/Next.wav")
SOUND_CHOICE  = Sound(volume=1.0, autoplay=True, positional=True, src=FILESTORE+"store/users/johnchoi/Sounds/NPC/Choice.wav")
SOUND_ENTER   = Sound(volume=0.8, autoplay=True, positional=True, src=FILESTORE+"store/users/johnchoi/Sounds/NPC/Enter.wav")
SOUND_EXIT    = Sound(volume=0.8, autoplay=True, positional=True, src=FILESTORE+"store/users/johnchoi/Sounds/NPC/Exit.wav")
SOUND_IMAGE   = Sound(volume=0.8, autoplay=True, positional=True, src=FILESTORE+"store/users/johnchoi/Sounds/NPC/Enter.wav")
SOUND_TALKING = Sound(volume=1.0, autoplay=True, positional=True, src=FILESTORE+"store/users/johnchoi/Sounds/NPC/Talking.wav")
SOUND_WALKING = Sound(volume=1.0, autoplay=True, positional=True, src=FILESTORE+"store/users/johnchoi/Sounds/NPC/Walking.wav") #Not applied yet, TODO

#DEFAULT ANIMATIONS (set these to None if you don't want default animations, or set USE_DEFAULT_ANIMATIONS = False)
ANIM_IDLE = AnimationMixer(clip="Idle", loop="repeat", timeScale = 1, crossFadeDuration=0.5)
ANIM_WALK = AnimationMixer(clip="Walk", loop="repeat", timeScale = 2, crossFadeDuration=0.5)
ANIM_TALK = AnimationMixer(clip="NailGun_Idle", loop="repeat", timeScale = 1, crossFadeDuration=0.5)

#DEFAULT MORPHS (set these to None if you don't want default morphs, or set USE_DEFAULT_MORPHS = False)
MORPH_OPEN  = [Morph(morphtarget="eyeTop",value=0.0), Morph(morphtarget="eyeBottom",value=0.0)]
MORPH_CLOSE = [Morph(morphtarget="eyeTop",value=0.0), Morph(morphtarget="eyeBottom",value=0.0)]
MORPH_BLINK = [Morph(morphtarget="eyeTop",value=0.0), Morph(morphtarget="eyeBottom",value=0.0)]
MORPH_RESET = [Morph(morphtarget="eyeTop",value=0.0), Morph(morphtarget="eyeBottom",value=0.0)]

#DEFAULT VIDEO LOADING FRAME
DEFAULT_VIDEO_FRAME_OBJECT = FILESTORE+"store/users/wiselab/images/conix-face-white.jpg"

#DEFAULT TRANSFORM 
TRANSFORM_RESET = [ Animation(property="position", end=ROOT_POSITION, easing="easeInOutSine", dur=TRANSFORM_TIMER), 
                    Animation(property="rotation", end=ROOT_ROTATION, easing="linear", dur=TRANSFORM_TIMER*0.5) ]

#---PRE-DEFINED QUICK ACTION MAPPINGS (for use in Yarn, because who wants to type all this out every time?)---#

# Shorthand sound names mapped to (Sound URL, volume, loop)
# --Sound Schema: https://docs.arenaxr.org/content/schemas/message/sound.html
# --Sound Example: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/sound.py 
soundMappings = {
    "next"    : Sound(volume=1.0, autoplay=True, positional=True, src=FILESTORE+"store/users/johnchoi/Sounds/NPC/Next.wav"),
    "choice"  : Sound(volume=1.0, autoplay=True, positional=True, src=FILESTORE+"store/users/johnchoi/Sounds/NPC/Choice.wav"),
    "enter"   : Sound(volume=0.8, autoplay=True, positional=True, src=FILESTORE+"store/users/johnchoi/Sounds/NPC/Enter.wav"),
    "exit"    : Sound(volume=0.8, autoplay=True, positional=True, src=FILESTORE+"store/users/johnchoi/Sounds/NPC/Exit.wav"),
    "talking" : Sound(volume=1.0, autoplay=True, positional=True, src=FILESTORE+"store/users/johnchoi/Sounds/NPC/Talking.wav")
}

# Shorthand animation names mapped to (animationName, crossFade, timeScale, loopMode['once', 'repeat', 'pingpong'])
# --AnimationMixer Schema: https://docs.arenaxr.org/content/schemas/message/animation-mixer.html 
# --AnimationMixer Example: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/animation_mixer.py 
animationMappings = {
    "idle"   : AnimationMixer(clip="Idle", loop="repeat", crossFadeDuration=0.5, timeScale = 1),
    "walk"   : AnimationMixer(clip="Walk", loop="repeat", crossFadeDuration=0.5, timeScale = 1),
    "talk"   : AnimationMixer(clip="NailGun_Idle", loop="repeat", crossFadeDuration=0.5, timeScale = 1),
    "crouch" : AnimationMixer(clip="Crouch", loop="repeat", crossFadeDuration=0.5, timeScale = 1),
    "jump"   : AnimationMixer(clip="Jump", loop="once", crossFadeDuration=0.5, timeScale = 1),
    "happy"  : AnimationMixer(clip="Happy", loop="once", crossFadeDuration=0.5, timeScale = 1)
}

# Shorthand transform names mapped to transform action over time
# --Animation Schema: https://docs.arenaxr.org/content/schemas/message/animation.html 
# --Animation Example: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/animation.py 
transformMappings = {
    "point0" : [              
        Animation(property="position", end=(0,0,0), easing="easeInOutSine", dur=TRANSFORM_TIMER),  
        Animation(property="rotation", end=(0,0,0), easing="linear", dur=TRANSFORM_TIMER*0.5)
    ],
    "point1" : [              
        Animation(property="position", end=(0,0,0), easing="easeInOutSine", dur=TRANSFORM_TIMER),  
        Animation(property="rotation", end=(0,0,0), easing="linear", dur=TRANSFORM_TIMER*0.5)
    ],
    "point2" : [              
        Animation(property="position", end=(0,0,-10), easing="easeInOutSine", dur=TRANSFORM_TIMER),  
        Animation(property="rotation", end=(0,300,0), easing="linear", dur=TRANSFORM_TIMER*0.5)
    ],
    "point3" : [              
        Animation(property="position", end=(10,0,0), easing="easeInOutSine", dur=TRANSFORM_TIMER),
        Animation(property="rotation", end=(0,180,0), easing="linear", dur=TRANSFORM_TIMER*0.5)
    ],
    "point4" : [              
        Animation(property="position", end=(10,0,0), easing="easeInOutSine", dur=TRANSFORM_TIMER),
        Animation(property="rotation", end=(0,180,0), easing="linear", dur=TRANSFORM_TIMER*0.5)
    ]
}

# Shorthand morph names mapped to list of morph target names with weights
# --Morph Schema: https://docs.arenaxr.org/content/python/animations.html#gltf-morphs
# --Morph Example: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/morph.py
morphMappings = {
    "smile"  : (Morph(morphtarget="Smile",value=1.0)),
    "blink"  : (Morph(morphtarget="Blink",value=1.0)),
    "open"   : (Morph(morphtarget="a",value=1.0)),
    "squint" : (Morph(morphtarget="><",value=1.0)),
    "dizzy"  : (Morph(morphtarget="@@",value=1.0)),
    "reset"  : (Morph(morphtarget="Smile",value=0.0), Morph(morphtarget="Blink",value=0.0))
}

# Shorthand url names mapped to (Website URL, volume, loop)
# --Url Schema: https://docs.arenaxr.org/content/schemas/message-examples.html#goto-url 
# --Url Example: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/goto_url.py 
urlMappings = {
    "youtube"   : GotoUrl(dest="popup", on="mouseup", url="https://www.youtube.com/watch?v=cBkWhkAZ9ds"),
    "wikipedia" : GotoUrl(dest="popup", on="mouseup", url="https://en.wikipedia.org/wiki/Fish"),
    "arena"     : GotoUrl(dest="popup", on="mouseup", url="https://arenaxr.org/"),
    "conix"     : GotoUrl(dest="newtab", on="mouseup", url="https://conix.io/"),
    "island"    : GotoUrl(dest="sametab", on="mouseup", url="https://arenaxr.org/public/island")    
}

# Shorthand image names mapped to (Website URL, volume, loop)
# --Url Schema: https://github.com/arenaxr/arena-py/blob/master/examples/objects/image.py
# --Url Example: https://docs.arenaxr.org/content/schemas/message/image.html
class IMG:
    def __init__(self, url, w, h, size):
        self.url = url
        self.w = w
        self.h = h
        self.size = size
        
imageMappings = {
    "doge"        : IMG(url = FILESTORE+"store/users/johnchoi/Images/doge.jpg", w = 369, h = 273, size = 1),
    "dragon"      : IMG(url = FILESTORE+"store/users/johnchoi/Images/dragon.jpg", w = 1200, h = 1200, size = 1),
    "exclamation" : IMG(url = FILESTORE+"store/users/johnchoi/Images/exclamation.png", w = 920, h = 951, size = 1),
    "fish"        : IMG(url = FILESTORE+"store/users/johnchoi/Images/fish.jpg", w = 800, h = 450, size = 1),
    "forest"      : IMG(url = FILESTORE+"store/users/johnchoi/Images/forest.jpg", w = 1500, h = 1000, size = 1),
    "graph"       : IMG(url = FILESTORE+"store/users/johnchoi/Images/graph.png", w = 918, h = 669, size = 1),
    "meme"        : IMG(url = FILESTORE+"store/users/johnchoi/Images/meme.jpg", w = 800, h = 450, size = 1),
    "nyan"        : IMG(url = FILESTORE+"store/users/johnchoi/Images/nyan.jpg", w = 800, h = 450, size = 1),
    "question"    : IMG(url = FILESTORE+"store/users/johnchoi/Images/question.png", w = 360, h = 480, size = 1),
    "potato"      : IMG(url = FILESTORE+"store/users/johnchoi/Images/potato.jpg", w = 1920, h = 1080, size = 1),
    "stonks"      : IMG(url = FILESTORE+"store/users/johnchoi/Images/stonks.png", w = 680, h = 510, size = 1),
    "sushi"       : IMG(url = FILESTORE+"store/users/johnchoi/Images/sushi.jpg", w = 1240, h = 1995, size = 1)
}

# Shorthand image names mapped to (Website URL, volume, loop)
# --Url Schema: https://docs.arenaxr.org/content/schemas/message/material.html#material
# --Url Example: https://github.com/arenaxr/arena-py/blob/master/examples/attributes/material.py
videoMappings = {
    #Src Video Material Method
    "rays"       : Material(src = FILESTORE+"store/users/johnchoi/Videos/rays.mp4", transparent = True, opacity = PLANE_OPACITY, w = 1920, h = 1080, size = 1),
    "hydroponic" : Material(src = FILESTORE+"store/users/johnchoi/Videos/hydroponic.mp4", transparent = True, opacity = PLANE_OPACITY, w = 1920, h = 1080, size = 1),
    "greenhouse" : Material(src = FILESTORE+"store/users/johnchoi/Videos/greenhouse.mp4", transparent = True, opacity = PLANE_OPACITY, w = 1920, h = 1080, size = 1)
    
    #VideoControl Method
    #"rays"       : VideoControl(video_path = FILESTORE+"store/users/johnchoi/Videos/rays.mp4", frame_object = DEFAULT_VIDEO_FRAME_OBJECT, video_object = None, anyone_clicks = True, video_loop = True, autoplay = True, volume = 1, w = 1920, h = 1080, size = 1),
    #"hydroponic" : VideoControl(video_path = FILESTORE+"store/users/johnchoi/Videos/hydroponic.mp4", frame_object = DEFAULT_VIDEO_FRAME_OBJECT, video_object = None, anyone_clicks = True, video_loop = True, autoplay = True, volume = 1, w = 1920, h = 1080, size = 1),
    #"greenhouse" : VideoControl(video_path = FILESTORE+"store/users/johnchoi/Videos/greenhouse.mp4", frame_object = DEFAULT_VIDEO_FRAME_OBJECT, video_object = None, anyone_clicks = True, video_loop = True, autoplay = True, volume = 1, w = 1920, h = 1080, size = 1)
}