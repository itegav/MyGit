def double():
	n = int(input("quel nombre avez vous fait ?"))
	compteur = 0
	for i in range(1,6) :
		for j in range(1,6) :
			if i+j == n :
				compteur +=1
	return compteur

def triple():
	n = int(input("quel nombre avez vous fait entre 3 et 18 ?"))
	compteur = 0
	for i in range(1,6):
		for j in range(1,6):
			for k in range(1,6):
				if i+j+k==n :
					compteur +=1
	return compteur

compteur = 0

def nimporte(s, nbd,compteur):
	if nbd == 1 and s < 7:
		compteur +=1
	else :
		for i in range(1,6):
			if s-i >= 1 :
				compteur = nimporte(s-i,nbd-1,compteur)
	return compteur