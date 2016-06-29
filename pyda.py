import wolframalpha
import wikipedia
import easygui
import base64
from secrets import APP_ID

class MyFrame():
	def __init__(self):
		self.decrypt_id = base64.b64decode(APP_ID)
		self.title = 'PyDa'
		self.message = 'What would you like to know?'
		self.input = easygui.enterbox(msg=self.message, title=self.title, strip=True)

	def onEnter(self,infinite):	
		if infinite == True:
			try:
				#wolframalpha
				client = wolframalpha.Client(self.decrypt_id)
				result = client.query((self.input).lower())
				answer = next(result.results).text
				easygui.msgbox("You asked me: " + str(self.input) + "\n\n" + "Here's what I found: \n\n" + answer, 'PyDa')
			except:
				#wikipedia
				new_input = self.input.split(" ")
				if new_input[0] == 'who' or new_input[0] == 'what' or new_input[0] == 'when' or new_input[0] == 'why' or new_input[0] == 'where':
					i = " ".join(new_input[2:])
				answer = wikipedia.summary(self.input)
				easygui.msgbox("You asked me: " + str(self.input) + "\n\n" + "Here's what I found: \n\n" + answer, 'PyDa')

if __name__ == '__main__':
	frame = MyFrame()
	frame.onEnter(True)

