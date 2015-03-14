### Specular illumination

Lighting of shiny surfaces is known as [specular illumination](glossary#specular)  

![specteapot](http://www.reindelsoftware.com/Documents/Mapping/images/latitude_specular_teapot.gif)

Specular lighting appears as 'highlights' or 'hot spots'.  Unlike diffuse lighting, the size and intensity of the highlight depends on the position of the viewer as well as the surface normal and the light. This causes the highlight to 'travel' across the surface of objects as cameras, objects or lights move. For this reason specular lighting cannot be [baked](glossary#bake).

There are several different ways of computing specular. The simplest ("Phong") has a single control for the size of the highlight. Other techiques such as "Blinn" shading allow control over the sharpness and contrast of the highlight as well.  Specular is more expensive to calculate than diffuse lighting, so many games use it sparingly.

![blinnphong](http://seblagarde.files.wordpress.com/2012/03/phong-blinn-compare.png)

 Specular is rendered _over_ conventional texture maps (mathematically, the pixel color of the specular is just added to the pixel color of the diffuse).  It's visually very effective to mask the specularity using a texture which turns down the shininess in some parts of the model; this breaks up the highlights as they travel across the surface and is a big help with realism.  As usual, of course, more realism = more memory and more CPU time.

![masked earth](http://www.physics.adelaide.edu.au/~pmcgee/tform/ventrio.jpg)

Most specular materials in real life show white highlights. The main exception is metals such as gold, copper or bronze which show tinted highlights.

[back](2-4-diffuse-lighting) [next](2-6-reflectivity)