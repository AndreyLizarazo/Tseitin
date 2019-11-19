# -*- coding: utf-8 -*-

conectivosB = ["O","Y",">","="]

class Tree(object):
	def __init__(self, r, iz, der):
		self.left = iz
		self.right = der
		self.label = r

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula

    if f.right == None:
        return f.label
    elif f.label == '~':
        return f.label + Inorder(f.right)
    else:
        return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"


def StringtoTree(A, letrasProposicionales):
    # Crea una formula Inorder(StringtoTree(regla,letras))como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree
    conectivos = ['-', 'O', 'Y', '>','=']
    pila = []
    for c in A:
        if c not in conectivos and c in letrasProposicionales:
            pila.append(Tree(c,None,None))
        else :
            if c == '-':
                formulaAux = Tree(c, None, pila[-1])
                del pila[-1]
                pila.append(formulaAux)
            elif c in conectivos and c != '-':
                formulaAux = Tree(c, pila[-1], pila[-2])
                del pila[-1]
                del pila[-1]
                pila.append(formulaAux)
    return pila[-1]




def atomos():
    e = "abcdefghijklmnqp"
    letras = []
    for i in e:
        t = i.upper()
        letras.append(i)
        letras.append(t)
    return letras

def Tseitin(A, letrasProposicionalesA):
	letrasProposicionalesB = [chr(x) for x in range(256, 1200)]
	#assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB)))
	L = []
	Pila = [] # Inicializamos pila
	i = -1 # Inicializamos contador de variables nuevas
	s = A[0] # Inicializamos sımbolo de trabajo
	atomos = letrasProposicionalesA + letrasProposicionalesB
	while (len(A) > 0):
		#print('A', A, ' L', L, ' Pila', Pila, ' i', i, ' s', s)
		if s in atomos and len(Pila)>0 and Pila[-1] =='-':
			i += 1
			atomo = letrasProposicionalesB[i]
			Pila = Pila[:-1]
			Pila.append(atomo)
			L.append(atomo + '=' + '-' + s)
			A = A[1:]
			if len(A) > 0:
				s = A[0]

		elif s == ')':
			w = Pila[-1]
			O = Pila[-2]
			v = Pila[-3]
			Pila = Pila[:len(Pila)-4]
			i += 1
			atomo = letrasProposicionalesB[i]
			L.append(atomo +"="+"(" + v + O + w + ")")
			s = atomo

		else:
			Pila.append(s)
			A = A[1:]
			if len(A) > 0:
				s = A[0]
			#print('A', A)

	B = ""
	if i < 0:
		atomo = Pila[-1]
	else:
		atomo = letrasProposicionalesB[i]

	for x in L:
		y = enFNC(x)
		B += "Y" + y

	B = atomo + B
	return B


# Output: B (cadena), equivalente en FNC
def enFNC(A):
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
# def Tseitin(A, letrasProposicionalesA):
#     letrasProposicionalesB = [chr(x) for x in range(256, 300)]
#     assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB)))
#     l = []
#     pila = []
#     i = -1
#     s = A[0]
#     while len(A) > 0:
#         if s in letrasProposicionalesA and pila[-1] == '-':
#             i += 1
#             atomo = letrasProposicionalesB[i]
#             pila = pila[:-1]
#             pila.append(atomo)
#             l.append(atomo + '=-' + s)
#             A = A[1:]
#             s = A[0]
#             if len(A) > 0:
#                 s = A[0]
#         elif s == ')':
#             w = pila[-1]
#             o = pila[-2]
#             v = pila[-3]
#             pila = pila[:len(pila)-4]
#             i += 1
#             atomo = letrasProposicionalesB[i]
#             l.append(atomo + "=" + v + o + w)
#             s = atomo
#         else:
#             pila.append(s)
#             A = A[1:]
#             if len(A) > 0:
#                 s = A[0]
#
#     b = ''
#     if i < 0:
#         atomo = pila[-1]
#     else:
#         atomo = letrasProposicionalesB[i]
#     for x in l:
#         y = enFNC(x)
#         b += 'Y' + y
#     b = atomo + b
#
#     return "OK"

# Subrutina Clausula para obtener lista de literales
# Input: C (cadena) una clausula
# Output: L (lista), lista de literales
def Clausula(C):
    L=[]
    while len(C)>0:
        s=C[0]
        if s == "O":
            C=C[1:]
        elif s=="~":
            literal = s + C[1]
            L.append(literal)
            C = C[2:]
        else:
            L.append(s)
            C = C[1:]
    return L

# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC
# Output: L (lista), lista de listas de literales
def formaClausal(A):
	L=[]
	i=0
	while len(A)>0:
		if i == len(A)-1:
			L.append(Clausula(A))
			A = ''
		else:
			if A[1] == 'Y':
				L.append(Clausula(A[:i]))
				A = A[i+1]
				i = 0
			else:
				i+= 1
	return L





def regla1():
	a = "(((aY-A)O(aY-A))O(-aY-A))"
	b = "(((bY-B)O((-bYB))O(-bY-B))"
	c = "(((cY-C)O(-cYC))O(-cY-C))"
	d = "(((dY-D)O(-dYD))O(-dY-D))"
	e = "(((eY-E)O(-eYE))O(-eY-E))"
	f = "(((fY-F)O(-fYF))O(-fY-F))"
	g = "(((gY-G)O(-gYG))O(-gY-G))"
	h = "(((hY-H)O(-hYH))O(-hY-H))"
	i = "(((iY-I)O(-iYI))O(-iY-I))"
	j = "(((jY-J)O(-jYJ))O(-jY-J))"
	k = "(((kY-K)O(-kYK))O(-kY-K))"
	l = "(((lY-L)O(-lYL))O(-lY-L))"
	m = "(((mY-M)O(-mYM))O(-mY-M))"
	n = "(((nY-N)O(-nYN))O(-nY-N))"
	q = "(((qY-Q)O(-qYQ))O(-qY-Q))"
	p = "(((pY-P)O(-pYP))O(-pY-P))"
	r1 = "(" + a + "Y" + b +")"
	r2 = "("+r1+"Y"+c+")"
	r3 = "("+r2+"Y"+d+")"
	r4 = "("+r3+"Y"+e+")"
	r5 = "("+r4+"Y"+f+")"
	r6 = "("+r5+"Y"+g+")"
	r7 = "("+r6+"Y"+h+")"
	r8 = "("+r7+"Y"+i+")"
	r9 = "("+r8+"Y"+j+")"
	r10 = "("+r9+"Y"+k+")"
	r11 = "("+r10+"Y"+l+")"
	r12 = "("+r11+"Y"+m+")"
	r13 = "("+r12+"Y"+n+")"
	r14 = "("+r13+"Y"+q+")"
	r15 = "("+r14+"Y"+p+")"
	regla = r15
	return regla




molino1 = "((((aY-A)Y(bY-B))Y(cY-C))O(((-aYA)Y(-bYB))Y(-cYC)))"
molino2 = "((((aY-A)Y(dY-D))Y(nY-N))O(((-aYA)Y(-dYD))Y(-nYN)))"
molino3 = "((((cY-C)Y(jY-J))Y(pY-P))O(((-cYC)Y(-jYJ))Y(-pYP)))"
molino4 = "((((nY-N)Y(qY-Q))Y(pY-P))O(((-nYN)Y(-qYQ))Y(-pYP)))"
molino5 = "((((eY-E)Y(fY-F))Y(gY-G))O(((-eYE)Y(-fYF))Y(-gYG)))"
molino6 = "((((eY-E)Y(hY-H))Y(kY-K))O(((-eYE)Y(-hYH))Y(-kYK)))"
molino7 = "(((gY-G)Y((iY-I)Y(mY-M)))O((-gYG)Y((-iYI)Y(-mYM))))"
molino8 = "((((kY-K)Y(lY-L))Y(mY-M))O(((-kYK)Y(-lYL))Y(-mYM)))"

def regla3():
	r1 = "(" +molino1+"O"+ molino2+"O"+")"
	r2= "("+r1+"O"+molino3+")"
	r3= "("+r2+"O"+molino4+")"
	r4= "("+r3+"O"+molino5+")"
	r5= "("+r4+"O"+molino6+")"
	r6= "("+r5+"O"+molino7+")"
	regla= "("+r6+"O"+molino8+")"
	return regla
def ClausulaRegla3():
    a = regla1()
    print(a)
    z = ""
    for i in a:
         if i not in "()":
             z += i

    #print(z)
    print( formaClausal(z))
# S = LetrasProposicionales
# I = {}
# def r1(S):
#     for i in S:
#         if len(i) == 1:
#             return True
#     return False
# def r2(S,I):
#     l = ""
#     temp = ""
#     I2 = I.keys()
#     for i in S:
#         for j in i:
#             if len(j) != 1:
#                 temp = j[1]
#             else:
#                 temp = j
#             if temp not in I2:
#                 l = j
#                 print(l)
#                 for x in S:
#                     if l in x:
#                         print(x)
#                         S.remove(x)
#
#                 if '-' not in l:
#                     I[l] = 1
#                     lc = '-' + l
#                     for e in S:
#                         if lc in e:
#                             e.remove(lc)
#                 if '-' in l:
#                     I[l[1]] = 0
#                     lc = l[1]
#                     for y in S:
#                         if lc in y:
#                             y.remove(lc)
#                 break
#
#     return S,I
#
#
# def unitPropagate(S,I):
#     while(r1(S)==True):
#         l = ""
#         for x in S:
#             if len(x) == 1:
#                 l = x[0]
#                 #print(l,x)
#                 S.remove(x)
#                 break
#
#         if '-' in l:
#             I[l[1]] = 0
#             lc = l[1]
#             for j in S:
#                 if l in j:
#                     S.remove(j)
#                 if lc in j:
#                     j.remove(lc)
#
#         if '-' not in l:
#             I[l] = 1
#             lc = '-' + l
#             for i in S:
#                 if l in i:
#                     S.remove(i)
#                 if lc in i:
#                     i.remove(lc)
#
#         unitPropagate(S,I)
#
#
#     return S,I
#
#
# def DPLL(S,I):
#     if r1(S):
#         unitPropagate(S,I)
#
#
#     if len(S)==1:
#         x = S[0]
#         for i in x:
#             if i not in I.keys():
#                 l = i
#                 if '-' not in l:
#                     I[l] = 1
#                     S.remove(x)
#                     break
#                 if '-' in l:
#                     I[l[1]] = 0
#                     S.remove(x)
#                     break
#
#
#     if [] in S:
#         return "Insatisfacible", I
#     if len(S) == 0:
#         return "Satisfacible", I
#     else:
#         r2(S,I)
#     return DPLL(S,I)

""" tratar de hacer reglas en polaca"""
#print("Regla 3:", "\n")
#print(regla3(),"\n")
# print("Regla 1:", "\n")
# print(regla1(),"\n")
x = atomos()
# print(Tseitin(regla1(),x))
# print(Tseitin(regla3(),x))
#print(Clausula(regla1()))
#ClausulaRegla3()

formula = '-(a>b)'
#tseit = Tseitin(formula, x)
#print('Tseitin:', tseit)
re1= regla1()
re3 = regla3()

forma = Tseitin(re3,x)
final= "("+re1+"Y"+re3+")"
#print(Tseitin(re1,x))
print('\n'*3)
#print(Tseitin(re3,x))
print('\n'*3)
print(Tseitin(final,x))
print('\n'*3)
#print(re3)
print('\n'*3)
#print(re1)

print('\n'*3)
#print(final)

print('\n'*3)
print(formaClausal(final))

#print(formaClausal(forma))
