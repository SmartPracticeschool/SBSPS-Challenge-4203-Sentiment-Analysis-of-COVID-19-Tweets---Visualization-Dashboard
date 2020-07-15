
class RunConfig:
    ckey="dmL868Kqi7GkZEWj4OzcVaMwQ"
    csecret="WoD3Zycw6vmYzi7ftEpu3P1IZ9Cn68wUYOAZ7801fzotezs1kP"
    atoken="2320627501-NcSRXBJobUwFxYQp88kgeilX3zJwd9HVDPvUalP"
    asecret="GFyFJpp0JyH9daXRdOuVVHnr9Xizb4punVyfGo4JwAScv"
    dbNameInit = 'twitter.db'
    tableName = 'Tweets'
    positiveNegativeThreshold = 0.001
    #keyWords= ["Corona Virus", "Covid19", "novalcorona", "lockdown"]
    keyWords= ["Covid19", "lockdown", "corona"]
    dbName = dbNameInit.split('.')[0]+"_".join(keyWords)+".db"
