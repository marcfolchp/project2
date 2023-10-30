import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import warnings

table = pd.read_csv("tables/top5leagues.csv")

class visualisation():

    def goalspermatch(self):
        goals = table.groupby("league")["score"].mean().mul(2).reset_index()
        goals = goals.sort_values('score', ascending=False)
        sns.barplot(x="league", y="score", data=goals, palette="autumn", zorder=1)

        plt.xlabel("Leagues")
        plt.ylabel("Goals")
        plt.title("Average Goals per Match")
        plt.show();

    def highteamgoals(self):
        goals = table.groupby("team")["score"].mean().reset_index()
        color = ['#D10214', '#38003c', '#FF4B44', '#CEFB03', '#008fd7']

        goals = goals.sort_values('score', ascending=False).head(5)
        sns.barplot(x="score", y="team", data=goals, palette="summer", orient="h", zorder=3)

        plt.xlabel("Goals")
        plt.ylabel("Team")
        plt.title("Highest Average Goals per Match")
        plt.show();
    
    def lowteamgoals(self):
        goals = table.groupby("team")["score"].mean().reset_index()
        color = ['#D10214', '#38003c', '#FF4B44', '#CEFB03', '#008fd7']

        goals = goals.sort_values('score', ascending=True).head(5)
        sns.barplot(x="score", y="team", data=goals, palette="summer", orient="h")

        plt.xlabel("Goals")
        plt.ylabel("Team")
        plt.title("Lowest Average Goals per Match")
        plt.show();

    def shotsgoals(self):
        data = table.sample(50)
        a = sns.scatterplot(x='totalshots', y='score', hue='league', data=data)
        a.legend(loc='center left', bbox_to_anchor=(1, 0.7), ncol=1)
        plt.xlabel("Shots")
        plt.ylabel("Goals")
        plt.title("Shots/Goals Relation")
        plt.show();
    
    def passing(self):
        goals = table.groupby("team")["passing"].mean().reset_index()
        color = ['#D10214', '#38003c', '#FF4B44', '#CEFB03', '#008fd7']

        goals = goals.sort_values('passing', ascending=False).head(5)
        sns.barplot(x="passing", y="team", data=goals, palette="summer", orient="h")

        plt.xlabel("Passes")
        plt.ylabel("Team")
        plt.title("Average Passes per Match")
        plt.show();

    def ontarget(self):
        goals = table.groupby("team")["ontarget"].mean().reset_index()
        color = ['#D10214', '#38003c', '#FF4B44', '#CEFB03', '#008fd7']

        goals = goals.sort_values('ontarget', ascending=False).head(5)
        sns.barplot(x="ontarget", y="team", data=goals, palette="summer", orient="h")

        plt.xlabel("Shots on Target")
        plt.ylabel("Team")
        plt.title("Average Shots on Target per Match")
        plt.show();

    def fouls(self):
        goals = table.groupby("league")["foulscommited"].mean().mul(2).reset_index()
        color = ['#D10214', '#38003c', '#FF4B44', '#CEFB03', '#008fd7']

        goals = goals.sort_values('foulscommited', ascending=False)
        sns.barplot(x="league", y="foulscommited", data=goals, palette="autumn")

        plt.xlabel("Leagues")
        plt.ylabel("Fouls")
        plt.title("Average Fouls per Match")
        plt.show();
    
    def distribution(self):
        pie = table
        pie = pie.groupby('league', as_index=False).agg({'ontarget': "mean", 'offtarget': 'mean', "blocked":"mean"})
        leagues = ["La Liga", "Premier League", "Bundesliga", "Serie A", "Ligue 1"]

        colors = sns.color_palette('YlOrBr')[0:5]

        for i in pie["league"]:
            x = pie[pie["league"]==i]
            x = x.set_index(['league'])
            x = x.T
            plot = x.plot.pie(y=i, figsize=(5, 5), autopct='%1.1f%%', colors=colors, labels=None)
            plt.title("Shots distribution")
            plt.show();

    def marketvalue(self):
        table = {"league":["La Liga", "Premier League", "Bundesliga", "Serie A", "Ligue 1"], "average":[9.78, 19.93, 8.31, 8.34, 7.59]}
        df = pd.DataFrame(table)

        df = df.sort_values('average', ascending=False)
        sns.barplot(x="league", y="average", data=df, palette="autumn")

        plt.xlabel("League")
        plt.ylabel("Average")
        plt.title("Average Player Market Value")
        plt.show();
    
    def simulation(self):
        
        self.la = 0
        self.pr = 0
        self.b = 0
        self.li = 0
        self.s = 0
        
        laliga = table[table["league"]=="La Liga"][["team", "score"]]
        laliga = laliga.groupby("team")["score"].mean().round().reset_index()

        premierleague = table[table["league"]=="Premier League"][["team", "score"]]
        premierleague = premierleague.groupby("team")["score"].mean().round().reset_index()

        bundesliga = table[table["league"]=="Bundesliga"][["team", "score"]]
        bundesliga = bundesliga.groupby("team")["score"].mean().round().reset_index()

        seriea = table[table["league"]=="Serie A"][["team", "score"]]
        seriea = seriea.groupby("team")["score"].mean().round().reset_index()

        ligue1 = table[table["league"]=="Ligue 1"][["team", "score"]]
        ligue1 = ligue1.groupby("team")["score"].mean().round().reset_index()

        for i in range(10):
            
            print(f"MATCHDAY {i+1}\n")
            
            laligateam = (laliga.at[random.randint(0, len(laliga) - 1), "team"])
            laligascore = laliga[laliga["team"] == laligateam]["score"].values[0]
            premierleagueteam = (premierleague.at[random.randint(0, len(premierleague) - 1), "team"])
            premierleaguescore = premierleague[premierleague["team"] == premierleagueteam]["score"].values[0]
            
            if laligascore >  premierleaguescore:
                self.la += 3
            elif laligascore <  premierleaguescore:
                self.pr += 3
            else:
                self.pr += 1
                self.la += 1
            print(laligateam, laligascore, " - ",  premierleaguescore, premierleagueteam)

            laligateam = (laliga.at[random.randint(0, len(laliga) - 1), "team"])
            laligascore = laliga[laliga["team"] == laligateam]["score"].values[0]
            bundesligateam = (bundesliga.at[random.randint(0, len(bundesliga) - 1), "team"])
            bundesligascore = bundesliga[bundesliga["team"] == bundesligateam]["score"].values[0]

            if laligascore > bundesligascore:
                self.la += 3
            elif laligascore <bundesligascore:
                self.b += 3
            else:
                self.b += 1
                self.la += 1
            print(laligateam, laligascore, " - ", bundesligascore, bundesligateam)

            laligateam = (laliga.at[random.randint(0, len(laliga) - 1), "team"])
            laligascore = laliga[laliga["team"] == laligateam]["score"].values[0]
            serieateam = (seriea.at[random.randint(0, len(seriea) - 1), "team"])
            serieascore = seriea[seriea["team"] == serieateam]["score"].values[0]

            if laligascore > serieascore:
                self.la += 3
            elif laligascore < serieascore:
                self.s += 3
            else:
                self.s += 1
                self.la += 1
            print(laligateam, laligascore, " - ", serieascore, serieateam)
                
            laligateam = (laliga.at[random.randint(0, len(laliga) - 1), "team"])
            laligascore = laliga[laliga["team"] == laligateam]["score"].values[0]
            ligue1team = (ligue1.at[random.randint(0, len(ligue1) - 1), "team"])
            ligue1score = ligue1[ligue1["team"] == ligue1team]["score"].values[0]

            if laligascore > ligue1score:
                self.la += 3
            elif laligascore < ligue1score:
                self.li += 3
            else:
                self.li += 1
                self.la += 1
            print(laligateam, laligascore, " - ", ligue1score, ligue1team)    

            premierleagueteam = (premierleague.at[random.randint(0, len(premierleague) - 1), "team"])
            premierleaguescore = premierleague[premierleague["team"] == premierleagueteam]["score"].values[0]
            serieateam = (seriea.at[random.randint(0, len(seriea) - 1), "team"])
            serieascore = seriea[seriea["team"] == serieateam]["score"].values[0]

            if  premierleaguescore > serieascore:
                self.pr += 3
            elif  premierleaguescore < serieascore:
                self.s += 3
            else:
                self.pr += 1
                self.s += 1
            print(premierleagueteam,  premierleaguescore, " - ", serieascore, serieateam)

            premierleagueteam = (premierleague.at[random.randint(0, len(premierleague) - 1), "team"])
            premierleaguescore = premierleague[premierleague["team"] == premierleagueteam]["score"].values[0]
            bundesligateam = (bundesliga.at[random.randint(0, len(bundesliga) - 1), "team"])
            bundesligascore = bundesliga[bundesliga["team"] == bundesligateam]["score"].values[0]

            if  premierleaguescore > bundesligascore:
                self.pr += 3
            elif  premierleaguescore < bundesligascore:
                self.b += 3
            else:
                self.pr += 1
                self.b += 1
            print(premierleagueteam,  premierleaguescore, " - ", bundesligascore, bundesligateam)
                
            premierleagueteam = (premierleague.at[random.randint(0, len(premierleague) - 1), "team"])
            premierleaguescore = premierleague[premierleague["team"] == premierleagueteam]["score"].values[0]
            ligue1team = (ligue1.at[random.randint(0, len(ligue1) - 1), "team"])
            ligue1score = ligue1[ligue1["team"] == ligue1team]["score"].values[0]

            if  premierleaguescore > ligue1score:
                self.pr += 3
            elif  premierleaguescore < ligue1score:
                self.li += 3
            else:
                self.pr += 1
                self.li += 1
            print(premierleagueteam,  premierleaguescore, " - ", ligue1score, ligue1team)
                
            bundesligateam = (bundesliga.at[random.randint(0, len(bundesliga) - 1), "team"])
            bundesligascore = bundesliga[bundesliga["team"] == bundesligateam]["score"].values[0]
            serieateam = (seriea.at[random.randint(0, len(seriea) - 1), "team"])
            serieascore = seriea[seriea["team"] == serieateam]["score"].values[0]

            if bundesligascore > serieascore:
                self.b += 3
            elif bundesligascore < serieascore:
                self.s += 3
            else:
                self.b += 1
                self.s += 1
            print(bundesligateam, bundesligascore, " - ", serieascore, serieateam)

            bundesligateam = (bundesliga.at[random.randint(0, len(bundesliga) - 1), "team"])
            bundesligascore = bundesliga[bundesliga["team"] == bundesligateam]["score"].values[0]
            ligue1team = (ligue1.at[random.randint(0, len(ligue1) - 1), "team"])
            ligue1score = ligue1[ligue1["team"] == ligue1team]["score"].values[0]

            if bundesligascore > ligue1score:
                self.b += 3
            elif bundesligascore < ligue1score:
                self.li += 3
            else:
                self.b += 1
                self.li += 1
            print(bundesligateam, bundesligascore, " - ", ligue1score, ligue1team)

            serieateam = (seriea.at[random.randint(0, len(seriea) - 1), "team"])
            serieascore = seriea[seriea["team"] == serieateam]["score"].values[0]
            ligue1team = (ligue1.at[random.randint(0, len(ligue1) - 1), "team"])
            ligue1score = ligue1[ligue1["team"] == ligue1team]["score"].values[0]

            if serieascore > ligue1score:
                self.s += 3
            elif serieascore < ligue1score:
                self.li += 3
            else:
                self.s += 1
                self.li += 1
            print(serieateam, serieascore, " - ", ligue1score, ligue1team)
                
            print("\n")
    
    def simulationtable(self):
        simulation = {"league":["La Liga", "Premier League", "Bundesliga", "Serie A", "Ligue 1"], "points":[self.la, self.pr, self.b, self.s, self.s]}
        df = pd.DataFrame(simulation)
        df = df.sort_values('points', ascending=False)
        print(df)