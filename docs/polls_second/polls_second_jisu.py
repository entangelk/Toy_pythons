# sorce yohan from ../pools_first/polls_first_[yohan].py
# 코드가 지저분해서... 미안해요... 미안.... 안녕...

list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]


list_answer =  ["좋음", "중간", "좋아지길"]

list_answer_result = [0, 0, 0]


for num_count in range(len(list_question)): # list_question의 아이템 갯수만큼 반복
    print("{}. {}".format(num_count+1,list_question[num_count]))
    for num_second_count in range(len(list_answer)): # list_answer의 아이템 갯수만큼 반복
        print("{}. {}".format(num_second_count+1,list_answer[num_second_count]),end=" ") # 아이템 갯수 index+1을 번호로 지정 2번째 라인까지
    pass
    print("")
    print("")
    num_print_answer= int(input("당신 생각은 몇 번 : ")) # num으로 input 받기
    index=num_print_answer-1 # index form으로 만들기
    list_answer_result[index]=list_answer_result[index]+1 #list_answer_result(list)에 답항 count
    if num_count != 3:
        print("--------------------------------------")
        #input으로 답항 받기
    else :
        print("")
    pass  
    pass
 
#list_answer_result 표시하기
print("설문자 답항별 갯수 표시 : 1({}) 2({}) 3({})".format(list_answer_result[0],list_answer_result[1],list_answer_result[2] ))
#list_answer_result의 가중 평균 구하기
list_answer_average= (3*list_answer_result[0]+2*list_answer_result[1]+1*list_answer_result[2])/(3+2+1)
print("답항 가중 평균 : {}".format(list_answer_average))
