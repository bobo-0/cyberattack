from py2neo import Graph
import json

json_data=open('/Users/junha_lee/Desktop/tweets/random/random_100_relation.json').read()

data = json.loads(json_data)


def setting():
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "1"
    
    graph = Graph(uri=uri, user=user, password=password)
    graph.run("CREATE CONSTRAINT ON (n:Hackers) ASSERT n.username IS UNIQUE")
    graph.run("CREATE CONSTRAINT ON (n:NotHackers) ASSERT n.username IS UNIQUE")

def delete_all_node():
    graph.delete_all()
    
def create_all_node():
    
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
    
    
    for i in range(0,len(real_hackers)):
        graph.run('create (u:Hackers {username:"'+str(real_hackers[i])+'"})')
    for i in range(0,len(real_nonhackers)):
        graph.run('create (u:NotHackers {username:"'+str(real_nonhackers[i])+'"})')
        
    
      
        
        
        
        
    
    
def create_all_rel():
    
    for i in range(0,len(data)):
        for n in range(0,len(data[i]['following'])):
            graph.run("match (a:Hackers),(b:Hackers) "+"where a.username='"+str(data[i]['username'])+"' and b.username='"+str(data[i]['following'][n])+"' "+"create unique (a)-[:follow]->(b)")  
            graph.run("match (a:NotHackers),(b:Hackers) "+"where a.username='"+str(data[i]['username'])+"' and b.username='"+str(data[i]['following'][n])+"' "+"create unique (a)-[:follow]->(b)")  
            graph.run("match (a:Hackers),(b:NotHackers) "+"where a.username='"+str(data[i]['username'])+"' and b.username='"+str(data[i]['following'][n])+"' "+"create unique (a)-[:follow]->(b)")  
    
    for i in range(0,len(data)):
        for n in range(0,len(data[i]['follower'])):
            graph.run("match (a:NotHackers),(b:Hackers) "+"where a.username='"+str(data[i]['username'])+"' and b.username='"+str(data[i]['follower'][n])+"' "+"create unique ((b)-[:follow]->(a))")  
            graph.run("match (a:Hackers),(b:NotHackers) "+"where a.username='"+str(data[i]['username'])+"' and b.username='"+str(data[i]['follower'][n])+"' "+"create unique ((b)-[:follow]->(a))")  



def set_attribute():
    
    for user in range(0,len(data)):
        graph.run("merge(n:Hackers {username:'"+data[user]['username'] +"'}) set n = {username:'"+   data[user]['username']  +"'}")








if __name__ == '__main__':
    
    delete_all_node()
    
    create_all_node()
    
    create_all_rel()
    
    set_attribute()
    

    
    
    
    