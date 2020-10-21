from random import randint
import codecs
import time
compteur = False
def traitement(mot):
	liste = []
	for x in range(1, len(mot)-1):
		liste.append(mot[x])
	res = mot
	while res == mot:
		alea = []
		cp_liste = liste.copy()
		n = None
		for x in range(0, len(cp_liste)):
			n = randint(0, len(cp_liste)-1)
			alea.append(cp_liste[n])
			cp_liste.remove(cp_liste[n])
		alea = ''.join(alea)
		res = mot[0]+alea+mot[-1]
	return res
sortie = []
i = 0
print(f"Traitement en cours...")
try:
	if compteur:
		print("")
	fichier = codecs.open("input.txt", "r", "utf-8")
	texte = fichier.read()
	texte2 = texte
	lignes = texte.split("\n")
	nb_mots = len(texte2.split(" ")) + len(lignes) - 1
	fichier.close()
	tps1 = time.time()
	for x in range(0, len(lignes)):
		lignes[x] = lignes[x].split(" ")
		sortie_lignes = []
		for mot in lignes[x]:
			if len(mot.split("-")) > 1:
				tirets = []
				for tiret in mot.split("-"):
					if len(tiret) >= 4:
						tirets.append(f"{traitement(tiret)}")
					else:
						tirets.append(f"{tiret}")
				tirets = '-'.join(tirets)
				sortie.append(tirets)
			else:
				if len(mot) >= 4:
					sortie.append(traitement(mot))
				else:
					sortie.append(mot)
			if compteur:
				i = i + 1
				p = "{:06.2F}".format(i * 100 / nb_mots)
				print(f"[{p}%] {i} sur {nb_mots} Traité")
		sortie.append("\n")
	tps2 = time.time()
	with codecs.open("output.txt","w", "utf-8") as fichier:
		for x in range(0, len(lignes)):
			sortie_lignes = " ".join(sortie).split("\n")
			sortie_lignes[x] = sortie_lignes[x].strip()
			fichier.write(f"{sortie_lignes[x]}\n")
		fichier.close()
	print(f"\n    {nb_mots} mots en {(tps2 - tps1)} seconde(s)")
	print(f"    {int(nb_mots/(tps2 - tps1))} Mots/s\n")
except Exception as e:
	print(f"    /!\\ Erreur: {e}\n")