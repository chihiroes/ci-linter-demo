import  sys,os,math
from collections import  defaultdict,Counter

def   calculate_total_price(  items, tax_rate=0.08,discount=0  ):
    '''这个函数计算总价格，包括税费和折扣，但是参数列表有很多空格，而且行很长'''
    subtotal = sum(  item['price'] * item['quantity']   for item in items  )
    discount_amount = subtotal * discount
    taxable_amount = subtotal - discount_amount
    tax_amount = taxable_amount * tax_rate
    total = taxable_amount + tax_amount
    return   total

class   ShoppingCart:
    def __init__(   self   ):
        self.items =   []
        self.customer_name =   ""
    
    def add_item( self, name, price, quantity=1 ):
        '''添加商品到购物车，这个方法的参数格式不对'''
        self.items.append( { 'name':name,'price':price,'quantity':quantity } )
    
    def   print_receipt( self ):
        '''打印收据，这个方法有很多格式问题'''
        print("="*50)
        print(f"顾客: {self.customer_name}")
        print("="*50)
        total_price = calculate_total_price(self.items)
        
        for   i   in   range(  len( self.items ) ):
            item = self.items[i]
            line = f"{i+1}. {item['name']} - ${item['price']} x {item['quantity']} = ${item['price'] * item['quantity']}"
            print(  line  )
        
        print( "-" * 50 )
        print( f"总计: ${total_price:.2f}" )

def  main(  ):
    cart = ShoppingCart(  )
    cart.customer_name = "张三"
    
    # 这一行故意写得很长，超过了79字符的限制
    cart.add_item("Python编程从入门到实践（第2版）超级豪华典藏版", 99.99, 2)
    cart.add_item("笔记本电脑支架", 25.50, 1)
    cart.add_item("USB-C数据线高速传输充电线", 15.75, 3)
    
    cart.print_receipt( )
    
    # 不必要的空格
    x =  5
    y  =  10
    z  =  x  +  y
    
    # 过长的行
    result = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) if x > 0 and y > 0 else 0
    
    print(f"计算结果: {result}")
    
    # 导入多个模块写在一行，操作符周围空格不一致
    a=1
    b=2
    c=a+b
    d=a-b
    e=a*b
    
    # 字典和列表中的空格不一致
    my_dict = {  'a':1, 'b' :2, 'c' : 3 }
    my_list = [ 1,2,3,4,5 ]

if  __name__  ==  "__main__"  :
    main( )
