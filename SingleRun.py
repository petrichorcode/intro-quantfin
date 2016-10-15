from tradgame import *
import os
import pandas as pd

gameParameters = {"seed" : 932748239, "quotewidth" : 0.3, "delay" : 0.001, "steps" : 200}
import sys
from models import *

if __name__=='__main__':

    # compatibility python2/3
    try:
        input = raw_input
    except NameError:
        pass


    if len(sys.argv) == 1:
        print("Usage %s <model1> [<model2> ...]"%sys.argv[0])
        sys.exit(-1)
    models = []
    for model in sys.argv[1:]:
        bn =os.path.basename(model)
        if not bn.endswith(".py"):
            print("Error %s is not a python file"%bb)
            sys.exit(-1)
        module = sys.modules["models.%s"%bn[:-3]]
        models.append(getattr(module, "pricer"))

    game = TradingGame(gameParameters)
    game.run(models)
    print(game.ranking())
    fout = open("events", "w")
    fout.write("%s"%game.getEvents())
    fout.close()
    pp = EventPlot(game)
    pp.plot()
    input("Any key to close plot")
    pp.close()
    sys.exit(0)
