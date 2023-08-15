"""Let g(n) is a function to calculate the  total number of ways of attending classes over N days 
 so they can eligible for attending the graduation ceremony.

 once the student absent 4 or more then 4 consecutive day then he will be not will be not eligible for attending the graduation ceremony so we can take the base condition for consecutive day of absend from 0 to 3

f(n-1-0)=number of ways to attend class in the first n with no consecutive absend,d=0
f(n-1-1)=number of ways to attend class in the first n with 1 consecutive absend,d=1
f(n-1-2)=number of ways to attend class in the first n with 2 consecutive absend,d=2
f(n-1-3)=number of ways to attend class in the first n with 3 consecutive absend,d=3

g(n)=f(n-1,0)+f(n-1,1,)+f(n-1,2)+f(n-1,3)

f(n-1,1)-->f(n-2,0)
f(n-1,2)-->f(n-2,1)-->f(n-3,0)
f(n-1,3)-->f(n-2,2)-->f(n-3,1)-->f(n-4,0)

To calculate the total number of ways of attending classes so student can  can eligible for attending the graduation ceremony.
I've derived to get a linear equation like this by using the above method.


#To calculate the The probability that so that student will miss your graduation ceremony on day n.

Let k(n) is a function to calculate the  total number of ways of attending classes over N days so student can eligible for attending the graduation ceremony but they will miss the graduation.

To calculate the The probability that so that student will miss your graduation ceremony.

student will miss the graduation ceremony they You don't attend class on day n

i have derived this liner eqaution student did attend class on day n

k(n)=f(n-1,1,)+f(n-1,2)+f(n-1,3)

"""






def graduation_ceremony(n):


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


	#for n num of day i have to run this equation from 4 to till n so I  run this for loop from 4 to n+1


	for i in range(4,n+1):
			dict_E_attend_ceremony[i]=dict_E_attend_ceremony[i-1-0]+dict_E_attend_ceremony[i-1-1]+dict_E_attend_ceremony[i-1-2]+dict_E_attend_ceremony[i-1-3]
			if i>4:
				# deleting unused memory to save from memory leakage
				del dict_E_attend_ceremony[i-5]

	#1..The number of ways to attend classes over N days

	number_of_ways_to_attend_classes_over_N_days=dict_E_attend_ceremony[n]

	#To calculate the The probability that so that student will miss your graduation ceremony on day n.			
   
	dict_Miss_g_ceremony[n]=dict_E_attend_ceremony[n-1-1]+dict_E_attend_ceremony[n-1-2]+dict_E_attend_ceremony[n-1-3]

	#2..number of ways so the student can miss the gradu_ceremony

	number_of_ways_so_the_student_can_miss_the_gradu_ceremony=dict_Miss_g_ceremony[n]
			
	result =	f"{number_of_ways_so_the_student_can_miss_the_gradu_ceremony}/{number_of_ways_to_attend_classes_over_N_days}"
	#sentence =	"".format({number_of_ways_of_attending_classes_over_N_days(n)} + '/' + {absence_on_graduation(n)})
	return result
	

print(graduation_ceremony(5))
print(graduation_ceremony(10))
