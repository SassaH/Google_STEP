import copy

def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta *= 0.1
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index

def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readBy(line, index):
    token = {'type': 'BY'}
    return token, index + 1

def readDiv(line, index):
    token = {'type': 'DIV'}
    return token, index + 1

def readParL(line, index):
    token = {'type': 'LEFT'}
    return token, index + 1

def readParR(line, index):
    token = {'type': 'RIGHT'}
    return token, index + 1

def find_right(tokens):
    index = 0
    count = -1
    inside = True
    while index< len(line) and inside == True:
        if tokens[index]['type'] == 'RIGHT':
            count += 1
        elif tokens[index]['type'] == 'LEFT':
            count -= 1
        if count == 0:
            inside = False
        #print  tokens[index], count
        index += 1
    return index

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readBy(line, index)
        elif line[index] == '/':
            (token, index) = readDiv(line, index)
        elif line[index] == '(':
            (token, index) = readParL(line, index)
        elif line[index] == ')':
            (token, index) = readParR(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens

def evaluate_by(tokens):
    if tokens[0] !=  {'type': 'PLUS'}:
        tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    tokens2 = []
    ans=0
    while index < len(tokens):
        #print index
        #print tokens
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index-1]['type'] == 'PLUS' or tokens[index-1]['type'] == 'MINUS':
                #pass
                tokens2.append(tokens[index-1])
                tokens2.append(tokens[index])
                
            elif tokens[index-1]['type'] == 'BY':
                ans = tokens2[len(tokens2)-1]['number'] * tokens[index]['number']
                # ans = tokens[index-2]['number'] * tokens[index]['number']
                # del tokens[index-2:index+1]
                # tokens.insert(index-2,ans)
                # index = index-2
                tokens2.pop()
                tokens2.append({'type': 'NUMBER', 'number': ans})
            elif tokens[index-1]['type'] == 'DIV':
                #ans = tokens[index-2]['number'] / tokens[index]['number']
                #del tokens[index-2:index+1]
                #tokens.insert(index-2,ans)
                #index = index-2             


                ans = tokens2[len(tokens2)-1]['number'] / tokens[index]['number']
                tokens2.pop()
                tokens2.append({'type': 'NUMBER', 'number': ans})
            else:
                print 'evaluate_by is Invalid syntax'
            
        #print tokens2
        index += 1
        #print index
    else:
        tokens2 = evaluate(tokens2[1:])
    #    index = len(tokens)
    return tokens2


def evaluate(tokens):
    if tokens[0] !=  {'type': 'PLUS'}:
        tokens.insert(0, {'type': 'PLUS'})
    answer = 0
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'evaluate is Invalid syntax'
        index += 1
    return answer

def evaluate_par(tokens):
    index = 0
    tokens2 = []
    ans = 0
    inside = True 
    #print tokens
    while index < len(tokens) :#and inside:
        #print index, tokens2
        if tokens[index]['type'] == 'LEFT':
            right = find_right(tokens[index:]) 
            value = evaluate_par(tokens[index+1:right])
            print value
            del tokens[index:right+1]
            tokens.insert(index, value)
            print tokens
            #tokens2 = tokens2 + evaluate_par(tokens[index+1:]) 
            #index = index + find_right(tokens[index2:]) 
            #print find_right(tokens[index2:]) 
        index += 1
    else:
            ans = evaluate(evaluate_by(tokens))
            tokens = [{'type': 'NUMBER', 'number':ans}]
            print tokens
           # index += 1
        #elif tokens[index]['type'] == 'RIGHT':
         #   tokens.pop();
         #   ans = evaluate(evaluate_by(tokens))
         #   tokens = {'type': 'NUMBER', 'number':ans}
         #   #print tokens
            #index += 1
     #   else:
            #tokens2.append(tokens[index])
     #       index += 1
        #index += 1
      
    return tokens  

while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    tokens2 = evaluate_par(tokens)
    #tokens3 = evaluate_by(tokens2)
    #answer = evaluate(tokens3)
    print "answer = %f\n" % tokens2[0]['number']
    # print find_right(tokens[1:])
    #print evaluate_by(tokens)
