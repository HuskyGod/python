from pathlib import *
import fnmatch
import fileinput
import sys
import linecache
import random
import os
# pp = PurePath('class.py')
# print(pp)
# pp = PurePath('crazyit', 'some/path', 'info')
# print(pp)
# pp = PurePath(Path('crazyit'), Path('info'))
# print(pp)
# pp = PurePosixPath('crazyit', 'some/path', 'info')
# print(pp)
# pp = PurePath()
# print(pp)
# pp = PurePosixPath('/etc', '/usr', 'lib64')
# print(pp)
# pp = PureWindowsPath('c:/window', 'd:info')
# print(pp)
# pp = PurePath('foo//bar')
# print(pp)
# pp = PurePath('foo/./bar')
# print(pp)
# pp = PurePath('foo/../ber')
# print(pp)
#
# p = Path('.')
# for x in p.iterdir():
#     print(x)

# p = Path('../')
# for x in p.glob('**/*.py'):
#     print(x)

# p = Path('g:/publish/codes')
# for x in p.glob('**/Path_text1.py'):
#     print(x)

# p = Path('test.txt')
# result = p.write_text('111111111111112222222222222222fffffffffffff')
# print(result)
# content = p.read_text(encoding='GBK')
# print(content)
# bb = p.read_bytes()
# print(bb)

# for file in Path('.').iterdir():
#     if fnmatch.fnmatch(file, '*num.py'):
#         print(file)

# names = ['a.py', 'b.py', 'c.py']
#
# sub = fnmatch.filter(names, '[ac].py')
# print(sub)
# f = open('test.txt')
# print(f.encoding)
# print(f.mode)
# print(f.closed)
# print(f.name)

# f = open('test.txt', 'r', True)
# while True:
#     ch = f.read(1)
#     if not  ch:break
#     print(ch, end='')
# f.close()

# f = open('test.txt', 'rb', True)
# print(f.read().decode('utf-8'))
# f.close()
#
# f = open('test.txt', 'r', True, 'utf-8')
# while True:
#     ch = f.read(1)
#     if not ch:break
#     print(ch, end='')
# f.close()

# f = open('test.txt', 'r', True, 'utf-8')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line, end='')
# f.close()

# for line in fileinput.input(files=('test.txt', '2.txt')):
#     print(fileinput.filename(), fileinput.filelineno(), line, end = '\n')
# fileinput.close()

# for line in sys.stdin:
#     print('用户输入：', line, end = '')

# text = sys.stdin.read()
# print(text)

# with open('test.txt', 'r', True, 'utf-8') as f:
#     for line in f:
#         print(line, end = '')

# class FkResource:
#     def __init__(self, tag):
#         self.tag = tag
#         print('构造器，初始化资源: %s' % tag)
#     def __enter__(self):
#         print('【——enter--%s】：' % self.tag)
#         return 'fkit'
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('【——exit--%s】：' % self.tag)
#         if exc_tb is None:
#             print('木有异常时关闭资源')
#         else:
#             print('遇到异常时关闭资源')
#             return  False
#
# with FkResource('孙悟空') as dr:
#     print(dr)
#     print('[with代码块] 没有异常')
# print('----------------------------------')
# with FkResource('白骨精'):
#     print('[with代码块] 异常之前的代码块')
#     raise Exception
#     print('[with代码块] 异常之后的代码块')

# print(linecache.getline(random.__file__, 3))
# print(linecache.getline('test.txt', 2))
# print(linecache.getline('test.txt', 3))

# f = open('x.txt', 'w+')
# f.write('我爱ptyhon' + os.linesep)
# f.writelines(('土门' + os.linesep,
#               '几元' + os.linesep,
#               '城下' + os.linesep,
#               '狂' + os.linesep))

# f = open('y.txt', 'wb+')
# f.write(('我爱python' + os.linesep).encode('utf-8'))
# f.writelines((('土门' + os.linesep).encode('utf-8'),
#               ('几元' + os.linesep).encode('utf-8'),
#               ('城下' + os.linesep).encode('utf-8'),
#               ('狂' + os.linesep).encode('utf-8')))

# f = open('y.txt', 'a+')
# f.write(('我爱python' + os.linesep))
# f.writelines((('土门' + os.linesep),
#               ('几元' + os.linesep),
#               ('城下' + os.linesep),
#               ('狂' + os.linesep)))

# print(os.getcwd())
# os.chdir('../python')
# print(os.getcwd())

