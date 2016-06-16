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
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens

def evaluate_by(tokens):
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    tokens2 = []
    ans=0
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                tokens2.append(tokens[index-1])
                tokens2.append(tokens[index])
            elif tokens[index - 1]['type'] == 'MINUS':
                tokens2.append(tokens[index-1])
                tokens2.append(tokens[index])
            elif tokens[index - 1]['type'] == 'BY':
                ans = tokens[index-2]['number'] * tokens[index]['number']
                tokens2.pop()
                tokens2.append({'type': 'NUMBER', 'number': ans})
            elif tokens[index - 1]['type'] == 'DIV':
                ans = tokens[index-2]['number'] / tokens[index]['number']
                tokens2.pop()
                tokens2.append({'type': 'NUMBER', 'number': ans})
            else:
                print 'Invalid syntax'
        index += 1
    return tokens2


def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer


while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    tokens2 = evaluate_by(tokens)
    answer = evaluate(tokens2)
    print "answer = %f\n" % answer
