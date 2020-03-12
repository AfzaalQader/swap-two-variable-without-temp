# User has an account on stackoverflow:

# = User has posted 5 questions
# = User has posted 15 answers
# = Question 1 got 5 downvotes, and 2 upvotes
# = Question 2 got 0 downvote, and 10 upvote
# = Answer 1 accepted
# = Answer 2 accepted and 10 upvote
# = Answer 3 not accepted and got 3 upvote and 2 downvote


# 1 Upvote = 10 points
# 1 downvote = -2 points
# 1 acceptedd answer = 15 points

def question_voting(number_of_upvote,number_of_downvote):
	point_per_upvote = 10
	point_per_downvote = -2
	total_point_of_question =  number_of_upvote * point_per_upvote + number_of_downvote * point_per_downvote
	return total_point_of_question

def answer_voting(number_of_upvote,number_of_downvote,number_of_accepted_answer):
	point_per_upvote = 10
	point_per_downvote = -2
	point_per_accepted_answer = 15
	total_point_of_question =  number_of_upvote * point_per_upvote + number_of_downvote * point_per_downvote + number_of_accepted_answer * point_per_accepted_answer
	return total_point_of_question


total_points = question_voting(2,5) + question_voting(10,0) + answer_voting(0,0,1) + answer_voting(10,0,1) + answer_voting(3,2,0)
print("Total vote of the user is {} ".format(total_points))
