学习笔记
1. 对于链表的处理，多数情况下使用快慢指针
2. 处理链表问题，需要新建链表接收结果
3. 栈：先进后出，像弹夹装子弹一样。 队列：先进先出，像排队一样

优先队列：
区别于队列，优先队列在存入数据的时候设置了优先级，并且值越小，优先级越高。
priorityQueue 重载了 Queue 的put()和get()函数。
put():
queue中，put函数为往queue中直接添加元素。 priorityQueue使用heappush，将元素的优先级和元素加入queue中。
get():
queue使用popleft, priorityQueue使用heappop