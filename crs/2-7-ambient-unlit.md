### Ambient lighting

The last major aspect of lighting (and artistically, the one that gets overlooked the most) is ambient lighting.  Unlike the other forms of illumination, ambient light is 'directionless'.  Graphically, it's a 'fill color' - it just gets added to the rendered image directly. Scenes with no ambient light seem very harsh and contrasty; scenes with too much ambient light look washed out and flat.  This image shows different levels of ambient light in the vertical direction and different amounts of diffuse light in the horizontal direction:

![ambient](http://csis.pace.edu/~marchese/CG/Lect15/cg_l15_files/image011.jpg)

In Unity ambient light is not controlled by a placed light. It's in the render settings dialog **Edit >> Render Settings**:

![render settings](http://cdn.tutsplus.com/active/uploads/legacy/tuts/270_IntroToUnityPart1/images/unity-render-settings.gif)

### Self illumination (aka 'Emissive' lighting)

Many shaders also all you to set an object to be 'self illuminated' or 'emissive'.  In both case this simply means you can locally add in a color that you want and you'll get that color added in, much like ambient light.  Unlike ambient light, however, self-illumination is limited to objects with the right shader rather than covering everything. 

Self illumination can be controlled by textures or be applied to whole models. It's very commonly used for things like effects and user interfaces (glowing arrows, hit boxes and so on) 

[back](2-6-reflectivity) [next](2-8-shaders-materials)

Lighting links:


http://gamasutra.com/view/news/192391/Lighting_design_fundamentals_How_and_where_to_use_colored_light.php
http://www.gamasutra.com/view/news/196583/www.daionet.gr.jp/~masa/rthdribl
http://bensimonds.com/2010/06/03/lighting-tips-from-the-masters/