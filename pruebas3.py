# -*- coding: utf-8 -*-
import copy
import ax
def atomos():
    e = "abcdefghijklmnqp"
    letras = []
    for i in e:
        t = i.upper()
        letras.append(i)
        letras.append(t)
    return letras



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

def Clausula(C):
    L=[]
    while len(C)>0:
        s=C[0]
        if s == "O":
            C=C[1:]
        elif s== "-":
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
    l = []
    i = 0
    while len(A)> 0:
        if i >= len(A):
            l.append(Clausula(A))
            A = []
        else:
            if A[i] == 'Y':
                l.append(Clausula(A[:i]))
                A = A[i+1:]
                i = 0
            else:
                i+=1
    return l





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
	r1 = a + "Y" + b
	r2 = "("+"("+r1+"Y"+c+")"+")"
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
	r1 = "(" +molino1+"O"+ molino2+")"
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
def neg(a):
    if len(a) == 1:
        l = "-" + a
    else:
        l = a[-1]
    return l


def unitPropagate(S, I):
    bool = True
    while bool:
        for k in S:
            if len(k) == 0:
                #return "Insatisfacible", {}
                break

        cont = 0
        for i in S:
            if len(i) == 1:
                cont += 1
                lit = i[0]
                if len(lit) == 1:
                    pp = lit
                    compl = "-" + lit
                    valor = 1

                elif(len(lit) == 2):
                    pp = lit[1]
                    compl = lit[1]
                    valor = 0

                for j in S:
                    if j != i:
                        if lit in j:
                            S.remove(j)
                I[pp] = valor
                S.remove(i)
                #print(i)


        if cont == 0:
            bool = False
        else:
            for k in S:
                if compl in k:
                    k.remove(compl)
    return S, I

def DPLL(s, i):
    void = []
	
    s, i = unitPropagate(s,i)
    if void in s:
        return "Insatisfacible", {}
    elif len(s) == 0:
        return "Satisfacible", i
    l = ""
    for y in s:
        for x in y:
            if x not in i.keys():
                l = x
    l_comp = neg(l)
    if l == "":
        return None
    Sp = copy.deepcopy(s)
    Sp = [n for n in Sp if l not in n]
    for q in Sp:
        if l_comp in q:
            q.remove(neg(l))
    Ip = copy.deepcopy(i)
    if l[0] == "-":
        Ip[l[1]] = 0
    else:
        Ip[l] = 1
    S1, I1 = DPLL(Sp, Ip)
    if S1 == "Satisfacible":
        return S1, I1
    else:
        Spp = copy.deepcopy(s)
        Spp = [q for q in Spp if neg(l) not in q]
        for h in Spp:
            if l in h:
                h.remove(l)
        Ipp = copy.deepcopy(i)
        if l[0] == "-":
            Ipp[l[1]] = 0
        else:
            Ipp[l] = 1
        return DPLL(Spp, Ipp)






""" tratar de hacer reglas en polaca"""

x = atomos()
def quitar(DPLL2):
	letras = atomos()
	misLetras = {}
	k = DPLL2.keys()
	letra = []
	for b in k:
		if b in letras:
			letra.append(b)
	letra.sort()
	for i in letras:
		misLetras[i] = DPLL2.get(i)

	return misLetras
formula = '-(a>b)'
#tseit = Tseitin(formula, x)
#print('Tseitin:', tseit)
#re1= regla1()
re3 = regla3()
re1 = regla1()
#print(re1)
# print(re3)
forma = Tseitin(re3,x)
final= "("+re1+"Y"+re3+")"
forma = Tseitin(final,x)
#print(forma)
#u = formaClausal(forma)
#print(u)
#print(DPLL(u,{}))
# #
# # print('\n'*3)
# # r = Tseitin(final,x)
# # print(regla1())
#print(Tseitin(regla1(),x))
a = {}
t = formaClausal(forma)
#print(DPLL(t,a))

f = (DPLL(t,a))
f[1]
f[0]
print(f[0])
u = quitar(f[1])
print(u)
print(len(u))
ax.create_situation(u)
