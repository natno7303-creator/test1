print("hellow world")

print("1+2")

print(1+2)

print("1 + 2 =",1+2)

message=("zcc")
print(message)

age=22
print(message,age)

next_age=age + 1
print(next_age)

age=age+1
print(age)

#列表（List）操作
fruits=["苹果","香蕉"]
print(fruits[1])

fruits.append("西瓜")
print(fruits)

#元组，元组创建后不能修改元素，否则会报 TypeError
point=(10,20)
print(point[0])   #point[0]=30  元组不能修改

#字典， 字典是可变、无序（但3.7+保留插入顺序）的键值对集合。
user = {"name1":"zcc","age1":22}
print(user["name1"])
user["age1"]=19
user["Gender"]="xiaozhang"
print(user)

#集合，集合自动去重，元素必须可哈希（不可变）。
number={1,2,2,3,3}
print(len(number))
number.add(4)
print(len(number))
number.add(2)  #2已经存在
print(len(number))

#列表索引与切片
numbers=[1,2,3,4,5]
print(numbers[0])
print(numbers[-1])
print(numbers[0:4])  #第0个位置开始至第4个位置前

#算1，2，3，4，5的平方，2种写法
squares=[x*x for x in range(1,6)]
print(squares)

squares = []
for x in range(1, 6):
    squares.append(x*x)

#字典的get与update方法
userz={"name":"zcc","age":22,"Gender":"zhangchenhao"}
print(userz)
print(userz.get("level","无"))
userz.update({"age":23,"level":"入门"})
print(userz)
print(userz.get("level","无"))
print(userz.items())