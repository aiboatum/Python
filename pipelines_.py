"""
    coroutiners can be used to implement data pipelines where one coroutine
    will send data to the next conroutine in the pipeline .
    cotoutines push data into the pipeline using the send() method.

    there is an example of a small pipeline where the values sent to the
    producer coroutine are squared and sent to the consumer coroutine for
    print.
"""
def producer(consumer):
    print("Producer ready")
    while True:
        val=yield
        consumer.send(val**2)
def consumer():
    print("Consumer ready")
    while  True:
        val=yield
        print("Consumer got",val)

# cons=consumer()
# prod=producer(cons)
# next(prod)
# next(cons)
# prod.send(10)
"""
    Also,with coroutines,data can be sent to multiple destinations.The 
    following example implements two consumers where the first only
    prints numbers in 0..10 and the  second only print numbers in 10.20
"""
def producer_1(consumers):
    print("producer ready")
    try :
        while True:
            val=yield
            for consumer in consumers:
                consumer.send(val**2)
    except GeneratorExit:
        #when a generator or coroutine is closed
        for consumer in consumers:
            consumer.close()

def consumer_1(name,low,high):
    print("%s ready "%(name))
    try:
        while True:
            val=yield
            if low<val<high:
                print('%s got '%(name),val)
    except GeneratorExit:
        print("%s closed"%(name))

# con1=consumer_1("consumer 1",00,10)
# con2=consumer_1("consumer 2",10,20)
# prod=producer_1([con1,con2])
# next(prod)
# next(con1)
# next(con2)
# prod.send(1)
# prod.send(2)
# prod.send(3)
# prod.send(4)
# prod.close

def producer_2(consumers):
    try:
        while True:
            val=yield
            for consumer in consumers:
                consumer.send(val**2)
    except GeneratorExit:
        for consumer in consumers:
            consumer.close()

def consumer_2():
    try:
        min=yield
        min=int(min)
        while True:
            val=yield
            if int(val)<min:
                min=int(val)
            print("the min is %d so far"%min)
    except GeneratorExit:
        pass
def consumer_3():
    try:
        max=yield
        max=int(max)
        while True:
            val=yield
            if int(val)>max:
                max=int(val)
            print("the max is %d so far"%max)
    except GeneratorExit:
        pass 

con2_=consumer_2()
con2__=consumer_3()
prod_2=producer_2([con2_,con2__])
next(prod_2)
next(con2_)
next(con2__)
for i in range(4):
    prod_2.send(int(i))
