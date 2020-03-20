import copy

# 전역변수 선언
state = [1, [3, 3], [0, 0]]
action = [1, 0, 0]
goal = [2, [0, 0], [3, 3]]
visited = []
stack = []
temp = []


# 함수선언
# 왼쪽에서 오른쪽으로 가는 움직임 반환
def LtoRaction():
    return [[1, 1, 1], [1, 1, 0], [1, 2, 0], [1, 0, 1], [1, 0, 2]]


# 오른쪽에서 왼쪽으로 가는 움직임 반환
def RtoLaction():
    return [[2, 1, 1], [2, 1, 0], [2, 2, 0], [2, 0, 1], [2, 0, 2]]


# 스테이트와 액션에 맞게 움직이기
def move(state, action):
    after_state = [0, [0, 0], [0, 0]]
    after_state = copy.deepcopy(state)
    if (action[0] == state[0]):
        # 보트가 왼쪽에서 오른쪽으로 움직이는 행동
        if (after_state[0] == 1):
            after_state[0] = 2
            after_state[1][0] = after_state[1][0] - action[1]
            after_state[1][1] = after_state[1][1] - action[2]
            after_state[2][0] = after_state[2][0] + action[1]
            after_state[2][1] = after_state[2][1] + action[2]
        # 보트가 오른쪽에서 왼쪽으로 움직이는 행동
        elif (after_state[0] == 2):
            after_state[0] = 1
            after_state[1][0] = after_state[1][0] + action[1]
            after_state[1][1] = after_state[1][1] + action[2]
            after_state[2][0] = after_state[2][0] - action[1]
            after_state[2][1] = after_state[2][1] - action[2]

        return after_state

    else:
        print("@ @ @ 보트의 위치와 action의 시작 위치가 맞지 않습니다.@ @ @")
        return 0


# 올바른 움직임 인지 체크
def check(after_state):
    left = after_state[1]
    right = after_state[2]
    # 선교사 또는 식인종의 수가 음수이면 잘못된 것
    if (left[0] < 0) or (left[1] < 0) or (right[0] < 0) or (right[1] < 0):
        return -1
    # 선교사 또는 식인종의 수가 4를 넘으면 잘못된 것
    elif (left[0] >= 4) or (left[1] >= 4) or (right[0] >= 4) or (right[1] >= 4):
        return -1
    # 왼쪽, 오른쪽 모두 선교사의 숫자가 식인종보다 크거나 많아야함
    elif (left[0] >= left[1]) and (right[0] >= right[1]):
        return 1
    # 왼쪽 선교사의 숫자가 0일때 오른쪽의 선교사의 숫자가 3이면 정상
    elif (left[0] == 0) and (right[0] == 3):
        return 2
    # 왼쪽 선교사의 숫자가 3일때 오른쪽의 선교사의 숫자가 0이면 정상
    elif (left[0] == 3) and (right[0] == 0):
        return 2
    else:
        return -3


# 목표에 도달했을때 과정 출력
def done(list):
    print("끝!", list)
    temp = []
    num = -1
    while list:
        temp = list.pop(0)
        num += 1
        if (temp[0] == 1):
            print("Moon.B.W   * * * * * 현재상태 * * * * *", num, "번째 움직임")
            print(" --------------------------------------------------")
            print("|                  ||~~~~~~~~~~||                  |")
            print("|   선교사 : %d명   ||~~~~~~~~~~||   선교사 : %d명   |" % (temp[1][0], temp[2][0]))
            print("|                  ||<->~~~~~~~||                  |")
            print("|   식인종 : %d명   ||~~~~~~~~~~||   식인종 : %d명   |" % (temp[1][1], temp[2][1]))
            print("|                  ||~~~~~~~~~~||                  |")
            print(" --------------------------------------------------")

        elif (temp[0] == 2):
            print("Moon.B.W   * * * * * 현재상태 * * * * *", num, "번째 움직임")
            print(" --------------------------------------------------")
            print("|                  ||~~~~~~~~~~||                  |")
            print("|   선교사 : %d명   ||~~~~~~~~~~||   선교사 : %d명   |" % (temp[1][0], temp[2][0]))
            print("|                  ||~~~~~~~<->||                  |")
            print("|   식인종 : %d명   ||~~~~~~~~~~||   식인종 : %d명   |" % (temp[1][1], temp[2][1]))
            print("|                  ||~~~~~~~~~~||                  |")
            print(" --------------------------------------------------")
    print("움직인 횟수 :", num, "번")


# 깊이 우선 탐색으로 솔루션 찾기
def DFS():
    global stack, visited, goal
    while stack:
        none = 0
        # 하나의 노드를 꺼내서 탐색 시작
        now_state = stack.pop()
        state = copy.deepcopy(now_state)
        # 기록
        visited.extend([now_state])
        # 보트가 왼쪽에 있는 상태
        if (now_state[0] == 1):
            if (now_state == goal):
                print("탐색 성공!")
                done(visited)
                return 0
            else:
                available_action = LtoRaction()
                while (available_action):
                    action = available_action.pop()
                    after_state = move(now_state, action)
                    can = check(after_state)
                    if (can > 0):
                        if after_state not in visited:
                            none = 1
                            stack.extend([after_state])
                    else:
                        pass
                if (none == 0):
                    visited.pop()

        # 보트가 오른쪽에 있는 상태
        elif (now_state[0] == 2):
            if (now_state == goal):
                print("탐색 성공!")
                done(visited)
                return 0
            else:
                available_action = RtoLaction()
                while (available_action):
                    action = available_action.pop()
                    after_state = move(now_state, action)
                    can = check(after_state)
                    if (can > 0):
                        if after_state not in visited:
                            none = 1
                            stack.extend([after_state])
                    else:
                        pass
                if (none == 0):
                    visited.pop()


# 실행
stack.extend([state])
DFS()

