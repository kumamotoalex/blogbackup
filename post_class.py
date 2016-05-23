"""NOTE: May need to rearrange based upon html configs"""
class Post:
	div_class_post = "<div class=\"shadow\">"
	div_class_post_end = "</div>"
	div_class_title = "<h2>"
	div_class_title_end = "</h2>"
	div_class_body = "<div class=\"textpostbody\">"
	div_class_body_end = "</div>"
	def __init__(self, body, header):
		body = body.replace('<p>','\n').replace('</p>', '').replace('&rsquo;', "'").replace("&nbsp;", " ").replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&hellip;", "...").replace("<span>", '')
		body = body.replace('<p class="MsoNormal">','').replace('<em>', '').replace('&mdash;', '-').replace("<br>", '\n')
		try:
			header = header.split('<')[1].split('>')[1].replace('&rsquo;', "'").replace("&nbsp;", " ").replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&hellip;", "...").replace("<span>", '').replace('<p class="MsoNormal">','').replace('<em>', '').replace('&mdash;', '-')
		except IndexError:
			header = ''
		body_char_to_slice = body.find('>')
		body = body[body_char_to_slice:]
		self.body = body
		self.header = header
	def returnText(self):
		result = "----------------------------------------\n\n" + self.header + '\n\n' + self.body + '\n\n'
		return result