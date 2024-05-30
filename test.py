#打印商品列表
your_money = int(input("请输入您的预算："))
view_all = [('swatch',300),('Ps4',2000),('Iphone',7000),('MacBook',10000)]
shopping_cart = []
while True:
    print('ProductList'.center(45))
    print('=' * 45)
    print('{:15}{:^15}{:>15}'.format('Num', 'Name', 'Price'))
    print('-' * 45)
    for index,i in enumerate(view_all,1):
        print('{:<15}{:^15}{:>15,}\t'.format(index,i[0],i[1]))
    print('-' * 45)
#选择商品添加购物车并计算余额
    your_choose = input('请输入你的选择：')
    if your_choose.isdigit():
        your_choose = int(your_choose)
        if your_choose >=1 and your_choose <= len(view_all):
            if (your_money - view_all[your_choose-1][1]) >= 0:
                shopping_cart.append(view_all[your_choose-1])
                your_money -= view_all[your_choose-1][1]
                print('商品已添加购物车，您的余额为{:,}'.format(your_money))
            else:
                print('余额不足，添加失败')
        else:
            print('商品不存在')
    elif your_choose == 'q':
        break
    else:
        print('输入错误，请重新输入')

#打印出用户已添加的商品及余额
print('您的余额剩余：{:,}'.format(your_money))
print('您添加购物车商品：')
for x in shopping_cart:
    print(x[0]+',',x[1])
print('感谢您本次购买，欢迎下次光临！')