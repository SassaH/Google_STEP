def count_to(node, edges):
    index = 0
    count = 0
    while index < len(edges):
        if node == edges[index]['from']:
            count += 1
        index += 1
    return count

def initialize(nodes):
    index = 0
    while index < len(nodes):
        nodes[index]['score'] = nodes[index]['next']
        nodes[index]['next'] = 0
        index += 1
    return nodes

def search_index(nodes,edge):
    index = 0
    answer = 0
    while index < len(nodes):
        if nodes[index]['node'] == edge:
            answer = index
        index += 1
    return answer

def make_par(nodes, edges):
    index2 = 0
    while index2 < len(edges):
        index = 0
        while index < len(nodes):
            par = nodes[index]['score']/ count_to(nodes[index]['node'], edges)
            if nodes[index]['node'] == edges[index2]['from']:
                nodes[search_index(nodes,edges[index2]['to'])]['next'] += par
            index += 1
        index2 += 1
    return nodes

def partition(nodes,edges):
    count = 0
    while count < 1000:
        index = 0
        if  count_to(nodes[index]['node'], edges) != 0:
            nodes = make_par(nodes, edges)
            index += 1
        initialize(nodes)
        count += 1
    return nodes

f = open('medium_data.txt', 'r')
line = f.readline() 
count = 0
nodes = []
edges = []
ans_lst = []

while line:
    line = line.replace('\n','')
    if line.isdigit() == True:
        count = int(line)
        while count >= 0:
            line = f.readline()
            line = line.replace('\n','')
            nodes.append({'node':line,'score':100,'next':0})
            count -= 1
        else:
            count = int(line)
            line = f.readline()
        nodes.pop()
        while count > 0:
            line = line.replace('\n','')
            line2 = line.split(" ")
            token2 = {'from':line2[0],'to':line2[1]}
            edges.append(token2)
            line = f.readline()
            count -= 1
        print nodes    
        print edges
    f.close

print partition(nodes, edges)
