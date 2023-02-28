from TexSoup import TexSoup

with open('latex.tex', 'r') as file:
    text = file.read()


text = fr"{text}"

text = text.replace('$', '')
text = text.replace('$\Pi$', '')
text = text.replace("{p{9cm}}", "")
text = text.replace(r"\\", "")
text = text.replace(r"*", " ")
# text = text.replace(r"\n", "")

soup = TexSoup(
    text
)

soup = soup.document




#site title
# title = soup.find("document").find("flushright").find("tabular")[2]
# print(title)





# head = soup.find("document").find_all("center")[1].find("tabular").text
head = soup.find_all("center")[1].tabular.text


keywords_index = head.index("Kalit so'zlar:")
keywords = head[keywords_index:keywords_index+2]



i = 2
while True:
    if head[i] == '[':
        nat = i
        break
    i+=1


title = head[2:keywords_index]






if __name__ == "__main__":
    print("Dastur ishga tushirildi")