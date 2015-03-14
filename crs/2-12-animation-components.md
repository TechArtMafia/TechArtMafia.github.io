### Animation components

* Animation clips are played by the _Animation_ component on game objects (the _Animator_ component is different!)
* To make a clip available to a character it has to be added to the component
* Clips have to be used by the objects they were created for. If not, they have no effect.
* Add clips in the usual way (drag-drop or the circle button)
   * **Tip** _you often have multiple animations with the same names for different characters - expand the picker window to see the full path_
* **You can't call an animation from script unless it is added to the component.**

### Animation clip properties
* In the inspector for a clip you can set it to loop, play only once, cycle back and forth, or play once and freeze.
* You can preview the clip by selecting it and dragging the right model into the preview window.
  * This is awkward for animations on a part of a hierarchy

### Animation layers
* An animation component can play multiple animations at once
* Animations have a 'layer'. Animations in the same layer can blend; animations in different layers are added in
* Under the hood this is just another way of calcuating the underlying numbers... so it results may not be what you expect
* good for:
    * adding partial motions, like turning the head on a walking character
    * blending different versions of one motion ('walk-look-left' to 'walk-look-right')
* Not good for
   * animations with mismatched length or features (no blending between walk and swim, or from stand to run)


[excersize](emergency-last-minute-excersize)