
list = [[7,8,9],[4,5,6],[1,2,3]]


def draw():
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if (list[i][j] == 'X' or list[i][j] == 'O'):
                continue
            else:
                return
    print(f"The game is a draw")
    print(f"\t")
    start()


def matrix(n,i,s):

  list[n][i] = s
  for num in range(0, len(list)):
     print(list[num][0], '|', list[num][1], '|', list[num][2])
     if num == 2:
         break
     print("-" * 10)
  print(f"\t")


def calc(v1,v2,s1,s2):
    a = int(input(f"player {v1} choose the number where u want to enter the symbol: "))

    for num in range(0,len(list)):
        for in_num in range(0,3):
          if list[num][in_num] == a:
              matrix(num,in_num,s1)
              break
          else:
             continue

    check1(v1,s1)
    draw()


    b = int(input(f"player {v2} choose the number where u want to enter the symbol: "))


    for num in range(0,len(list)):
            for in_num in range(0,3):
             if list[num][in_num] == b:
              matrix(num,in_num,s2)
              break
             else:
                 continue

    check2(v2,s2)
    draw()

    calc(v1,v2,s1,s2)


def check1(v1,s1):
             for num in range(0, len(list)):
              if (list[num][0] == list[num][1] == list[num][2] == s1) or (
                    list[0][num] == list[1][num] == list[2][num] == s1) or (
                    list[0][0] == list[1][1] == list[2][2] == s1) or (list[0][2] == list[1][1] == list[2][0] == s1):
                print(f"player {v1} wins")

                print(f"\t")
                start()
                break



def check2(v2, s2):

           for num in range(0, len(list)):
            if(list[num][0] == list[num][1] == list[num][2] == s2) or (
                     list[0][num] == list[1][num] == list[2][num] == s2) or (
                    list[0][0] == list[1][1] == list[2][2] == s2) or (list[0][2] == list[1][1] == list[2][0] == s2):
              print(f"player {v2} wins")
              print(f"\t")
              start()
              break



def symbol(v1 , v2):
    l = 'XO'
    s1 = input(f"player {v1} , choose from 'X' or 'O': ")
    if s1== l[0]:
       s2 = l[1]
    elif s1 == l[1]:
       s2 = l[0]
    else:
       print("WRONG SYMBOL!!")
       return


    for num in range(0,len(list)):
        print(list[num][0],'|',list[num][1],'|',list[num][2])
        if num == 2:
           break
        print("-"*10)
    print(f"\t")


    calc(v1,v2,s1,s2)



def player():
    value = int(input("player 1 or player 2: "))
    if  value ==1:
       v1 = value
       v2 = 2
    else:
       v1 = value
       v2 = 1

    symbol(v1,v2)



def start():

    ans = input("Do you want to play(yes/no): ")
    k=1
    if ans.lower() == 'yes':
        for i in range(0,3):
            for j in range(0,3):
                list[i][j]=k
                k += 1
        player()

    elif ans == 'no':
        exit(0)
    else:
        print(f'Answer in yes/no')
        start()


start()


