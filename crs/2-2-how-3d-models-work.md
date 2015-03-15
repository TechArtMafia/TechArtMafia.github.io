## How 3d Models work

Models are collections of [3D coordinates](glossary.md#coordinate) known as "[vertices](glossary.md#vertex)".  The vertices are grouped together into [triangles](glossary.md#triangle) (confusingly, they are sometimes known interchangeably as 'polygons' - strictly, a polygon is alway going to be made of triangles)

![triangles](http://www.webreference.com/3d/lesson52/52-16.gif)

Triangles are useful because they are always planar. The math for figuring out of a triangle is facing one way or the other or whether something lies on the plane of the triangle is very simple. The number of vertices in the model is directly related to how much work the computer will have to do to render it: a 1000 vertex model is about 10 times slower to render than a 100 vertex model.  For this reason many game models are described in terms of their 'poly count' or 'triangle count'. A model under 1,000 triangles is fairly inexpensive to render; between 1000 and 5000 is moderate cost, 5,000 to 10,000 is fairly expensive, and more than 10,000 should be rare.  On less powerful hardware (such as phones or tablets) Unity slows down when the number of triangles on screen passes about 150,000.  More powerful PCs can do much better - but unless you're working on very high end hardware total counts should be well under 500,000 triangles at a time.

**Tip** _You can use the 'Optimize Mesh' setting in the inspector to attempt to simplify models. This will reduce the poly count for incoming models, but often at the expense of quality. If you can't work on the models by hand, this may be a handy way to bring them under control_

The direction that a triangle faces is known as its [normal](glossary.md#normal). Normals are used to calculate shading: if the normal of a triangle points towards a light source, that triangle will be lit; if it's perpendicular or pointing away, the triangle is not lit.  Triangles are not naturally two sided - they are invisible from the 'back' unless you choose a shader that deliberately renders the back sides of triangles as well as their front faces.

![lighting normals](http://docs.unity3d.com/Documentation/Images/manual/AnatomyofaMesh-0.jpg)

To create the appearance of smooth surfaces, we tell the computer to average out the normals of adjacent triangles. This makes the surface light as if it were smooth, even though it is still faceted:

![smooth normals](http://download.autodesk.com/global/docs/maya2014/en_us/images/comp_vertexNormals3.png)

Just like other 3d coordinates, vertices can be moved, rotated or scaled by transforms in the scene. 

Some models are [skinned](glossary.md#skinned). In a skinned model, the vertices of the model can be moved by more than one transform (for example, a vertex in a character's elbow might move partially with the bicep transform and partially with the forearm transform) creating a soft deformation that looks like skin flexing.

**TIP** _Skinning is used all the time in games, but it comes with a cost.  Don't use skinning unless you need to deform the models - if you're not planning on smooth skinned behavior, make sure your models are not skinned! You can spot skinned models in Unity because they will have a **SkinnedMeshRenderer** component rather than the more common **MeshRenderer** in their inspectors._

![skinning](http://upload.wikimedia.org/wikipedia/commons/6/66/Ie_paint_tube.jpg)

* For obvious reasons, the transforms of a skinned character are usually known as '[bones](glossary.md#bones)'.
![skeleton](http://morpheo.inrialpes.fr/people/hetroy/data/uploads/rech-anim-old.png)
[back](2-1-basics-of-3d-rendering.md) [next](2-3-3d-lighting.md)