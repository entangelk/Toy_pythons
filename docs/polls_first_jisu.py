list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"]

list_answer =  ["좋음", "중간", "좋아지길"]

# #질문 만듦
# for count_q in [0, 1, 2, 3]:
#     pass
#     # 질문 index
#     str_questions = list_question[count_q]
#     print("{}. {}".format(count_q+1, str_questions))
# print("End program!")
# #답안 만듦
# for count_a in [0, 1, 2] :
#     pass
#     # 답안 index
#     str_answer = list_answer[count_a]
#     print("{}. {}".format(count_a+1, str_answer), end=" ")


# for count in [0, 1, 2, 3]:
#     if count <4:
#     # 질문 index
#         str_questions = list_question[count]
#         print("{}. {}".format(count+1, str_questions))
#         print("1. {} 2. {} 3. {}".format(list_answer[0], list_answer[1], list_answer[2]))
#     print("---------")
# else :
#     print("")
    
# print("End program!")

# #답안 만듦
# for count_a in [0, 1, 2] :
#     pass
#     # 답안 index
#     str_answer = list_answer[count_a]
#     print("{}. {}".format(count_a+1, str_answer), end=" ")


for count in [0, 1, 2, 3]:
    # 질문 index
        str_questions = list_question[count]
        print("{}. {}".format(count+1, str_questions))     
        for count_a in [0, 1, 2]:
                   print("{}. {}".format(count_a+1, list_answer[count_a]), end=" ")
        if count < 3 :
                print("")
                print("----")
        
    
