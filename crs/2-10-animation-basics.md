### Animation basics


From a purely *technical* perspective, computer animation is about controlling the change in numbers over time.  Unity does a pretty good job of letting you handle that aspect with a built in tool. That said, most of the animation in your game will be done in other software -- Unity is fine for animating individual objects or changing shaders, but it's not a character animation package on its own. 

On the other hand, the **artform** of animation is a very big, complex topic. We're not going to get into the art form this time out. If you want to study up on that, check out [Richard Williams' website](http://www.theanimatorssurvivalkit.com/index.html)  or buy a copy of [*The Illustion of Life*](http://www.barnesandnoble.com/w/illusion-of-life-frank-thomas/1102678914?ean=9780786860708) Another option (If you are able to model or buy characters but are intimidated by character animation) is  [Mixamo](http://www.mixamo.com/) a website which will add motion captured generic animations onto your characters.

Unity's animation interface is available under **Windows >> Animation** (note it's *Animation* and not **Animator**, which is a new system that is going to replace the 'legacy' system we're covering today.  You can also get to the animation UI with **command/ctrl + 6**

![example](http://media.moddb.com/images/articles/1/52/51573/auto/Learning20the20Interface-36.jpg)

The animation window has four main parts:

* A vcr-like control at top left
* A timeline at the top right
* A list of objects and animatable properties at the left
* A **Graph view** at the right

### Understanding the graph view display
The graph view is the most unusual. It shows the way values change over time. In the example above, the cube's rotation in Y starts around 0, climbs to just over 180 degrees at about 1 and a half seconds and levels off.

**Tip** _The times are in timecode:  0:30 is 30/60ths of a second; 1:00 is one second, 1:30 is 1.5 seconds, etc._
 
The dots on the colored line are 'keyframes' values that are set by hand, saying 'have this value at this time'.  The lines connecting the dots are 'in-betweens' or 'tweens' for short - mathematical interpolations between the keys.

The interpolation is controlled by setting *tangents* at the key frames. A tangent describes how fast or slowly to interpolate the values at that key (if you've used Adobe Illustrator or Photoshop curves, tangents are like curve handles).
  'Flat' tangents slow down the change of values near the keys; steeper tangents indicate a quick change in the numbers.  

To set the tangents for a key, you can right click on it in the animation window and choose a tangent type. If the tangents are editable they show up as handles like those in Photoshop.

[next](2-11-creating-an-animation.md.md)


 