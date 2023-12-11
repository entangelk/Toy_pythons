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


# class solv:
#     def __init__(self,list_question,list_answer) -> None:
#         self.answer_list=[]
#         self.list_answer=list_answer
#         self.list_question = list_question
#         pass

    # def print_question(self) :
answer_list=[]
for num_count in range(len(list_question)) :    # 질문-답안-input 반복
    print("{}. {}".format(num_count+1, list_question[num_count])) 
    print("{}".format(list_answer[num_count]))
    answer_list.append(int(input("-정답 : ")))
    print("")    
    # self.listing_answer()
    # return 