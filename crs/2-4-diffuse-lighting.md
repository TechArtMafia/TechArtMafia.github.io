
### Diffuse illumination

Lighting of matte surfaces is known as [diffuse illumination](glossary.md#diffuse):

![diffuse](http://www.reindelsoftware.com/Documents/Mapping/images/diffuse_teapot2.gif)

Diffuse illumination is calculated by comparing the [normal](#normal.md) of the surface and the position of the light  (usually, the cosine of the angle between them tells you how bright the light is). Because it only uses the surface and light positions, diffuse illumination does not depend on the viewpoint of the camera.  For this reason,  diffuse illumination is sometimes precalculated or '[baked](glossary.md#baking)' to save rendering time; in Unity the precalculated lights are stored into [textures](glossary.md#texture) known as [lightmaps](glossary.md#lightmap)

The color of a 3d model is also affected by [textures](glossary.md#texture).  The color of the texture pixels is multiplied by the color of the lit surface to produce a shaded image:

![textured](https://tpfto.files.wordpress.com/2012/03/teapots.png)

[back](2-3-3d-lighting.md) [next](2-5-specular-lighting.md)