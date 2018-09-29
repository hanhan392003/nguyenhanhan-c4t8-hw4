import pyglet

music = pyglet.resource.media('sample.wav', streaming = False)
music.play()

pyglet.app.run()