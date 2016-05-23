import urllib
import urllib.request
from post_class import Post
"""Note: May need to change post class split configs"""
"""MAKE SURE YOU HAVE NO PASSWORD PROTECTION ON THE LINK YOU USE BELOW"""
url_original = "http://kmoto.tumblr.com"
"""NAME OF BACKUP FILE"""
file_name = "iAmAlex"
"""NUMBER OF TOTAL BLOG PAGES"""
limit = 33
"""THE BELOW VARIABLEs SHOULD BE THE NAME OF THE DIV CLASS THAT CONTAINS AN INDIVIDUAL POST, THE CLASS THAT CONTAINS A TITLE,
AND THE CLASS THAT CONTAINS A BODY PARAGRAPH"""
div_class_post = "<div class=\"shadow\">"
div_class_post_end = "</div>"
div_class_title = "<h2>"
div_class_title_end = "</h2>"
div_class_body = "<div class=\"textpostbody\">"
div_class_body_end = "</div>"

"""IGNORE EVERYTHING BELOW"""
Post.div_class_post = div_class_post
Post.div_class_post_end = div_class_post_end
Post.div_class_title = div_class_title
Post.div_class_title_end = div_class_title_end
Post.div_class_body = div_class_body
Post.div_class_body_end = div_class_body_end

open_file = open(file_name+'.txt', 'w')
url = url_original + "/page/1"
i = 1
f = urllib.request.urlopen(url)
page = f.read().decode("utf-8")
post_list = []
while div_class_post in page and i <= limit:
	page = page.split(div_class_post)
	page = page[1:]
	for entry in page:
		s1 = entry.find(div_class_title)
		if s1 == -1:
			e1 = -1
		else:
			e1 = entry.find(div_class_title_end)
		s2 = entry.find(div_class_body)
		if s2 == -1:
			e2 = -1
		else:
			e2 = entry.find(div_class_body_end)
		if s2 != -1:
			head = ''
			if s1 != -1:
				head = entry[s1+1:e1]
			b = entry[s2+1:e2]
			p = Post(b,head)
			post_list.append(p)
	for entry_post in post_list:
		open_file.write(entry_post.returnText())
	i += 1
	f = urllib.request.urlopen(url_original + "/page/" + str(i))
	page = f.read().decode("utf-8")
	post_list = []
