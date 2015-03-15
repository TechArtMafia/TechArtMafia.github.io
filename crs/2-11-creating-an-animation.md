###Creating an animation

Animations are stored as Animation clips. Clips are assets on disk like textures or models. They are specific to individual assets, so you have to create animations with objects selected.

### Animating from the editor

* Select your dalek model and open the animation editor (**Windows >> Animation Editor**) 
* Create a new clip by clicking on the dropdown in the top-right corner of the left panel)
* Expand the dalek view in the outliner at left. Select the head, then expand the **transform**
* Select the Rotate Y channel and right click on it. Choose **Add Curve** to make it animatable
* Set the time by clicking in the time slider at the top right. Set the time forward a couple of seconds.
* Add a new key by right clicking in the gray bar under the time slider and choosing **Add Keyframe**.
* Change the value by grabbing the new key and move it up to about 45.
* Hit the play button at the top left, switch to the scene view and you'll see the head swivel.

----------
### Adding keys
* Notice the play button turns *red* when you're playing an animation. This means that anything you do will be included into the animation.
* Set the time slider after the key you have. 
* Switch to the scene view and select the head. Rotate it around the vertical axis in the view. 
* Check the graph view, the change should be a new key.

-------------
### Tangents

Tangents are an important tool for controlling the interpolation between keys

* Flat tangents slow down the rate of change
* Steep tangents indicate fast change
* Smooth curves mean organic motion
* Linear lines and cusps look mechanical.

Each key has its own tangents.

* In the animation window, delete the keys in between the first and last so you have only two.
* right click on the end tangent. Check the differences between **Left tangent >> Free**, **Left tangent >> Linear** and **Left tangent >> constant**.
  * Linear does a straight linear interpolation. It looks pretty mechanical
  * Constant snaps the values at the last minute
  * Free creates a handle you can edit



[back](2-10-animation-basics.md.md) [next](2-12-animation components.md.md)