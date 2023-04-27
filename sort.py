num = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", 
"K", "A"]
teir = ["♦", "♣", "♥", "♠"]
pai = {}
pnt = 0
for n in range(0, 13):
    for x in range(0, 4):
        pnt += 1
        pai[num[n] + teir[x]] = pnt



def insertionSort(lis, last):
    comp = 0
    for i in range(0, last):
        
        key = lis[i+1]
        j = i
        while j >= 0 and pai[key] < pai[lis[j]]:
            lis[j+1] = lis[j]
            j -= 1
            comp += 1
        lis[j+1] = key
        
        print(lis)
    return 'Comparison time: %d' %(comp + last - 1)

def selectionSort(lis, last):
    comp = 0
    for i in range(0, last):
        o_c = lis[i]
        smol = i
        wok  = i + 1
        for j in range(wok, last+1):
            if pai[lis[j]] < pai[lis[smol]]:
                smol = j
            comp+= 1
        
        lis[i] = lis[smol]
        lis[smol] = o_c
        print(lis)
        
    return 'Comparison time: %d' %(comp)

def bubbleSort(lis, last):
    comp = 0
    srted = False

    for cur in range(0, last):
        if srted == False:
            wok = last
            srted = True
            for i in range(wok, cur, -1):
                if pai[lis[i]] < pai[lis[i-1]]:
                    srted = False
                    o_w = lis[i]
                    lis[i] = lis[i-1]
                    lis[i-1] = o_w
                comp += 1
        print(lis)
    return 'Comparison time: %d' %(comp)



wow = (['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'])
# print(insertionSort(wow, 8))
# print(selectionSort(wow, 8))
print(bubbleSort(wow, 8))

# 4♣
# 10♥
# K♦
# 4♠
