### Lights

Unity lights are not physically simulated - the first thing you'll notice is that by default they don't cast shadows. On closer inspection you'll also see that they don't bounce: a bright light shining on a wall should diffuse some light over the area indirectly, but a Unity light does not.

There are 4 main light types (this is a summary, the real details are [in the Unity Manual](#http://docs.unity3d.com/Documentation/Components/class-Light.html), in order of render cost:

* Directional lights : these light along a direction, but don't have a physical location. Even objects 'behind' the 3d icon of the light will be lit by it.  Directional lights are somewhat cheaper to render than other lights.
* Point lights: These shed light in all directions, like a light bulb.
* Spot lights: These are cones with an adjustable falloff, handy for accent lighting. Spotlights can also be used to project slides-type images or fake shadows.  The calculations for spots are a little more involved, so they cost more than point lights.
* Area lights: **Area lights don't work at run time** They are, however, useful for [pre-baking lightmaps](glossary#bake) if you want nice soft falloffs in your lightmaps.

### Lighting budget

All lights are really just being called by the [shaders](glossary#shader) on your objects.  Each additional light in your scene requires extra calculation from every object in the scene ("Am I in range of the light? If so, what's the angle between it an my surface normal?" etc).  For this reason lights can be a significant cost factor in your rendering budget. Small lights with limited ranges are cheaper than large one; fewer lights are cheaper than more.   

Most Unity shaders can be lit in two ways. "Pixel" lighting is more details and realistic; "Vertex" lighting is cheaper to render, but cruder.  Typically Unity automatically runs pixel lighting on "important" lights and vertex lighting on the rest to save rendering power. Importance is a bit hard to calculate, but basically its based on the **Render Mode** setting in the light itself.  Directional lights win a "tie" with other kinds of lights, and closer lights are more "important" than farther ones.  Many Unity games have an low-level flickery look caused by too many lights jostling for 'importance' at render time. 

[back](2-8-shaders-materials)

[EXCERSIZE](http://www.tryscribble.com/wikis/intro-to-unity3d/pages/rendering-excersize-exterminate)
