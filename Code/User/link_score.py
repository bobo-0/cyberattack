from py2neo import Graph
import json
import numpy as np

#고정!! 바꾸면 안됨!!
json_data=open('/Users/junha_lee/documents/junha/study/projects/predictcyberattacks/crawling/follow/1000/Relationship_100.json').read()
data = json.loads(json_data)

    

def setting():
    
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "1"
    
    graph = Graph(uri=uri, user=user, password=password)
    graph.run("CREATE CONSTRAINT ON (n:Hackers) ASSERT n.username IS UNIQUE")
    graph.run("CREATE CONSTRAINT ON (n:NotHackers) ASSERT n.username IS UNIQUE")


# 특정 한 명의 해커에 대해서 그 해커와 가장 가까운 5명의 잠재적 해커 추출
def link_score_top(userid, standard):
        
    hackers = []
    
    for i in range(0, len(data)):
        hackers.append(str(data[i]['username']))

    
    index = hackers.index(str(userid))
    
    nonhackers = []
    score = []
    
    
    for i in range(0, len(data[index]["following"])):
        nonhackers.append(str(data[index]["following"][i]))
    for i in range(0, len(data[index]["follower"])):
        nonhackers.append(str(data[index]["follower"][i]))
        
        
        
    nonhackers =  list(set(nonhackers) - set(hackers))
    
    
    for i in range(0, len(nonhackers)):
        score.append(graph.run('MATCH (p1:Hackers {username: "'+str(userid)+'"}) MATCH (p2:NotHackers {username: "'+str(nonhackers[i])+'"}) RETURN algo.linkprediction.adamicAdar(p1, p2) AS score').data()[0]['score'])

        
    top = []
    top_score = []
    
    for i in range(0,len(score)):
        if max(score) > standard:
            top.append(nonhackers[score.index(max(score))])
            top_score.append(max(score))
            score.remove(max(score))
        else:
            break;
    
    
#    for i in range(0, len(top)):
#        print(str(userid)+"'s top"+str((i+1))+" : "+str(top[i])+"     score :  "+str(top_score[i]))
        
    return top
    





# 특정 한 명의 해커에 대해서 다른 해커와 특정 해커와의 평균 link score
def hacker_and_hacker_linkscore(userid):
    
    hackers = []
    
    for i in range(0, len(data)):
        hackers.append(str(data[i]['username']))
    
    index = hackers.index(str(userid))
    
    hackers.remove(hackers[index])

    score = []

    for i in range(0, len(hackers)):
        score.append(graph.run('MATCH (p1:Hackers {username: "'+str(userid)+'"}) MATCH (p2:Hackers {username: "'+str(hackers[i])+'"}) RETURN algo.linkprediction.adamicAdar(p1, p2) AS score').data()[0]['score'])
    
    avg = sum(score)/len(score)
    
    return avg
    


# 특정 한 명의 잠재적 해커와 다른 여러 해커들 사이의 평균 link score
def nonhacker_and_hacker_linkscore(userid):
            
    hackers = []
    
    for i in range(0, len(data)):
        hackers.append(str(data[i]['username']))
        
    score = []

    for i in range(0, len(hackers)):
        score.append(graph.run('MATCH (p1:NotHackers {username: "'+str(userid)+'"}) MATCH (p2:Hackers {username: "'+str(hackers[i])+'"}) RETURN algo.linkprediction.adamicAdar(p1, p2) AS score').data()[0]['score'])
        
    avg = sum(score)/len(score)
    
    if avg > 21.2583:
        print(str(userid)+"'s avg : "+str(avg))

    
    
    
    
    
    
if __name__ == '__main__':

    
users = [18983429,71522953,1590754944,128484298,56179836,218798348,100564168]


for j in range(0, len(users)):
    
    # 1. 특정 해커와 다른 해커들간의 link score를 구한다
    score = hacker_and_hacker_linkscore(users[j])
    
    # 2. 1에서 구한 link score보다 높은 잠재적 해커(특정 해커들의 following-follower)들을 구한다.
    result = link_score_top(users[j],score)
    
    # 3. 2에서 구한 잠재적 해커들과 해커들간의 link score를 구해서 21.2583다 높으면 너는 해커다
    for i in range(0, len(result)):
        nonhacker_and_hacker_linkscore(result[i])
    print j





sample = data

for i in range(0, 5):
    sample.append(data[i])
    
    
    
    
for i in range(0, len(sample)):
    for k in range(0, len(sample[i]['following'])):
        print str(sample[i]['username'])+' / '+str(sample[i]['following'][k])
    for k in range(0, len(sample[i]['follower'])):
        print str(sample[i]['username'])+' / '+str(sample[i]['follower'][k])
    
    
    
    
for i in range(0, len(sample)):
    for k in range(0, len(sample[i]['following'])):
        print graph.run('MATCH (p1:Hackers {username: "'+str(sample[i]['username'])+'"}) MATCH (p2:Hackers {username: "'+str(sample[i]['following'][k])+'"}) RETURN algo.linkprediction.adamicAdar(p1, p2) AS score').data()[0]['score']
    for k in range(0, len(sample[i]['follower'])):
        print graph.run('MATCH (p1:NotHackers {username: "'+str(sample[i]['follower'][k])+'"}) MATCH (p2:Hackers {username: "'+str(sample[i]['username'])+'"}) RETURN algo.linkprediction.adamicAdar(p1, p2) AS score').data()[0]['score']







hackers = []
nonhackers = []

        
for user in range(0,len(data)):
    hackers.append(str(data[user]['username']))


for user in range(0,len(data)):
    
    for following in range(0,len(data[user]['following'])):
        if str(data[user]['following'][following]) not in hackers:
            nonhackers.append(data[user]['following'][following])
        
        
    for follower in range(0,len(data[user]['follower'])):
        if str(data[user]['follower'][follower]) not in hackers:
            nonhackers.append(data[user]['follower'][follower])


real_hackers=list(set(hackers))
real_nonhackers=list(set(nonhackers))







users = []

for i in range(0, len(sample)):
     users.append(str(sample[i]['username']))
     
     for k in range(0, len(sample[i]['following'])):
         users.append(str(sample[i]['following'][k]))
     for k in range(0, len(sample[i]['follower'])):
         users.append(str(sample[i]['follower'][k]))


real_hackers = []

for i in range(0, len(sample)):
     real_hackers.append(str(sample[i]['username']))


real_nonhackers = list(set(users) - set(real_hackers))



for i in range(0,len(sample)):
    
    for k in range(0,len(sample[i]['following'])):
        if str(sample[i]['following'][k]) in real_nonhackers:
            score = str(float(graph.run('MATCH (p1:Hackers {username: "'+str(sample[i]['username'])+'"}) MATCH (p2:NotHackers {username: "'+str(sample[i]['following'][k])+'"}) RETURN algo.linkprediction.adamicAdar(p1, p2) AS score').data()[0]['score']))
            graph.run('match (a:Hackers)-[r:follow]->(b:NotHackers) where a.username = "'+str(sample[i]['username'])+'" and b.username="'+str(sample[i]['following'][k])+'" set r.weight='+str(score))
        else :
            score = str(float(graph.run('MATCH (p1:Hackers {username: "'+str(sample[i]['username'])+'"}) MATCH (p2:Hackers {username: "'+str(sample[i]['following'][k])+'"}) RETURN algo.linkprediction.adamicAdar(p1, p2) AS score').data()[0]['score']))
            graph.run('match (a:Hackers)-[r:follow]->(b:Hackers) where a.username = "'+str(sample[i]['username'])+'" and b.username="'+str(sample[i]['following'][k])+'" set r.weight='+str(score))

    for k in range(0, len(sample[i]['follower'])):
        if str(sample[i]['follower'][k]) in real_nonhackers:
            score = float(graph.run('MATCH (p1:NotHackers {username: "'+str(sample[i]['follower'][k])+'"}) MATCH (p2:Hackers {username: "'+str(sample[i]['username'])+'"}) RETURN algo.linkprediction.adamicAdar(p1, p2) AS score').data()[0]['score'])
            graph.run('match (a:NotHackers)-[r:follow]->(b:Hackers) where a.username = "'+str(sample[i]['username'])+'" and b.username="'+str(sample[i]['follower'][k])+'" set r.weight='+str(score))
        else:
            score = str(float(graph.run('MATCH (p1:Hackers {username: "'+str(sample[i]['username'])+'"}) MATCH (p2:Hackers {username: "'+str(sample[i]['following'][k])+'"}) RETURN algo.linkprediction.adamicAdar(p1, p2) AS score').data()[0]['score']))
            graph.run('match (a:Hackers)-[r:follow]->(b:Hackers) where a.username = "'+str(sample[i]['username'])+'" and b.username="'+str(sample[i]['following'][k])+'" set r.weight='+str(score))

    print str(len(sample))+' / '+str(i)










