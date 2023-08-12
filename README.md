# Particle-Editor
Tool for creating particles/effects in pygame (With Guide)

## Guide
### Creating Particles
![ezgif com-video-to-gif](https://github.com/FrogTesseract/Particle-Editor/assets/118939591/983016fd-7ea8-47b6-84b4-f11a3ec4a11f)


Radius (0 - 99): Changes the radius of the particles

X (X1 <= X2): Changes the distance in which the particles move on the x-axis every frame. A random number is generated between X1 and X2. 
Y (Y1 <= Y2): Changes the distance in which the particles move on the y-axis every frame. A random number is generated between Y1 and Y2. 

Shrink Rate ( >= 0): Changes the size in which the radius decreases every frame. 

Emission Rate ( >= 0): Time in ms between each particle is created.

### Exporting

Exporting will create a text file named "particle.txt" - In this file is the class for the particle, the particle event. This can be copied directly into your pygame project.

In the event loop you will need to call particle.add_particles() when the event PARTICLE_EVENT occurs:

In the game loop you will need to call particle.emit() (Similar to displaying images). - **Make sure to call after you are displaying other surfaces**

### Additional Support
An example of particle.txt can be found in the repo (example.txt) with the additional code to call the functions.




            













