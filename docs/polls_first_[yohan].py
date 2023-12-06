list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]

list_answer =  ["좋음", "중간", "좋아지길"]


for num_count in range(len(list_question)): # list_question의 아이템 갯수만큼 반복
    print("{}".format(list_question[num_count]))
    for num_second_count in range(len(list_answer)): # list_answer의 아이템 갯수만큼 반복
        print("{}. {}".format(num_second_count+1,list_answer[num_second_count]),end=" ") # 아이템 갯수 index+1을 번호로 지정
        pass
    pass

#뭘 넘겨줘야 할지 몰라서 제일 어려운 중간에 선 3개 긋는거...?