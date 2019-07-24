import requests

def send_simple_message(email):
	response = requests.post(
		"https://api.mailgun.net/v3/sandbox76dd88d70f644273a7b3189a4ffcba1b.mailgun.org/messages",
		auth=("api", "25e1996be2f29d3789c0073f18b7159f-fd0269a6-85e17316"),
		data={"from": "Excited User <mailgun@sandbox76dd88d70f644273a7b3189a4ffcba1b.mailgun.org>",
			"to": email,
			"subject": "We are finding you a travel buddy",
			"text": "Thanks for signing up. We will match your holiday destination and preferences and find you someone to travel with. Thanks, the CarryOn Girls"})
        print(response)
        return response

send_simple_message();
