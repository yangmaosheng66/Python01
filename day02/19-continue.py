# 有五个苹果
# 1. 吃了三个苹果之后, 吃饱了.后续的苹果不吃了
# 2. 吃了三个苹果之后.在吃第四个苹果,发现了半条虫子,这个苹果不吃了,还要吃剩下的苹果

for i in range(1, 6):
    if i == 4:
        print('发现半条虫子,这个苹果不吃了, 没吃饱,继续吃剩下的')
        continue  # 会结束本次循环,继续下一次循环

    print(f'吃了编号为{i}的苹果')