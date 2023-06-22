#blue acaive gacha simulation ver 1.0
import sys
import random
print("En or Kr")
langu=input()
if(langu == "Kr" or langu == "kr" or langu == "kR" or langu == "KR"):
    print("페스일경우 p를 눌러주세요.")
    pok=input()
    if(pok == "p"):
        print("페스에 들어가는 픽업 학생수를 입력해주세요.")
        stu=int(input())
    else:
        print("픽업 학생수를 입력해주세요")
        stu=int(input())
    print("모든가차 확률은 블루아카이브 확률 공시에 따라 결정됩니다.")
    print("학생의 이름을 입력해주세요.(주픽업학생이 첫번째로)")
    if(pok=="p"):
        name=list(map(str,input().split()))
    else:
        nm1=list(map(str,input().split()))
    print("뽑기횟수를 입력해주세요, (미입력시 오류발생합니다.")
    gn= int(input())
    if(pok =="p"):
        for c in range (gn):
            rand_num = int(random.randint(0, 99999))
            if (rand_num <=5999):
                if(rand_num <= 699):
                    print(name[0] + "," , c)
                else:
                    if(rand_num>699 and (stu-1)*300+700>rand_num):
                        num_ran = int(random.randint(2,stu))
                        print(name[num_ran-1] + "," , c)
                    else:
                        print("3성 상시 픽업, " , c)
    else:
         for c in range (gn):
            rand_num = int(random.randint(0, 99999))
            if (rand_num <=2999):
                if(rand_num<=699):
                    print(nm1[0] + "," , c)
                else:
                    if(rand_num>699 and (stu-1)*36+700>rand_num):
                        num_ran = int(random.randint(1,stu))
                        print(nm1[num_ran-1] + "," , c)
                    else:
                        print("3성 상시 픽업," , c)
else:
    print("If it's pes, please press p.")
    pok=input()
    if(pok == "p"):
        print("Please enter the number of pick-up students entering the festival.")
        stu=int(input())
    else:
        print("Please enter the number of students for pick-up")
        stu=int(input())
    print("All differential probabilities are determined by the blue archive probability disclosure.")
    print("Please enter the student's name (main pick-up student is first)")
    if(pok=="p"):
        name=list(map(str,input().split()))
    else:
        nm1=list(map(str,input().split()))
    print("Please enter the number of times to draw. (If not entered, an error will occur.")
    gn= int(input())
    if(pok =="p"):
         for c in range (gn):
            rand_num = int(random.randint(0, 99999))
            if (rand_num <=5999):
                if(rand_num<=699):
                    print(name[0] + "," , c)
                else:
                    if(rand_num>699 and (stu-1)*300+700>rand_num):
                        num_ran = int(random.randint(1,stu))
                        print(name[num_ran] + "," , c)
                    else:
                        print("3-star always pick-up, " , c)
    else:
         for c in range (gn):
            rand_num = int(random.randint(0, 99999))
            if (rand_num <=2999):
                if(rand_num<=699):
                    print(nm1[0] + "," ,c)
                else:
                    if(rand_num>699 and (stu-1)*36+700>rand_num):
                        num_ran = int(random.randint(1,stu))
                        print(nm1[num_ran] + "," , c)
                    else:
                        print("3-star always pick-up," , c)
