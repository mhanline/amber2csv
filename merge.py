#!/usr/bin/env python3

import pandas as pd
import sys
from datetime import datetime
import os

if __name__ == '__main__':
    nowTime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    for inFile in sys.argv[1:]:
        df = pd.read_csv(inFile)
        estTrueDf = df.loc[df["estimate"] == True, ["perKwh", "startTime"]]
        estFalseDf = df.loc[df["estimate"] == False, ["perKwh", "startTime"]]
        pd.merge(estTrueDf, estFalseDf, on='startTime', how='inner').to_csv(f"{nowTime}-merged-{os.path.split(inFile)[1]}") 