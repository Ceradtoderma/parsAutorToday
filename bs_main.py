from parser import ParsAT



pars = ParsAT('https://author.today/reader/8776/42425', '123')
pars.get_text()

print(pars.text)