Glossary
--------

This page is a list of common Unity terms.  It will be updated each week to cover new ideas introduced in the lesson.

Asset
=======  All of the digital pieces which make up a game are known as 'assets'.  A texture map, a model file, or a file on disk that tells how much health your character begins the game with are all examples of assets. Unity stores assets in the [Project Folder](#projectfolder)

Bake
=======
Calculating and storing complex computations ahead of time is known as 'baking'. [Lightmaps](#lightmap), for example, are 'baked' diffuse illumination.  Baked data is usually more efficient to compute (thus better for CPU performance) but uses a lot of memory.

Bone
======= 
The hierarchy of [transforms](#transform) that make up a [skinned](#skin) model are called bones.  Bones are usually animated outside of Unity but they can also be controlled by scripts.

Budget
=======
Games are limited by available memory and computing power. If the game demands too much memory (for example, because it's trying to draw a very complex 3d scene) or two much processing power (if it is attempting some extremely difficult calculations) it will slow down. For this reason most game teams set a __budget__ for the amount of memory and computation they can use at a given time. Learning how to live within a budget is one of the keys to creating a game which plays smoothly.

Coordinates
=======
3-D space is defined by the [X,Y and Z axes](#xyz). A location in 3-d space can be specified with 3 numbers (in the order XYZ).  So (0,0,0) represents to the center of a scene, (1,0,0) a point 1 unit to the left of the center, and so on. When [transforms](#transform) are [parented](#parent) to each other, the child transforms are oriented around the center of their parent: as far as a child is concerned (0,0,0) is the location of the parent object and not the center of the world.

Collider
======= 
By default, [gameObjects](#gameobject) in Unity are visible but not tangible: they don't affect each other and aren't affected by gravity or other forces. A collider is a [component](#component) which makes an object tangible to the physics system. Colliders are usually much simpler shapes than the objects they are attached to, which makes the physics calculations run faster.  

Component
======= 
Components are nuggets of code which define how your game will play. Components are attached to one or more [GameObjects](#gameobject); each component usually only affects the object to which it is attached.

Console
=======
The Console is a Unity panel which displays messages from Unity or from your game code. It tells you when errors occur but is also a useful way to print out information as you're experimenting with new ideas.
![Console](http://docs.unity3d.com/Documentation/Images/manual/Console-0.jpg). The most recent console messages is also displayed at the bottom of the main Unity window, even if the console is closed.

 Diffuse
=======
Diffuse lighting (as opposed to [specular](#specular) lighting) refers to the rendering of matte objects. Diffuse lighting depends entirely on the angle between the [surface normal](#normal) of an object and the light - it looks the same regardless of the viewer's position.  Many shaders use the terms 'diffuse map', 'color map' and 'surface color' interchangeably.

FBX
======= 
A common format for storing 3d model files.

GameObject
======= 
Any object - for example, a model, a light, or a camera -- is a GameObject. Other asset types which don't get physically placed into the game on their own (such as textures or animations) are _not_ considered gameObjects. Only GameObjects can have [Components](#component).

Game Window
=======
A 3d view showing the game from the perspective of the currently active game camera.

Global Transform** Refers to a [transform](#transform) in absolute space. For example, a plate on a 3 foot high table may have a _local_ transform height of zero if parented to the table -- but it's _global_ transform height will be 3 feet.  In Unity scripts we use **transform.position**, **transform.rotation** and **transform.scale** to access the global transform.

Hierarchy Window
======= Shows all of the objects in your current Unity scene, arranged in an outliner like indented view![hierarchy view](http://docs.unity3d.com/Documentation/Images/manual/Hierarchy-0.jpg)
 For more information see the [Unity docs](http://docs.unity3d.com/Documentation/Manual/Hierarchy.html)


Import
=======
To bring an [asset](#asset) into Unity. Files cam be imported through the import menu, or by file drag-and-drop in the [project folder](#projectfolder).  If you update a file already in the project folder, Unity will automatically re-import it. 

Inspector
=======
The Unity inspector window is used to examine or set the properties of [gameObjects](#gameobject) and [assets](#asset)![inspector](http://docs.unity3d.com/Documentation/Images/manual/Inspector-1.jpg)

Lightmap
=======
A lightmap is a [texture](#texture) which stores pre-computed [diffuse lighting](#diffuse) for a scene. This allows the computer to skip many repetitive lighting calculations (at the cost of more memory). Lightmaps are often used to create the illusion of shadows.

Local Transform** Refers to a [transform](#transform) that is defined relative to another. For example, a plate on a 3 foot high table may have local transform height of 0 if it is [parented](#parent) to table - even though it's absolute position is still three feet above the zero plane. In Unity scripts we use **transform.localPosition**, **transform.localRotation** and **transform.localScale** to access the global transform.  See also: [parent](#parent)

Matrix
======= 
A collection of 16 numbers in a 4 row by 4 column arrangement which represents the mathematical desicription of a [transform](#transform). For more info see this [video course](http://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/video-lectures/).

Mesh
=======
A mesh is a collection of [vertices](#vertex) or 3D point.  The computer draws the mesh as a collection of facets or [polygons](#polygon)

Normal
=======
The direction which a 3D [polygon](#polygon) faces is it's 'normal'. It's mathematically expressed as a 3D vector.  Normals are used to calculate light and shading, to figure out if objects are visible from behind, and to calculate the effects of physics collisions.

Parent
=======
[Transforms](#transform) can be linked so that one transform is relative to another, and moves when the other moves: for example, moving your shoulder causes your elbow to move, moving your elbow causes your wrist to move, and so on.  The transform which causes the other to move is known as the "parent", any transforms which are moved by a parent are "children".  A parent can have many children, but each child has only a single parent. We also refer to the act of linking transforms in this way as "parenting".  See also [local transform](#localtransform) and [global transform](#globaltransform).

Polygon
=======
3 or more vertices which form a planar facet than can be rendered in 3D.

Project Folder
==============
Every unity game defines a 'Project Folder' where all of the assets are stored. Anything inside the project folder is available to the game. Usually the project folder will be stored in your Documents folder. Since all [assets](#asset) live in the project folder, we usually refer to them by relative paths such as **Assets/levels/intro.unity** or **Assets/textures/bowling_pin.tif**


Project Window
=======
The project window shows all of the [assets](#asset) in your [project folder](#projectfolder)
![projectWindow](http://docs.unity3d.com/Documentation/Images/manual/ImportingAssets-0.jpg)

Prefab
=======
Stores a collection of [GameObjects](#gameobject), along with any components, materials, textures and settings. Prefabs are stored as ".prefab" files in the [project folder](#projectfolder). 

Scene
=======
Aka a "level."  The basic work unit in Unity; a collection of [gameObjects](#gameobject) and their associated [components](#component).  Scenes are saved in the [project folder](#projectfolder) as files with a ".Unity" extension.

Scene Window
=======
A 3d view showing your currently opened scene file.
![scene view](http://forum.unity3d.com/attachment.php?attachmentid=13583&stc=1&d=1285687229)

Script
=======
A small, modular piece of computer code which controls one aspect of Unity game. Most [components](#component) are created by scripts, and people will occasionally use the terms interchangeably. 

Skinning
======= 
Skinning is a way of allowing several different [transforms](#transform) (or '[bones](#bone)' to move the [vertices](#vertex) of a model. This allows for models which deform realistically rather than hard mechanical surfaces.

 Specular
======= Specular lighting refers to the lighting calculations for shiny or glossy materials such as plastic or metal. Unlike [diffuse lighting](#diffuse) the size and intensity of specular lighting changes dependent on the position of the viewer as well as the position of the lights and the [surface normals](#normal)

Texture
======= 
A 2-d bitmap image that is applied to a 3d model. 
![texture](http://www.vrarchitect.net/anu/cg/Texture/Image/slide12.jpg)

Transform
======= 
The collection of movement, rotation and scale which defines an object's position in space is known as its transform. Transforms can be either local or global.

Trigger
======= 
A [collider](#collider) with the _IsTrigger_ checkbox turned on acts a trigger rather than a physics volume. Scripts can detect when a [gameObject](#gameobject) enters a trigger -- for example, a character walking into a trigger could spring a trap, or a ball entering a score trigger could give the player points. 

Update Loop
=======
Several times a second, the game will tell all of the active [GameObjects](#gameobject) and [components](#component)to update themselves. This causes the scripts attach to each component to run their Update
======= code, which can make objects move or take actions.  

Vertex
=======
A vertex (pl. 'vertices') is one point of a 3d [mesh](#mesh). The visible surface of a model is drawn by the computer as a series of facets connecting vertices.

XYZ
======= 
The [coordinate system](#coords) for a 3-d space has three main directions, or 'axes'.  In Unity, the ground plane is defined by the X and Z axes, and the vertical dimension is Y. The [origin](#origin) is the 3-d point located at X=0, Y=0, Z=0.  Positions, rotations and scales are all defined for each axis, so an object might be located at (0, 10, 0) -- that is, ten units off the ground -- and rotated (45, 0, 0) -- that is, rotated 45 degrees clockwise around the X axis.
![axis](http://docs.unity3d.com/Documentation/Images/manual/class-Transform-4.jpg)
By convention controls that manipulate the scene are colored coded so that red = the X axis,  green = the Y axis and B = the Z axis. 
