def initialize(s): #start the conversation between service and client
	resp = 'This is Health Help. Please text any symptoms of the current patient'
	return resp

def parse_message(s): #find keywords
	words = s.split()
	for word in words:
		if word == 'attempted suicide':
			attempted_suicide_dt()
		if word == 'shooting':
			shooting_dt()
