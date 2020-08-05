# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



def SGtoAPI(SG_API):
	SG_1 = SG_API
	API = 141.5/SG_1 - 131.5

	return API


def SGtoBaume(SG_Baume):
	SG_2 = SG_Baume
	if SG_2 <= 1:
		Baume = 141.5/SG_2 - 131.5
	else:
		Baume = 145 - 145/SG_2

	return Baume
