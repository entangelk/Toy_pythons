list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"]

list_answer =  ["좋음", "중간", "좋아지길"]



for count in [0, 1, 2, 3]:
    # 질문 index
        print("{}. {}".format(count+1, list_question[count]))     
        for count_a in [0, 1, 2]:
                   print("{}. {}".format(count_a+1, list_answer[count_a]), end=" ")
        if count < 3 :
                print("")
                print("----")
print("")
print("End program!")
    
