import threading
import time

# def action(max):
#     for i in range(max):
#         print(threading.current_thread().getName() + " " + str(i))
#
# for i in range(100):
#     print(threading.current_thread().getName() + "  " + str(i))
#     if (i == 20):
#         t1 = threading.Thread(target=action, args=(100,))
#         t1.start()
#         t2 = threading.Thread(target=action, args=(100,))
#         t2.start()
# print('主綫程完畢')

# class FkThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.i = 0
#     def run(self):
#         while self.i < 100:
#             print(threading.current_thread().getName() + "     " + str(self.i))
#             self.i += 1
#
# for i in range(100):
#     print(threading.current_thread().getName() + "   " + str(i))
#     if i == 20:
#         ft1 = FkThread()
#         ft1.start()
#         ft2 = FkThread()
#         ft2.start()
# print('主綫程完畢')

# def action (max):
#     for i in range(max):
#         print(threading.current_thread().name + " " + str(i))
# for i in range(30):
#     print(threading.current_thread().name + " " + str(i))
#     if i == 20:
#         threading.Thread(target=action, args=(10,)).run()
#         threading.Thread(target=action, args=(10,)).run()


# def action(max):
#     for i in range(max):
#         print(threading.current_thread().name + " " + str(i))
#
# threading.Thread(target=action, args=(100,), name="新线程").start()
# for i in range(100):
#     if i == 20:
#         jt = threading.Thread(target=action, args=(100,), name="被Join的线程")
#         jt.start()
#         jt.join()
#     print(threading.current_thread().name + "  " + str(i))

# def action(max):
#     for i in range(max):
#         print(threading.current_thread().name + "  " + str(i))
# t = threading.Thread(target=action, args=(100,), name="后台线程")
# t.daemon = True
# t.start()
# for i in range(10):
#     print(threading.current_thread().name + "  " + str(i))

# for i in range(10):
#     print("当前时间: %s" % time.ctime())
#     time.sleep(1)

# class Account:
#     def __init__(self, account_no, balance):
#         self.account_no = account_no
#         self._balance = balance
#         self.lock = threading.RLock()
#     def getBalance(self):
#         return self._balance
#     def draw(self, draw_amount):
#         self.lock.acquire()
#         try:
#             if self._balance >= draw_amount:
#                 print(threading.current_thread().name + "取钱成功! 吐出钞票: " + str(draw_amount))
#                 time.sleep(0.001)
#                 self._balance -= draw_amount
#                 print('余额:' + str(self._balance))
#             else:
#                 print(threading.current_thread().name + "取钱失败:余额不足")
#         finally:
#             self.lock.release()
#
# def draw (account, draw_amount):
#     account.draw(draw_amount)
#
# acct = Account('123456', 1000)
# threading.Thread(name="甲", target=draw, args=(acct, 800)).start()
# threading.Thread(name="已", target=draw, args=(acct, 800)).start()

# class Account:
#     def __init__(self, account_no, balance):
#         self.account_no = account_no
#         self._balance = balance
#         self.cond = threading.Condition()
#         self._flag = False
#
#     def getBalance(self):
#         return self._balance
#     def draw(self, draw_amount):
#         self.cond.acquire()
#         try:
#             if not self._flag:
#                 self.cond.wait()
#             else:
#                 print(threading.current_thread().name + "取錢:" + str(draw_amount))
#                 self._balance -= draw_amount
#                 print('账户余额为' + str(self._balance))
#                 self._flag = False
#                 self.cond.notify_all()
#         finally:
#             self.cond.release()
#     def deposit(self, deposit_amount):
#         self.cond.acquire()
#         try:
#             if self._flag:
#                 self.cond.wait()
#             else:
#                 print(threading.current_thread().name + "存款:" + str(deposit_amount))
#                 self._balance += deposit_amount
#                 print("账户余额:" + str(self._balance))
#                 self._flag = True
#                 self.cond.notify_all()
#         finally:
#             self.cond.release()
#
# def draw_many (account, draw_amount, max):
#     for i in range(max):
#         account.draw(draw_amount)
# def deposit_many(account, deopsit_amount, max):
#     for i in range(max):
#         account.deposit(deopsit_amount)
# acct = Account('1234567', 0)
# threading.Thread(name="取钱者", target=draw_many, args=(acct, 800, 100)).start()
# threading.Thread(name="存款者甲", target=deposit_many, args=(acct, 800, 100)).start()
# threading.Thread(name="存款者已", target=deposit_many, args=(acct, 800, 100)).start()
# threading.Thread(name="存款者丙", target=deposit_many, args=(acct, 800, 100)).start()