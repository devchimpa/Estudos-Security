# O netcat pode ser utilizado também para varredura de portas.
# neste script ele é utilzado para trazer as portas abertas

echo " Digite o IP do alvo: "
read ALVO

PORTA_FECHADA=1

varre_portas(){

PORTAS=" 443  21  22  80 5432 "

for i in ${PORTAS[*]}

do

ABERTAS=$( nc -z -n -v $ALVO $i 2>&1>/dev/null )

CONEXOES=$( echo "$ABERTAS" | grep "open" )

if test -n "$CONEXOES"
then

PORTA_ABERTA=$( echo "$CONEXOES" | awk {'print $3 '} )
PROTOCOLO_ABERTO=$( echo "$CONEXOES" | awk {'print $4'} )
echo " $PORTA_ABERTA $PROTOCOLO_ABERTO OPEN. "
PORTA_FECHADA=0
else
TESTANDO=0
fi

done
}

ping -c 2 $ALVO 2>&1>/dev/null
VIVO=$( echo $? )
if [ $VIVO -eq 0 ]
then
varre_portas
else
echo "O alvo: $ALVO Parece estar indisponível."
exit 1
fi

