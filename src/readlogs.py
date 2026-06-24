import pandas as pd
o = pd.read_csv("data/users.csv")
print(o.info())
def logins():
    logins = o[o["action"] == "login"]
    print(logins)
    logins.to_csv("data/logins.csv", index=False)
def logouts():
    logouts = o[o["action"] == "logout"]
    print(logouts)
    logouts.to_csv("data/logouts.csv", index=False)
def downloads():
    downloads = o[o["action"] == "download"]
    print(downloads)
    downloads.to_csv("data/downloads.csv", index=False)
logins()
logouts()
downloads()
print(o["action"].value_counts())
