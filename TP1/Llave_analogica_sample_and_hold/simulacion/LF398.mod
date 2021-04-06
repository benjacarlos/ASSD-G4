.subckt LF398H 3 8 7 4 6 5 1
* INPUT STAGE
VOS 10 3 DC 2E-3
EPR 11 10 1 4 3.162E-6
RIN 11 100 1E+10
GIB 100 3 16 0 1E-9
IIB 0 16 1
RIB 16 0 3.5 TC=-.02762 3.81E-5
* INTERMEDIATE STAGE
EA 12 100 11 100 1
MSD 12 13 14 15 SDS
RMS 15 100 1MEG
ES 13 100 21 22 500
RC 14 6 300
RCC 6 100 5E+11
CF 3 14 0.32P
* LOGIC CONTROL
RL 8 7 1.5E+6
EL 20 0 8 7 1
RE 20 21 70
DL 24 20 DMOD
RDL 21 24 3.5
VE 23 0 1
CC 21 6 2P
CE 21 22 0.1U
DE 21 23 DMOD
VL 22 0 1.4
* OUTPUT STAGE
ERF 1 100 1 4 .5
DD1 31 32 MID
DD2 33 31 MID
VF2 32 100 0
VF3 100 33 0
FF1 100 31 VF1 1
GOT 100 34 45 100 2
ROT 100 34 0.5
RO1 1 5 200MEG
RO2 5 4 200MEG
RAC 34 35 0.1
VF1 35 5 0
RP1 1 100 3.5K
RP2 4 100 3.5K
FF2 100 1 VF2 -1
FF3 4 100 VF3 -1
* OUTPUT SHORT CIRCUIT CURRENT
GR 100 45 6 100 1E-3
RR 100 45 1K
MD1 45 42 100 43 SDS
MD2 45 44 100 43 SDS
RNM 43 100 1MEG
HF1 42 100 POLY(1) VF1 -65 5000
HF2 44 100 POLY(1) VF1 -32.5 -5000
.MODEL SDS NMOS KP=1
.MODEL DMOD D
* SPECTRE: + IMAX=1000
.MODEL MID D
* SPECTRE: + IMAX=1000
.ends