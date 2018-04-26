courses = ['History' , 'Comp_Sci', 'Math', 'Physics']
courses_2 = ['Art', 'Education']
nums = [1,5,4,3]
#courses.insert(0,courses_2)
#courses.extend(courses_2)
#courses.append(courses_2)
#courses.remove('Math')
#popped = courses.pop()
#courses.reverse()
#courses.sort()
#nums.sort()
#nums.sort(reverse=True)
#sorted_courses = sorted(courses)

#print(popped)
#print(sorted_courses)
#print(min(nums))
#print(max(nums))
#print(courses.index('Comp_Sci'))
#print ('Math' in courses)
#for item in courses:
	#print(item)
#for index, course in enumerate(courses, start=1):
#	print(index,course)

course_str = ' - '.join(courses)
#print(course_str)
new_list = course_str.split(' -')
print(new_list)