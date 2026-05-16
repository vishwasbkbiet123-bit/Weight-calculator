course = 'course for beginners'
print(course)
course = "course for beginner's"
print(course)
course = '''course for beginners'''
print(course)
course = """course for beginners"""
print(course)


#indexing 
name = "my name is vishwas"
print(name[::])
print(name[0:])
print(name[0:7])
print(name[4:7])
print(name[-1])
print(name[-2])


# formatted string
#to print vishwas [saini] is a coder
first = "vishwas"
last = "saini"
massag = f'{first} [{last}] is a coder'
print(massag)

#String methods
course = "Python for beginners"
print(len(course))
 
print(course.upper())
print(course.capitalize())
print(course.find("for"))
print(course.replace("beginners", "absoute beginners"))
print(course.lower())

