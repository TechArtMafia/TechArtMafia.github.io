### 3D Lighting 

Lights are objects in the scene, with their own [transforms](glossary.md#transform). They can be attached to other objects (for example, headlights on a car).  The computer uses the position of the light and the [normals](glossary.md#normal) of the [meshes](glossary.md#mesh) in the scene to figure out how bright something is. 

In the real world, there are many subtleties in how objects appear to the eye, depending on the physics of the lighting, the atmosphere, and the materials involved. Computers can't handle all of that in real time. Instead, there are a bunch of standard techniques which work as 'building blocks' to create complex effects. Ideally you'll choose as few of these as you can to get the results you need, saving on both rendering power and memory cost of your game.  

#### Diffuse, Specular, Reflectivity and Ambience: the building blocks

The game uses shaders -- small, highly specialized sub programs -- to render your effects on screen. Every Unity [material](glossary.md#material) can have its own shader. Most shaders are just mix-and-match collections of the techniques we'll go over next.

![basics](http://www.beyond3d.com/images/articles/Geometry/lighting-specular-sphere.gif)
#### Side note: Dynamic range and HDR

All computer images can only range from black pixels to white ones. In real life, a 'white' piece of paper under indoor lighting will be from 400 to 1000 times dimmer than a 'white' cloud in an afternoon sky; on a computer screen they will be exactly the same pixel color.  

In the real world, Your eye automatically adjusts so that the darkest things you see are 'black' and the lightest 'white' - but you know instinctively that there is a difference (as you can tell when you walk from a dark room into full sunlight and you need a second or two to adjust).  In graphics 
 we call that 'High Dynamic Range' or HDR.  

In HDR rendering each pixel is stored with a value that tells it's brightness in absolute terms.  Working with HDR is a complex task because the computer has to do the same kind of adaptation to different brightness values that your eyes do. If you're curious (and plan on getting Unity Pro) you can [read about it here.](http://docs.unity3d.com/Documentation/Manual/HDR.html)

[back](2-2-how-3d-models-work.md) [next](2-4-diffuse-lighting.md)