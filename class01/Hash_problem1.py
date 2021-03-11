def solution(participant, completion):
    # participant = ["park", "kim", "choi", "gi"]
    # completion = ["park", "kim", "choi"]


    # 빈 딕셔너리를 생성
    d = {}

    for x in participant:
        d[x] = d.get(x, 0) + 1
    # {'park': 1, 'kim': 1, 'choi': 1, 'gi': 1} participant 안에 x 값이 있으면 +1 을 해준다 두번 반복되면 +2 가 댄다
    for x in completion:
        d[x] -= 1
    # {'park': 0, 'kim': 0, 'choi': 0, 'gi': 1} completion 안에 x 값이 돌면 -1 을 해준다 gi는 completion 안에 없기 떄문에 1이 남아있다

    dnf = [k for k, v in d.items() if v > 0]
    # ['gi'] 남는다. 그 이유는 1이 남아 있기때문에
    answer = dnf[0]
    # 리스트 0번쨰가 정답
    return answer
