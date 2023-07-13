quizes = [
    ['Question 1', ['Ans 1', 'Ans 2', 'Ans 3', 'Ans 4']],
    ['Question 2', ['Ans 1', 'Ans 2', 'Ans 3', 'Ans 4']],
    ['Question 3', ['Ans 1', 'Ans 2', 'Ans 3', 'Ans 4']],
    ['Question 4', ['Ans 1', 'Ans 2', 'Ans 3', 'Ans 4']],
    ['Question 5', ['Ans 1', 'Ans 2', 'Ans 3', 'Ans 4']],
]

answers = [1, 2, 2, 3, 4]

def calculate_score(user_ans):
    score = 0
    for i in range(len(user_ans)):
        if user_ans[i] == answers[i]:
            score += 1
    return score

def prompt_quiz(quiz):
    print('-'*40)
    print(quiz[0])
    print()
    for i in range(4):
        print('[' + str(i + 1) + '] ' + quiz[1][i]) 
    print()
    print('-'*40)

def play():
    user_ans = [] 
    for i in range(len(quizes)):
        prompt_quiz(quizes[i])
        ans = 0
        while ans < 1 or ans > 4:
            ans = int(input('Your answer: '))
        user_ans.append(ans)
    score = calculate_score(user_ans)
    print('Your score is ' + str(score))

play()