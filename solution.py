class Graduation:
	def __init__(self, days):
		self.n=days
	def graduation_ceremony(self):
		n=self.n
		if isinstance(n, (int)) and n>0:

			#i created one empty dictonary to store the  value of Total_way_to_attend_class_so_stu_will_eligible_for_graduation_ceremony -->
			#dict_E_attend_ceremony['n':num_of_way_to_addent_the class]
			#g(0)=1
			#g(1)=2
			#g(2)=4
			#g(3)=8

			dict_E_attend_ceremony={}
			dict_E_attend_ceremony[0]=1
			dict_E_attend_ceremony[1]=2
			dict_E_attend_ceremony[2]=4
			dict_E_attend_ceremony[3]=8

			if n>=4:
				#for n num of day i have to run this equation from 4 to till n so I  run this for loop from 4 to n+1
				for i in range(4,n+1):
					dict_E_attend_ceremony[i]=dict_E_attend_ceremony[i-1-0]+dict_E_attend_ceremony[i-1-1]+dict_E_attend_ceremony[i-1-2]+dict_E_attend_ceremony[i-1-3]
					if i>5:
						# dleakageeleting unused memory to save from memory 
						del dict_E_attend_ceremony[i-5]

			#1..The number of ways to attend classes over N days			
			number_of_ways_to_attend_classes_over_N_days=dict_E_attend_ceremony[n]

			#2..number of ways so the student can miss the gradu_ceremony
			    #To calculate the The probability that so that student will miss your graduation ceremony on day n.	
				#i created one empty dictonary to store the value of Total_way_to_attend_class_so_stu_will_miss_the_graduation_ceromany -->
			    #dict_E_attend_ceremony['n':num_of_way_to_addent_the class]

			#put the base condtion like this
		    #k(1)=1
		    #k(2)=2
		    #k(3)=4
			
			dict_Miss_g_ceremony={}
			dict_Miss_g_ceremony[1]=1
			dict_Miss_g_ceremony[2]=2
			dict_Miss_g_ceremony[3]=4

			if n>=4:
				dict_Miss_g_ceremony[n]=dict_E_attend_ceremony[n-1-1]+dict_E_attend_ceremony[n-1-2]+dict_E_attend_ceremony[n-1-3]

			number_of_ways_so_the_student_can_miss_the_gradu_ceremony=dict_Miss_g_ceremony[n]

			result =	f"{number_of_ways_so_the_student_can_miss_the_gradu_ceremony}/{number_of_ways_to_attend_classes_over_N_days}"

			return result
		else:
			return "number of day can not be less than 1 and and it should only integer"


			
Graduation_obj=Graduation(1)
Graduation_obj_1=Graduation(3)
Graduation_obj_2=Graduation(5)
Graduation_obj_3=Graduation(10)
Graduation_obj_4=Graduation(-1)
Graduation_obj_5=Graduation(4)
print(Graduation_obj_4.graduation_ceremony())

"""print(graduation_ceremony(1))	
print(graduation_ceremony(3))
print(graduation_ceremony(5))
print(graduation_ceremony(10))
print(graduation_ceremony(-1))
print(graduation_ceremony("kuchh bhi"))
print(Graduation_obj.graduation_ceremony())"""
				



			