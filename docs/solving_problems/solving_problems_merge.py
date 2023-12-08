## source from JISU docs/project_test/parts/testparts_jisu.py

def test() :
    
    list_question = [   # 질문 list
            'Python에서 변수를 선언하는 방법은? (점수: 10점)'
            ,'Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)'
            ,'Python에서 조건문을 작성하는 방법은? (점수: 10점)'
            ,'Python에서 함수를 정의하는 방법은? (점수: 5점)'    
    ]
    
    list_answer = [     # 답안 list
        '1) var name 2) name = value 3) set name 4) name == value'
        ,'1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다'
        ,'1) if-else, 2) for-in, 3) while, 4) def'
        ,'1) class, 2) def, 3) import, 4) return'
    ]
    
    num_print_answer=[]
    for num_count in range(len(list_question)) :    # 질문-답안-input 반복
        print("{}. {}".format(num_count+1, list_question[num_count])) 
        print("{}".format(list_answer[num_count]))
        num_print_answer.append(int(input("-정답 : ")))
        print("")      
    return num_print_answer # user의 답변 return list return

## source from YOHAN docs/project_test/parts/testparts_yohan.py
def solve_result(answer_list):  # 결과값 계산 function
    correct=[2,1,1,2]   # 문제 정답 리스트
    score=[]    # 점수 저장 리스트
    score_problem=[10,15,10,5]  # 문제당 점수 리스트
    sum_score=0     # 점수 합계 변수 초기화

    for i in range(len(correct)): 
        if answer_list[i] == correct[i]:    # 입력과 정답이 동일할 경우
            score.append(score_problem[i])  # 점수 저장 리스트에 문제당 점수 저장
            pass
        pass
    for i in range(len(score)):     # 점수 저장 리스트의 아이템을 점수 합계 변수에 저장
        sum_score += score[i]
        pass
    if sum_score >= 30:     # 합계 점수의 단계별 등급 표현
        sum_level = "A"
        pass
    elif sum_score >= 20:
        sum_level = 'B'
        pass
    else :
        sum_level = 'C'
        pass
    print("응답한 내용 : ", end=" ")
    for i in range(len(correct)):   # 응답리스트 출력
        print("{}번 {}".format(i+1,answer_list[i]), end=" ")
        pass
    print("\n당신 응답 합계 : {}점".format(sum_score))  # 합계 점수 출력
    print("학점은 {} 입니다.".format(sum_level))    # 계산된 학점 출력
    pass
    return


solve_result(test())

