#keys = ['breathing difficulty', 'unconscious', 'heart problem', 'seizure', 'traumatic injury', 'stroke', 'hemmorrhage', 'overdose', 'poisoning', 'hypoglycemia', 'hyperglycemia', 'cardiac arrest', 'base pain', 'allergic reaction', 'pregnancy', 'headache', 'laceration', 'choking', 'hyperthermia', 'hypothermia', 'shooting', 'stabbing', 'burns']

def parse_message(s): #find keywords
	words = s.split()
	for word in words:
		if word == 'burns':
			return burns_dt()
		if word == 'choking':
			return choking_dt()
		if word == 'headache':
			return headache_dt()
		if word == 'heart':
			return heart_problem_dt()
		if word == 'hemorrhage':
			return hemorrhage_dt()
		if word == 'hyperthermia':
			return hyperthermia_dt()
		if word == 'hyperglycemia':
			return hypohyperglycemia_dt()
		if word == 'hypoglycemia':
			return hypohyperglycemia_dt()
		if word == 'hypothermia':
			return hypothermia_dt()
		if word == 'laceration':
			return laceration_dt()
		if word == 'overdose':
			return overdose_dt()
		if word == 'poisoning':
			return poisoning_dt()
		if word == 'pregnancy':
			return pregnancy_dt()
		if word == 'seizure':
			return seizure_dt()
		if word == 'shooting':
			return shooting_dt()
		if word == 'stabbing':
			return stabbing_dt()
		if word == 'unconscious':
			return unconscious_dt()
	return "error 1738"

def burns_dt():
    return "\n\n1. Stop burning\n2. Remove constrictive clothing\n3. For first-degree burns, cool burn, protect burn with sterile gauze or cloth, and then treat burn."
def choking_dt():
    return "\n\n1. If the person can cough, tell them to continue coughing. \n2. If no response is received, give 5 back blows. \n3. Provide 5 abdominal thrusts via the Heimlich maneuver. \n4. Alternate between these blows and thrusts until choking stops."
def headache_dt():
    return "\n\n1. Supply pain medication."
def heart_problem_dt():
	return "\n\n1. Have the person sit and relax\n2. Loosen tight clothing\n3. Give medicine if heart condition is known\n4. If individual is unconscious, begin CPR."
def hemorrhage_dt():
	return "\n\n1. Remove any clothing or debris on the wound\n2. Stop the bleeding with a sterile bandage or clean cloth\n3. Apply pressure to do so\n4. Help the injured person lie down and immobilize the injured body part if possible."
def hyperthermia_dt():
    return "\n\n1. Move the individual to cool area with adequate ventilation. \n2. Remove unnecessary clothing. \n3. Apply ice packs. \n4. Have the individual drink water slowly if possible."
def hypohyperglycemia_dt():
    return "\n\n1. If unconscious, roll the individual on their side and attempt to call for medical attention. \n2. If conscious, attempt to give the patient some sugar if hypoglycemic. \n3. If conscious and  hyperglycemic, supply insulin."
def hypothermia_dt():
    return "\n\n1. Get the person indoors. \n2.Dry the person off if needed. \n3.Warm the individual's torso first. \n4.Do not immerse them in warm water. \n5. Begin CPR if necessary."
def laceration_dt():
    return "\n\n1. Stop the bleeding. \n2. Clean the wound and cover with a sterile bandage."
def overdose_dt():
	return "\n\n1. If the individual is unconscious, place them on their side.\n2. Identify the drug taken\n3. If overheating is noticed, remove unnecessary clothing to assist with cooling skin."
def poisoning_dt():
	return "\n\n1. For swallowed poison, remove poison in mouth.\n2. If poison is on skin, remove contaminated clothing and rinse skin.\n3. For poison in the eye, flush the eye with water.\n4. If poison is inhaled, get the person into fresh air."
def pregnancy_dt():
    return "\n\n1. Get the individual on their back\n2. Tell the individual to breathe\n3. If contractions are less than two minutes, birth is imminent\n4. Ensure that as the baby comes out, you do not pull on the baby and that you do not drop the baby."
def seizure_dt():
	return "\n\n1. Stay with the person until the seizure has ended\n2. Communicate the situation to the individual once they are alert\n3. Comfort the individual\n4. Check to see if the individual is wearing any emergency information."
def shooting_dt():
	return "\n\n1. Treat both entry and exit wounds\n2. Elevate the wound\n3. Apply direct pressure and immobilize the affected limb\n4. Cover the wound with sterile gauze or clothing."
def stabbing_dt():
    return "\n\n1. Lie the victim down. Remove clothing around the wound.\n2. Stop the bleeding by applying pressure with sterile gauze or clothing.\n3. If the knife is in the wound, do not remove it.\n4. Clean the wound if possible."
def stroke_dt():
	return "\n\n1. Lay the individual on their side\n2. If the individual is not breathing, perform CPR\n3. Cover them with a blanket\n4. Do not give them anything to eat or drink."
def unconscious_dt():
	return "\n\n1. Roll them into a comfortable position\n2. Apply CPR."	