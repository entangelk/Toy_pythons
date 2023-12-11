answer_list = [2,1,1,2]

class solv:
    def __init__(self,answer_list) -> None:
        self.answer_list=answer_list
        self.sum_score=0
        self.score=[]
        self.correct=[2,1,1,2]
        self.sum_level=''
        self.score_problem=[10,15,10,5]
        pass

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
        
sol = solv(answer_list)
sol.init_list()
sol.level_check()
sol.print_result()
