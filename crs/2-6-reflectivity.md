### Reflectivity

Unity does not support 'real' reflections: You can't make a mirror or an ocean that actually calculates the correct reflections for other objects in the scene. Very few games, even on high end platforms, can afford the math needed to calculate reflections in real time. 

The usual substitute is known as an [environment map](glossary.md#environmentmap) or a [cube map](glossary.md#cubemap) This is a set of textures arranged as if they were mapped onto a cube:

![cubemap](http://judegodin.files.wordpress.com/2011/12/cube_map2.png)

At render time the computer calculates the reflection using the angle between the viewer and the surface normal to figure out how to color the surface. 

![refmap](http://www.reindelsoftware.com/Documents/Mapping/images/lat_spec_teapot.gif)

Like specular highlights, reflections are added on top of diffuse illumination. They can also be masked using a texture.  In some cases a very contrasty environment with a strong light source visible can be a good substitute for expensive specular calculations.

[back](2-5-specular-lighthing.md) [next](2-7-ambient-unlit.md)