import mdtex2html


with open("latex.tex", 'r') as file:
    latex = file.read()


a = mdtex2html.convert(latex)
print(a)