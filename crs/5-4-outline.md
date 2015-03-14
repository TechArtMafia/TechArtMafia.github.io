* Game shell
  * States
  * = level
  * Level limitations
    * No persistence
    * Passing game state
    * Make levels 'self starting'
  * Global objects
    * Don't overuse!
    * Singleton pattern
    * C# statics
  * How to store game data?
    * Levels for visible setup
    * Prefabs for working objects with many components
    * ScriptableObject for non-physical data
    * 'Resources' for things to load from disk
  * Switching levels
     * Level.load()
     * registering build
     * DontDestroyOnLoad for immortality.
  * Creating things on the fly
    * Instantiate()
    * Resources.load
      * Don't fall back on that too early!
  
  * Memory management and pools
    * about GC
    * Building a pool
    * Recycling
    * SetActive() to enable/disable
    * Finding available pool
  * Suicidal objects
    * Don't use Destroy if you don't have to! 
    * Using coroutines to time out


