### Unity materials and shaders

Now that you've got a grasp of some of the building blocks of 3d graphics, we'll take a look at Unity shaders and materials.

### Shaders

Shaders are tiny, specialized programs that only know how to render geometry and lights to the screen. Advanced users can write their own shaders for special effects (maybe we'll cover that in another class) but most users just pick shaders from the list included with the Unity standard assets or bought from the Asset Store.  You pick the shaders from the 'shader' dropdown in your materials; they are grouped into several categories, such as 'Reflective' or 'Transparent' ([details here](http://docs.unity3d.com/Documentation/Components/Built-inShaderGuide.html)).  Here are some of the available shaders, all using the same texture.

![examples](http://docs.unity3d.com/Documentation/Images/manual/Materials-1.jpg)


Every shader has a set of 'parameters' or properties you can edit. These come in a couple of flavors. Here's a shader inspector showing some common parameter types:

![insp](http://biphenyl.org/blog/wp-content/uploads/2012/04/Screen-Shot-2012-04-24-at-03.50.32.png)

The examples show:

* **Numeric values**, such as "shininess" or "Night Light Strength". Sometimes these are set with sliders (when the values are kind of impressionistic) and sometimes they are set with numbers directly when more control is needed.
* **Color values**.  These appear as color swatches in the editor, such as "Night Light Color" and "Specular Color" 
* **Textures**. These are image files in your Assets folder. They can be drag-dropped from Assets into a material, or you can choose the **Select** button to open a picker which lists available textures.  The 'tiling' option next to a texture allows you to specify repeats, so you could for example change the size of the tiles on a floor texture.  The "Offset" value allows you to move the 2D position of the image.

### A note on colors

![picker](http://www.rbcafe.com/Softwares/Unity/Documentation/Images/manual/Editing%20Value%20Properties-2.jpg)

For annoying historical reasons, Unity colors are represented by numbers between 0 and 255, where 0 is 'no color' and 255 is 'pure color'. "Alpha" values control things like transparency and intensity, typically Alpha 0 being transparent and Alpha 255 being opaque.

Unity colors are not exactly like traditional colors. Red and Green for example add to Yellow; Green and Blue to Cyan, and so on:

![rgb](http://upload.wikimedia.org/wikipedia/commons/2/28/RGB_illumination.jpg)

In this image the blue light color would be RGB (0, 255, 0).  The cyan overlap between the blue and green spots would be (0,255,255). In the center where all the lights overlap the color approaches (255,255,255) or white.

### Shaders vs Materials

A **Material** combines a choice of shader, textures, and parameter settings. Many materials may use the same shaders -- or (as in the example above) the same texture and different shaders. The material is the link between a particular shader, some settings, and one or more objects in your game.  Every material in the game imposes some extra costs when rendering: all things being equal, 10 objects with the same material will cost less to render than 10 objects which each had unique materials. In small scenes the difference is negligible; in larger scenes or on slower hardware the costs add up.  Often you can save memory (and extra material costs) by combining multiple different images into a single texture and material.


