### Week 1: Introducing Unity ###

This week is devoted to familiarizing everyone with the basics of the Unity 3d Interface.  We'll start with a high level overview of how Unity does it's work using components, assets, and scripts.  We'll learn how to use the Unity editor itself, in particular:

<hr>
Intro to Unity
===============
* Why Unity?
   * Games are programs - but a very special kinds of program
       * Lots of 'content' : models, images, sounds, and so on
       * Lots of small, almost autonomous bits of code
          * How does a character move?
          * How do we keep score?
          * What happens when I press the mouse button?
   * Building games is **hard**! 
       * That's why they're always (a) late and (b) expensive!
       * Lots of complexity = lots of ways to break things
       * Handling many different kinds of data takes lots of work
   * Unity tries to make this easier
       * Big architectural issues are handled for you
       * You work on bite-sized pieces
       * Content and pipeline are already done
       * Packaging for different hardware is "automatic".. to a point

<hr>
Unity Building Blocks
=============================
   * All Unity games are made up of a fairly small set of pieces:
     * [GameObjects](glossary#gameobject)
       * These are physical objects with a position in the 3d world
       * Can be placed by hand or created ("instantiated") in the game
       * GameObjects can contain other GameObjects in a [parent-child](glossary#parent) relationship
       * GameObjects can have attached [components](glossary#component) which control their behavior or appearance.
     * [Components](glossary#component) are small pieces of program code attached to GameObjects
       * One GameObject can have any number of components
       * Every "turn" (usually 1/60th of a second) all components are updated by the game.
       * Components can communicate using messages or call other bits of code
       * Unity provides many built in components:
        * _MeshRenderer_ displays 3d models
        * _Animation_ plays animations
        * _Collider_ is uses by the physics system to know the shape and mass of an object
  
     * [Prefabs](glossary#prefab) are assemblies of gameObjects and components
       * Lets your store and replicate a complex setup
       * Changing a prefab once updates **all** copies of that prefab!
       * You can override prefab by making changes to one copy
         * **Tip:** Prefabs are ordinarily displayed in **blue text**. Prefabs that have been altered (or 'broken' in Unity slang) are **pink**.
       * Models and animations created in outside programs can be brought in to Unity as prefabs
     * [Scenes](glossary#scene) are files containing a 3d setup of multiple prefabs and gameObjects
       * In most games this is known as a 'map' or 'level'
       * Scenes can be loaded while the game is running (ie, "load the beach level") 
       * Scenes **can't** be unloaded as a unit! It's up to you to delete scene contents when you're done with them!

* Every Unity game is just one or more scenes, containing prefabs and components
* This loose kind of organization is tough for big projects - but ideal for small games.


<hr>
UI basics
============

* The basic Unity UI
   * **Scene window**: where you construct your game world 
      * Scene window has special tools to show you only what you're intested in
      * Scene window camera is lets you see from any angle, not just the game's camera
      * Includes grid for lining up <br>
![sceneWindow](http://uploads.gamedev.net/packtpub/0546OT_01_10.png)
   * **Game window**: where you see the world through the player's eyes 
<br>![game](http://docs.unity3d.com/Documentation/Images/manual/GameView40-3.jpg)
   * **Hierarchy window**: Lists the contents of your world
      * The nesting reflects [parent-child](glossary#parent) relationships among your pieces.
<br>![hierarchy](http://www.umingo.de/mydata/paper/mechs_and_tanks/images/ch3/map_hierarchy.png)
   * **Project window**: Lists all the resources in your project; your 'toolbox'.<br>
![projectWindow](http://docs.unity3d.com/Documentation/Images/manual/ImportingAssets-0.jpg)
   * **Console**: How Unity provides feedback 
<br>![Console](http://docs.unity3d.com/Documentation/Images/manual/Console-0.jpg).
   * **Play button** Run the game in test mode<br>
   ![playbutton](http://www.geoplanit.co.uk/wp-content/uploads/2012/03/unity_play_buttons.jpg)
* Useful tricks
    * Many windows have search boxes in the upper right corner to help you find things in a crowded list
    * Windows can be moved and resized to match your work style
    * Windows can be docked as tabs
    * **Space bar** will set the active window to full screen, or reset it back to the default layout if it is already full screen
   * Use **Window > Layouts** to pick stored layouts or revert to the default view.

<hr>
Getting content into the game
=============================
* Unity projects
   * Projects are Unity's main organizational unit. A project is a set of folders on disk that contain everything needed to make up the game
   * Unity projects are created from the file menu (**File > New Project**)
   * The core of each project is the **Assets Folder**.  This is where all of your art and code will live 

* What are "assets"?
   * Assets are all the files that make up your unity project. They live in your [project folder](glossary#projectfolder).
   * Models & Animations (Maya, max, or any FBX file)
   * Textures (Photoshop, PNG, TIFF, TGA)
   * Shaders: the mini-programs that render 3d objects
   * Materials : combine a shader and texture(s) for a unique look
   * Unity ".asset" files - the catchall category for your own game data
   * Unity ".unity" scene files - game levels
   * Scripts: C# (.cs), Javascript (.js) and Boo (.boo) script files.
   * Unity ".prefab" files - combine all of the above into a complete game object with custom look, behaviors, and attributes

* Adding content to a project
   * Drop files into the project window from explorer/finder
   * Import file using **Assets > Import New Asset...***
   * Place files manually into the Assets folder
      * Right-click and choose 'refresh' if new files don't show up
      * Right-click and choose 'reimport' to force an asset to update
   * Via Unity Packages
   * From the Asset Store

* Import settings
   * Unity does a lot of work to make things usable in game. Most of this is hidden from users
   * Sometimes you need to tell Unity exactly what do to with an asset, however
   * Use the **Inspector** (**Window > Inspector** or Ctrl-3) to investigate settings.
       * **Common Model settings**
           * Scale factor: adjust for different size models from different sources
           * **TIP** Try to stick to 1 unit per meter for consistency
           * **TIP** Always model in **CM** in Maya. Unity forces the scale up by 100 for maya files!
           * Materials:
               * Import materials: controls the naming of materials and where Unity will look for materials matching those names.
       * **Common texture settings**
           * Be sure to choose the right texture type (normal map, GUI and texture are  the common ones)
           * Compression settings - keep an eye on budgets
           * **TIP** Texture memory is one of the biggest memory budget problems for games. Real games need to carefully control how much memory they use, especially on limited platfroms like iPhones.

<hr>
3d Basics
==========

* Placing objects in a Unity scene
   * Drag from the Project window to the Hierarchy Window
   * Drag from Project window to Scene window (can be confusing!)
   * Via Scripts and wizards
* Working with the Unity camera.
   * Use 'F' key to frame
   * Mouse wheel to dolly in and out
   * Orthographic vs Perspective 
   * Right click to choose preset cameras
   * **Alt+LMB** to orbit
   * **Alt+MMB** to pan
* Working with 3d objects
   * Pan tool (**Q** key)  ( same as **Alt+MMB**)
   * Move Tool (**W** key)
   * Rotate Tool (**E** key)
   * Scale Tool (**R** key)
* About 3d transformations
   * Transforms can be nested - moving one moves another
   * The 'parent' moves the 'child' -- but **not vice-versa**.
   * Children move and rotate **relative to the parent**
      * ex: Shoulder moves elbow; elbow moves wrist; wrist moves fingers...
      * ex: Moon rotates around earth; earth rotates around sun....
      * It's very useful to do your movement in the right space!
   * Parent objects by dragging the child onto the parent in Hierarchy view
   * Global and local mode buttons 
   * Pivot and center buttons

<hr>

Exercise:
============
We'll wrap up the class by importing some pre-made assets and assembling a (very) simple working bowling. Details [here](excersize-1-bowling-game)