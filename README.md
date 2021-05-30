# Desafio Python - Lógica de Programação

O programa foi criado para responder ao seguinte desafio:
```
Objetivo
O objetivo desse desafio é demonstrar seu conhecimento e seu raciocínio na resolução de um problema relacionado à lógica de programação, assim saberemos como você pensa e como resolve problemas na vida real.
 
O Problema
Um robô deve ser colocado pela MRSA (Mercado Radar Space Agency) para explorar um terreno em Marte.
Esse terreno, que é retangular, precisa ser navegado pelo robô de tal forma que suas câmeras acopladas possam obter uma visão completa da região, enviando essas imagens novamente para o QG da Mercado Radar.
 
A posição do robô é representada pela combinação de coordenadas cartesianas (x, y) e por uma letra, que pode representar uma das quatro orientações: NORTH, SOUTH, EAST e WEST.
Para simplificar a navegação, a região marciana a ser explorada foi subdividida em sub-regiões retangulares.
Uma posição válida do robô, seria (0, 0, N), que significa que o robô está posicionado no canto esquerdo inferior do terreno, voltado para o Norte.
Para controlar o robô, a MRSA envia uma string simples, que pode conter as letras ‘L’, ‘R’ e ‘M’. As letras ‘L’ e ‘R’ fazem o robô rotacionar em seu próprio eixo 90 graus para esquerda ou para direita, respectivamente, sem se mover da sua posição atual. A letra ‘M’ faz o robô deslocar-­se uma posição para frente.
Assuma que o robô se movimenta para o NORTE em relação ao eixo y. Ou seja, um passo para o NORTE da posição (x,y), é a posição (x, y+1)
Exemplo: Se o robô está na posição (0,0,N), o comando "MML" fará ele chegar na posição (0,2,W)
 
Requisitos do desafio
O terreno deverá ser iniciado com 5x5 posições;
O robô inicia na coordenada (0,0,N);
Todos os comandos enviados ao robô devem retornar a posição dele (Posição após a execução do comando);
O robô não pode se movimentar para fora da área especificada;
Não é necessário guardar o estado do robô;
 
Objetivo Final
Escreva um programa que permita aos engenheiros da MRSA enviar comandos para o robô e saber onde ele se encontra. Os engenheiros irão rodar testes no seu software para garantir que ele se comporta da forma esperada, antes de enviar o robô para Marte.
 

Requisitos técnicos
O desafio deve ser escrito na liguagem de programação em Python;
Não deverá ser utilizada qualquer biblioteca de terceiros;
```
