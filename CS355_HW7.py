import random

def SimulateTrial(trials):

	GoodSwap = 0
	BadSwap = 0
	DidntSwap_GoodChoice = 0
	DidntSwap_BadChoice = 0
	for i in range(trials):
		envelope_A = random.randint(1, 10)
		#print(envelope_A)
		envelope_B = random.randint(1, 10)
		#print(envelope_B)
		#establish money in the envelopes
		chosen_env = []
		not_chosen = []

		X = .5
		initial_coin = random.randint(0,1)

		flip_counter = 0
		if initial_coin == 0:
			chosen_env.append(envelope_A)
			not_chosen.append(envelope_B)
		elif initial_coin == 1:
			chosen_env.append(envelope_B)
			not_chosen.append(envelope_A)
		# 0 is heads, 1 is tails
		while True:
			flip = random.randint(0,1)
			flip_counter += 1
			if flip == 1 :
				continue
			elif flip == 0:
				break

		X = X + flip_counter
		if X > chosen_env[0]:
			#we swap envelopes
			if chosen_env[0] < not_chosen[0]:
				GoodSwap += 1
			elif chosen_env[0] > not_chosen[0]:
				BadSwap += 1
		elif X < chosen_env[0]:
			if chosen_env[0] < not_chosen[0]:
				DidntSwap_GoodChoice += 1
			elif chosen_env[0] > not_chosen[0]:
				DidntSwap_BadChoice += 1

	print("Number of good swaps ( swapping produced higher value):", GoodSwap)
	print("Number of bad swaps (swapping produced lower value):", BadSwap)
	print("Higher value without swapping:", DidntSwap_GoodChoice)
	print("Lower value without swapping:", DidntSwap_BadChoice)
	return

SimulateTrial(1000)
