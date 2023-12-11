
## source from JISU docs/project_test/parts/testparts_jisu.py


# 출력과 입력으로 나눔.

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


class solv:
    def __init__(self,list_question,list_answer) -> None:
        self.list_answer= list_answer
        self.list_question = list_question
        self.answer_list=[]
        self.sum_score=0
        self.score=[]
        self.correct=[2,1,1,2]
        self.sum_level=''
        self.score_problem=[10,15,10,5]
        pass

    def print_question(self) :
        for num_count in range(len(self.list_question)) :    # 질문-답안-input 반복
            print("{}. {}".format(num_count+1, self.list_question[num_count])) 
            print("{}".format(self.list_answer[num_count]))
            self.answer_list.append(int(input("-정답 : ")))
            print("")    
            # self.listing_answer()
        return self.answer_list
    
    
    def listing_answer(self) :
        return self.answer_list # user의 답변 list - return

    def init_list(self):
        for i in range(len(self.correct)):
            if self.answer_list[i] == self.correct[i]:
                self.score.append(self.score_problem[i])
                pass
            pass

    def level_check(self):
        for i in range(len(self.score)):
            self.sum_score += self.score[i]
            pass
        if self.sum_score >= 30:
            self.sum_level = "A"
            pass
        elif self.sum_score >= 20:
            self.sum_level = 'B'
            pass
        else :
            self.sum_level = 'C'
            pass
        return self.sum_level
    
    def print_result(self):
        print("응답한 내용 : ", end=" ")
        for i in range(len(self.correct)):
            print("{}번 {}".format(i+1,self.answer_list[i]), end=" ")
            pass
        print("\n당신 응답 합계 : {}점".format(self.sum_score))
        print("학점은 {} 입니다.".format(self.sum_level))
        return
    
sol = solv(list_question,list_answer)
sol.print_question()
sol.listing_answer()
sol.init_list()
sol.level_check()
sol.print_result()