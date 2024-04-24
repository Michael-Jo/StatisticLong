#Lambda : Statement Function yang tidak memiliki def

def kuadrat( num ):
    return num **2
print( f"Result Kuadrat : { kuadrat(4) }")
#syntax :
# output = lambda variabel_parameter : expression
ResultKuadrat = lambda abc : abc ** 2
print( f"Result Kuadrat lambda: { ResultKuadrat(4) }")

def pangkat ( angka, pangkat ):
    return angka ** pangkat
print( f"Result pangkat : { pangkat( 4,3 ) }" )

ResultKuadrat = lambda a, b : a ** a

print( f"hasil 5 pangkat 2 { ResultKuadrat( 5, 2 ) } ")

def batas():
    print( "-"*15 )

batas()
dataAlf = [ "bbb", "cc", "d", "zzzz", "aa"]
dataAlf.sort()
print( f"data sorted : { dataAlf }")

def pnjData( data ):
    return len( data )

dataAlf.sort( key = pnjData )