from random import randrange

def afficher(M):
    "Affiche une matrice en respectant les alignements par colonnes"
    w=[max([len(str(M[i][j])) for i in range(len(M))]) for j in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            print("%*s" %(w[j],str(M[i][j])), end= ' ')
        print()  

def matriceNulle(n, p):
    "Constructeur de matrice de dimensions données"
    M=[]
    for i in range(n):
        L=[]
        for j in range(p):
            L.append(0)
        M.append(L)
    return M

def produitExterne(a,A):
    "Retourne le produit externe aA"
    n=len(A)
    p=len(A[0])
    B=matriceNulle(n,p)
    for i in range(n):
        for j in range(p):
            B[i][j]=a*A[i][j]
    return B

def matriceAleatoire(n,p, a, b):
    A=matriceNulle(n,p)
    for i in range(n):
        for j in range(p):
            A[i][j] = randrange(a, b+1)
    return A    

def dimensions(A):
    return [len(A), len(A[0])]

def extraireColonne(A,j):
    p=len(A[0])
    col=[]
    for i in range(p):
        col.append(A[i][j])
    return col

def identite(n):
    M=matriceNulle(n,n)
    for i in range(n):
        M[i][i]=1
    return M

def sontEgales(A,B):
    n,p=dimensions(A)
    s,t=dimensions(B)
    if n!=s or p!=t:
        return False
    for i in range(n):
        for j in range(p):
            if A[i][j] != B[i][j]:
                return False
    return True

def oppose(A):
    return produitExterne(-1,A)

def somme(A,B):
    n,p=dimensions(A)
    S=matriceNulle(n,p)
    for i in range(n):
        for j in range(p):
            S[i][j] = A[i][j] + B[i][j]
    return S

def transpose(A):
    n,p=dimensions(A)
    B=matriceNulle(p,n)
    for j in range(n):
        for i in range(p):
            B[i][j]=A[j][i]
    return B

def trace(A):
    n,p = dimensions(A)
    s = 0
    for i in range(n) :
        s += A[i][i]
    return s

def produit(A,B):
    n,p = dimensions(A)
    q,r = dimensions(B)
    C = matriceNulle(n,r)
    for i in range(n) :
        for j in range(r) :
            for k in range(p) :
                C[i][j] += A[i][k]*B[k][j]
    return C
