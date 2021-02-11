import enum
class checkEnum (enum.Enum):
    EAST = "东边"
    WEST = "西边"
    SOUTH = "南边"
    NORTH = "北边"
    def info (self) :
        print('这是一个代表放心[%s]的枚举' % self.value)

print(checkEnum.SOUTH)
print(checkEnum.SOUTH.value)
print(checkEnum['WEST'])
print(checkEnum('南边'))
print(checkEnum.NORTH.info())
print(checkEnum.__members__)