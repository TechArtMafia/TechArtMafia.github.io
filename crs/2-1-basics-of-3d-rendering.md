##How computers create 3d images

_You won't really need to do the 3d math yourself - the Unity engine does most of this for you. However it's a good idea to have a grasp of the basics before playing with the UI so you know what you understand the possibilities and limitations_

### Transforms & perspective
A [transform](glossary.md#transform) moves, rotates or scales a set of points in 3D space. It's high school trigonometry - just done really, really fast (and by a computer).  It gets the name because it 'transforms' one set of [3D coordinates](glossary.md#coordinate) (an XYZ position) into another.

Transforms are represented mathematically by a [matrix](glossary.md#matrix) of numbers. You don't usually need to know how this works - multiplying matrices in order is the mathematical version of moving, rotating and scaling things.

Transforms can be nested into [parent-child](glossary.md#parent) relationship. Movements or rotation in the parent affect the children; children move and rotate _relative_ to their parents. 

[Perspective][persp] is just another kind of transform.  It transforms points from 3D space to the 2D space of the screen:

![durer perspective machine](http://mhsartgallerymac.wikispaces.com/file/view/dg-pic2-vkr15p.jpg/346574366/dg-pic2-vkr15p.jpg)
![perspective transform](http://upload.wikimedia.org/wikipedia/commons/9/90/Perspective_Projection_Principle.jpg)

* In the world, X and Z are the ground plane, Y is the vertical dimension
* On the screen, X is horizontal, Y is vertical. (Z is still present in  the math but not used)

[next](2-2-how-3d-models-work.md.md)

[persp]:http://en.wikipedia.org/w/index.php?title=Perspective_(graphical)&oldid=585108474