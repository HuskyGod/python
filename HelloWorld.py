# 这是单行注释
print("Hello world")
'''
我是多行注释
我是多行注释
'''
s = "12345678910";
print(s[2])
print(s[:5])
print(s[2:])
print(s[2:5])
print(s[-2])

a = "out admin"

print(a.title())
print(a.lower())
print(a.upper())

my_list = ['chrazyit', 20, 'python'];
print(my_list);

my_tuple = ('chrazyit', 20, 'python')
print(my_tuple);

vlas = 10, 20, 30, 40

a, b, c, d = vlas;
print(a, b, c, d);

a, b, c, d = 100, 50, 60, 480;
print(a, b, c, d);

a, b, *rest = 100, 50, 60, 480;
print(a, b, rest);

list = list(range(10));
print(list);

a_list = ['crazyit', 20, -1.2];
a_tuple = tuple(a_list);

print(a_tuple)

b_range = range(1, 5);
b_tuple = tuple(b_range);

print(b_tuple);

c_tuple = [1, 2, 3];
print(c_tuple);
c_tuple.append([1, 2]);
print(c_tuple);
c_tuple.append((1, 2, 3));
print(c_tuple);
c_tuple.extend([2, 3, 4]);
print(c_tuple);
del c_tuple[1: 2]
print(c_tuple);
# del c_tuple;
# print(c_tuple);

c_list = [1, 2, 3, 40, 20, 30];
print(c_list);
c_list.remove(1);
print(c_list);
c_list.remove(40);
print(c_list);
c_list.clear();
print(c_list);

