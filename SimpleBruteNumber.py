import time

mdp = 65648667
mdpo = 0
temps = time.time()
print ( "Start" )

while mdp != mdpo:
    mdpo += 1

temps = time.time() - temps
parsec = mdpo/temps
print ( "Stop" )
print ( mdpo )
print ( temps )
print ( int(parsec), " op par secondes" )
