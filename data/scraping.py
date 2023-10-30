def scraping():

    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    from urllib.request import urlopen
    import re
    from datetime import datetime
    
    # 1.
    url = "https://www.skysports.com/la-liga-results"
    
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    soup
    
    html = soup.find_all("span", {"class":"swap-text__target"})
    html2 = soup.find_all("span", {"class":"matches__teamscores-side"})
    html3 = soup.find_all("a", {"class":"matches__item matches__link"})


    #2. 
    team = []

    for i in range(len(html)):
        if i != 0:
            team.append(html[i].text)

    score = []

    for i in range(len(html2)):
        score.append(html2[i].text.strip())

    match_link = [i.get("href") for i in html3]
    link = [(i[:-6]+"stats/"+i[-6:]) for i in match_link]


    # 3.
    all_stats = []

    for i in link:
        res = requests.get(i)
        soup = BeautifulSoup(res.content, "html.parser")
        link2 = soup.find_all("span", {"class":"sdc-site-match-stats__val"})
        for i in link2:
            all_stats.append(i.text)

    dates = []

    for i in link:
        res = requests.get(i)
        soup = BeautifulSoup(res.content, "html.parser")
        link2 = soup.find_all("time", {"class":"sdc-site-match-header__detail-time"})
        for i in link2:
            dates.append((re.findall(r'(\d{1,2}(?:st|nd|rd|th)? \w+ \d{4})', (i.text))[0]))
            dates.append((re.findall(r'(\d{1,2}(?:st|nd|rd|th)? \w+ \d{4})', (i.text))[0]))

    
    # 4.
    homeoraway = []
    possession = []
    totalshots = []
    ontarget = []
    offtarget = []
    blocked = []
    passing = []
    clearchutchances = []
    corners = []
    offsides = []
    tackles = []
    aerialduels = []
    saves = []
    foulscommited = []
    foulswon = []
    yellow = []
    red = []
    league = []

    x = 0

    for i in range(len(all_stats)):
        if x < 2:
            possession.append(all_stats[i])
            x += 1
        elif x < 4:
            totalshots.append(all_stats[i])
            x += 1
        elif x < 6:
            ontarget.append(all_stats[i])
            x += 1
        elif x < 8:
            offtarget.append(all_stats[i])
            x += 1
        elif x < 10:
            blocked.append(all_stats[i])
            x += 1
        elif x < 12:
            passing.append(all_stats[i])
            x += 1
        elif x < 14:
            clearchutchances.append(all_stats[i])
            x += 1
        elif x < 16:
            corners.append(all_stats[i])
            x += 1
        elif x < 18:
            offsides.append(all_stats[i])
            x += 1
        elif x < 20:
            tackles.append(all_stats[i])
            x += 1
        elif x < 22:
            aerialduels.append(all_stats[i])
            x += 1
        elif x < 24:
            saves.append(all_stats[i])
            x += 1
        elif x < 26:
            foulscommited.append(all_stats[i])
            x += 1
        elif x < 28:
            foulswon.append(all_stats[i])
            x += 1
        elif x < 30:
            yellow.append(all_stats[i])
            x += 1
        elif x < 31:
            red.append(all_stats[i])
            x += 1
        elif x < 32:
            red.append(all_stats[i])
            x = 0
            
    for i in range(len(possession)):
        league.append("La Liga")
        if i % 2 == 0:
            homeoraway.append("home")
        elif i % 2 != 0:
            homeoraway.append("away")
    

    # 5.
    db = {}

    db["date"] = dates
    db["league"] = league

    db["team"] = team
    db["score"] = score

    db["possession"] = possession
    db["totalshots"] = totalshots
    db["ontarget"] = ontarget
    db["offtarget"] = offtarget
    db["blocked"] = blocked
    db["passing"] = passing
    db["clearchutchances"] = clearchutchances
    db["corners"] = corners
    db["offsides"] = offsides
    db["tackles"] = tackles
    db["saves"] = saves
    db["foulscommited"] = foulscommited
    db["foulswon"] = foulswon
    db["yellow"] = yellow
    db["red"] = red

    laliga = pd.DataFrame(db)

    
    # 1.
    url = "https://www.skysports.com/premier-league-results"
    
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    soup
    
    html = soup.find_all("span", {"class":"swap-text__target"})
    html2 = soup.find_all("span", {"class":"matches__teamscores-side"})
    html3 = soup.find_all("a", {"class":"matches__item matches__link"})


    #2. 
    team = []

    for i in range(len(html)):
        if i != 0:
            team.append(html[i].text)

    score = []

    for i in range(len(html2)):
        score.append(html2[i].text.strip())

    match_link = [i.get("href") for i in html3]
    link = [(i[:-6]+"stats/"+i[-6:]) for i in match_link]


    # 3.
    all_stats = []

    for i in link:
        res = requests.get(i)
        soup = BeautifulSoup(res.content, "html.parser")
        link2 = soup.find_all("span", {"class":"sdc-site-match-stats__val"})
        for i in link2:
            all_stats.append(i.text)

    dates = []

    for i in link:
        res = requests.get(i)
        soup = BeautifulSoup(res.content, "html.parser")
        link2 = soup.find_all("time", {"class":"sdc-site-match-header__detail-time"})
        for i in link2:
            dates.append((re.findall(r'(\d{1,2}(?:st|nd|rd|th)? \w+ \d{4})', (i.text))[0]))
            dates.append((re.findall(r'(\d{1,2}(?:st|nd|rd|th)? \w+ \d{4})', (i.text))[0]))

    
    # 4.
    homeoraway = []
    possession = []
    totalshots = []
    ontarget = []
    offtarget = []
    blocked = []
    passing = []
    clearchutchances = []
    corners = []
    offsides = []
    tackles = []
    aerialduels = []
    saves = []
    foulscommited = []
    foulswon = []
    yellow = []
    red = []
    league = []

    x = 0

    for i in range(len(all_stats)):
        if x < 2:
            possession.append(all_stats[i])
            x += 1
        elif x < 4:
            totalshots.append(all_stats[i])
            x += 1
        elif x < 6:
            ontarget.append(all_stats[i])
            x += 1
        elif x < 8:
            offtarget.append(all_stats[i])
            x += 1
        elif x < 10:
            blocked.append(all_stats[i])
            x += 1
        elif x < 12:
            passing.append(all_stats[i])
            x += 1
        elif x < 14:
            clearchutchances.append(all_stats[i])
            x += 1
        elif x < 16:
            corners.append(all_stats[i])
            x += 1
        elif x < 18:
            offsides.append(all_stats[i])
            x += 1
        elif x < 20:
            tackles.append(all_stats[i])
            x += 1
        elif x < 22:
            aerialduels.append(all_stats[i])
            x += 1
        elif x < 24:
            saves.append(all_stats[i])
            x += 1
        elif x < 26:
            foulscommited.append(all_stats[i])
            x += 1
        elif x < 28:
            foulswon.append(all_stats[i])
            x += 1
        elif x < 30:
            yellow.append(all_stats[i])
            x += 1
        elif x < 31:
            red.append(all_stats[i])
            x += 1
        elif x < 32:
            red.append(all_stats[i])
            x = 0
            
    for i in range(len(possession)):
        league.append("Premier League")
        if i % 2 == 0:
            homeoraway.append("home")
        elif i % 2 != 0:
            homeoraway.append("away")
    

    # 5.
    db = {}

    db["date"] = dates
    db["league"] = league

    db["team"] = team
    db["score"] = score

    db["possession"] = possession
    db["totalshots"] = totalshots
    db["ontarget"] = ontarget
    db["offtarget"] = offtarget
    db["blocked"] = blocked
    db["passing"] = passing
    db["clearchutchances"] = clearchutchances
    db["corners"] = corners
    db["offsides"] = offsides
    db["tackles"] = tackles
    db["saves"] = saves
    db["foulscommited"] = foulscommited
    db["foulswon"] = foulswon
    db["yellow"] = yellow
    db["red"] = red

    premierleague = pd.DataFrame(db)

    
    # 1.
    url = "https://www.skysports.com/ligue-1-results"
    
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    soup
    
    html = soup.find_all("span", {"class":"swap-text__target"})
    html2 = soup.find_all("span", {"class":"matches__teamscores-side"})
    html3 = soup.find_all("a", {"class":"matches__item matches__link"})


    #2. 
    team = []

    for i in range(len(html)):
        if i != 0:
            team.append(html[i].text)

    score = []

    for i in range(len(html2)):
        score.append(html2[i].text.strip())

    match_link = [i.get("href") for i in html3]
    link = [(i[:-6]+"stats/"+i[-6:]) for i in match_link]


    # 3.
    all_stats = []

    for i in link:
        res = requests.get(i)
        soup = BeautifulSoup(res.content, "html.parser")
        link2 = soup.find_all("span", {"class":"sdc-site-match-stats__val"})
        for i in link2:
            all_stats.append(i.text)

    dates = []

    for i in link:
        res = requests.get(i)
        soup = BeautifulSoup(res.content, "html.parser")
        link2 = soup.find_all("time", {"class":"sdc-site-match-header__detail-time"})
        for i in link2:
            dates.append((re.findall(r'(\d{1,2}(?:st|nd|rd|th)? \w+ \d{4})', (i.text))[0]))
            dates.append((re.findall(r'(\d{1,2}(?:st|nd|rd|th)? \w+ \d{4})', (i.text))[0]))

    
    # 4.
    homeoraway = []
    possession = []
    totalshots = []
    ontarget = []
    offtarget = []
    blocked = []
    passing = []
    clearchutchances = []
    corners = []
    offsides = []
    tackles = []
    aerialduels = []
    saves = []
    foulscommited = []
    foulswon = []
    yellow = []
    red = []
    league = []

    x = 0

    for i in range(len(all_stats)):
        if x < 2:
            possession.append(all_stats[i])
            x += 1
        elif x < 4:
            totalshots.append(all_stats[i])
            x += 1
        elif x < 6:
            ontarget.append(all_stats[i])
            x += 1
        elif x < 8:
            offtarget.append(all_stats[i])
            x += 1
        elif x < 10:
            blocked.append(all_stats[i])
            x += 1
        elif x < 12:
            passing.append(all_stats[i])
            x += 1
        elif x < 14:
            clearchutchances.append(all_stats[i])
            x += 1
        elif x < 16:
            corners.append(all_stats[i])
            x += 1
        elif x < 18:
            offsides.append(all_stats[i])
            x += 1
        elif x < 20:
            tackles.append(all_stats[i])
            x += 1
        elif x < 22:
            aerialduels.append(all_stats[i])
            x += 1
        elif x < 24:
            saves.append(all_stats[i])
            x += 1
        elif x < 26:
            foulscommited.append(all_stats[i])
            x += 1
        elif x < 28:
            foulswon.append(all_stats[i])
            x += 1
        elif x < 30:
            yellow.append(all_stats[i])
            x += 1
        elif x < 31:
            red.append(all_stats[i])
            x += 1
        elif x < 32:
            red.append(all_stats[i])
            x = 0
            
    for i in range(len(possession)):
        league.append("Ligue 1")
        if i % 2 == 0:
            homeoraway.append("home")
        elif i % 2 != 0:
            homeoraway.append("away")
    

    # 5.
    db = {}

    db["date"] = dates
    db["league"] = league

    db["team"] = team
    db["score"] = score

    db["possession"] = possession
    db["totalshots"] = totalshots
    db["ontarget"] = ontarget
    db["offtarget"] = offtarget
    db["blocked"] = blocked
    db["passing"] = passing
    db["clearchutchances"] = clearchutchances
    db["corners"] = corners
    db["offsides"] = offsides
    db["tackles"] = tackles
    db["saves"] = saves
    db["foulscommited"] = foulscommited
    db["foulswon"] = foulswon
    db["yellow"] = yellow
    db["red"] = red

    ligue1 = pd.DataFrame(db)

    
    # 1.
    url = "https://www.skysports.com/serie-a-results"
    
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    soup
    
    html = soup.find_all("span", {"class":"swap-text__target"})
    html2 = soup.find_all("span", {"class":"matches__teamscores-side"})
    html3 = soup.find_all("a", {"class":"matches__item matches__link"})


    #2. 
    team = []

    for i in range(len(html)):
        if i != 0:
            team.append(html[i].text)

    score = []

    for i in range(len(html2)):
        score.append(html2[i].text.strip())

    match_link = [i.get("href") for i in html3]
    link = [(i[:-6]+"stats/"+i[-6:]) for i in match_link]


    # 3.
    all_stats = []

    for i in link:
        res = requests.get(i)
        soup = BeautifulSoup(res.content, "html.parser")
        link2 = soup.find_all("span", {"class":"sdc-site-match-stats__val"})
        for i in link2:
            all_stats.append(i.text)

    dates = []

    for i in link:
        res = requests.get(i)
        soup = BeautifulSoup(res.content, "html.parser")
        link2 = soup.find_all("time", {"class":"sdc-site-match-header__detail-time"})
        for i in link2:
            dates.append((re.findall(r'(\d{1,2}(?:st|nd|rd|th)? \w+ \d{4})', (i.text))[0]))
            dates.append((re.findall(r'(\d{1,2}(?:st|nd|rd|th)? \w+ \d{4})', (i.text))[0]))

    
    # 4.
    homeoraway = []
    possession = []
    totalshots = []
    ontarget = []
    offtarget = []
    blocked = []
    passing = []
    clearchutchances = []
    corners = []
    offsides = []
    tackles = []
    aerialduels = []
    saves = []
    foulscommited = []
    foulswon = []
    yellow = []
    red = []
    league = []

    x = 0

    for i in range(len(all_stats)):
        if x < 2:
            possession.append(all_stats[i])
            x += 1
        elif x < 4:
            totalshots.append(all_stats[i])
            x += 1
        elif x < 6:
            ontarget.append(all_stats[i])
            x += 1
        elif x < 8:
            offtarget.append(all_stats[i])
            x += 1
        elif x < 10:
            blocked.append(all_stats[i])
            x += 1
        elif x < 12:
            passing.append(all_stats[i])
            x += 1
        elif x < 14:
            clearchutchances.append(all_stats[i])
            x += 1
        elif x < 16:
            corners.append(all_stats[i])
            x += 1
        elif x < 18:
            offsides.append(all_stats[i])
            x += 1
        elif x < 20:
            tackles.append(all_stats[i])
            x += 1
        elif x < 22:
            aerialduels.append(all_stats[i])
            x += 1
        elif x < 24:
            saves.append(all_stats[i])
            x += 1
        elif x < 26:
            foulscommited.append(all_stats[i])
            x += 1
        elif x < 28:
            foulswon.append(all_stats[i])
            x += 1
        elif x < 30:
            yellow.append(all_stats[i])
            x += 1
        elif x < 31:
            red.append(all_stats[i])
            x += 1
        elif x < 32:
            red.append(all_stats[i])
            x = 0
            
    for i in range(len(possession)):
        league.append("Serie A")
        if i % 2 == 0:
            homeoraway.append("home")
        elif i % 2 != 0:
            homeoraway.append("away")
    

    # 5.
    db = {}

    db["date"] = dates
    db["league"] = league

    db["team"] = team
    db["score"] = score

    db["possession"] = possession
    db["totalshots"] = totalshots
    db["ontarget"] = ontarget
    db["offtarget"] = offtarget
    db["blocked"] = blocked
    db["passing"] = passing
    db["clearchutchances"] = clearchutchances
    db["corners"] = corners
    db["offsides"] = offsides
    db["tackles"] = tackles
    db["saves"] = saves
    db["foulscommited"] = foulscommited
    db["foulswon"] = foulswon
    db["yellow"] = yellow
    db["red"] = red

    seriea = pd.DataFrame(db)

    
    # 1.
    url = "https://www.skysports.com/bundesliga-results"
    
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    soup
    
    html = soup.find_all("span", {"class":"swap-text__target"})
    html2 = soup.find_all("span", {"class":"matches__teamscores-side"})
    html3 = soup.find_all("a", {"class":"matches__item matches__link"})


    #2. 
    team = []

    for i in range(len(html)):
        if i != 0:
            team.append(html[i].text)

    score = []

    for i in range(len(html2)):
        score.append(html2[i].text.strip())

    match_link = [i.get("href") for i in html3]
    link = [(i[:-6]+"stats/"+i[-6:]) for i in match_link]


    # 3.
    all_stats = []

    for i in link:
        res = requests.get(i)
        soup = BeautifulSoup(res.content, "html.parser")
        link2 = soup.find_all("span", {"class":"sdc-site-match-stats__val"})
        for i in link2:
            all_stats.append(i.text)

    dates = []

    for i in link:
        res = requests.get(i)
        soup = BeautifulSoup(res.content, "html.parser")
        link2 = soup.find_all("time", {"class":"sdc-site-match-header__detail-time"})
        for i in link2:
            dates.append((re.findall(r'(\d{1,2}(?:st|nd|rd|th)? \w+ \d{4})', (i.text))[0]))
            dates.append((re.findall(r'(\d{1,2}(?:st|nd|rd|th)? \w+ \d{4})', (i.text))[0]))

    
    # 4.
    homeoraway = []
    possession = []
    totalshots = []
    ontarget = []
    offtarget = []
    blocked = []
    passing = []
    clearchutchances = []
    corners = []
    offsides = []
    tackles = []
    aerialduels = []
    saves = []
    foulscommited = []
    foulswon = []
    yellow = []
    red = []
    league = []

    x = 0

    for i in range(len(all_stats)):
        if x < 2:
            possession.append(all_stats[i])
            x += 1
        elif x < 4:
            totalshots.append(all_stats[i])
            x += 1
        elif x < 6:
            ontarget.append(all_stats[i])
            x += 1
        elif x < 8:
            offtarget.append(all_stats[i])
            x += 1
        elif x < 10:
            blocked.append(all_stats[i])
            x += 1
        elif x < 12:
            passing.append(all_stats[i])
            x += 1
        elif x < 14:
            clearchutchances.append(all_stats[i])
            x += 1
        elif x < 16:
            corners.append(all_stats[i])
            x += 1
        elif x < 18:
            offsides.append(all_stats[i])
            x += 1
        elif x < 20:
            tackles.append(all_stats[i])
            x += 1
        elif x < 22:
            aerialduels.append(all_stats[i])
            x += 1
        elif x < 24:
            saves.append(all_stats[i])
            x += 1
        elif x < 26:
            foulscommited.append(all_stats[i])
            x += 1
        elif x < 28:
            foulswon.append(all_stats[i])
            x += 1
        elif x < 30:
            yellow.append(all_stats[i])
            x += 1
        elif x < 31:
            red.append(all_stats[i])
            x += 1
        elif x < 32:
            red.append(all_stats[i])
            x = 0
            
    for i in range(len(possession)):
        league.append("Bundesliga")
        if i % 2 == 0:
            homeoraway.append("home")
        elif i % 2 != 0:
            homeoraway.append("away")
    

    # 5.
    db = {}

    db["date"] = dates
    db["league"] = league

    db["team"] = team
    db["score"] = score

    db["possession"] = possession
    db["totalshots"] = totalshots
    db["ontarget"] = ontarget
    db["offtarget"] = offtarget
    db["blocked"] = blocked
    db["passing"] = passing
    db["clearchutchances"] = clearchutchances
    db["corners"] = corners
    db["offsides"] = offsides
    db["tackles"] = tackles
    db["saves"] = saves
    db["foulscommited"] = foulscommited
    db["foulswon"] = foulswon
    db["yellow"] = yellow
    db["red"] = red

    bundesliga = pd.DataFrame(db)

    allmatches = pd.concat([premierleague, laliga, ligue1, seriea, bundesliga], ignore_index=True)
    allmatches.to_csv("tables/top5leagues.csv", index=False)