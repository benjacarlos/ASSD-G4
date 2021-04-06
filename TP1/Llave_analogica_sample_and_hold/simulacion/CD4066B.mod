**********
*SRC=CD4066B;CD4066B;Analog Switch;;
*SYM=CD4066B
.SUBCKT CD4066B 11 4 2 10 7
*Analog Switch In Out Control Vdd Vss
X1 2 6 10 7 INVERT
X2 6 1 10 7 INVERT
M1 14 6 7 7 CD4001BN
M7 11 6 14 10 CD4001BP
M3 11 1 14 14 CD4001BN
M4 11 1 4 14 CD4001BN
M8 11 6 4 10 CD4001BP
.MODEL CD4001BN NMOS (LEVEL=1 VTO=3.5 KP=3.2M GAMMA=3.97U
+ PHI=.75 LAMBDA=1.87M RD=23.2 RS=90.1 IS=31.2F PB=.8 MJ=.46
+ CBD=63.5P CBS=76.2P CGSO=93.6N CGDO=78N CGBO=128N)
.MODEL CD4001BP PMOS (LEVEL=1 VTO=-3.0 KP=2.4M GAMMA=3.97U
+ PHI=.75 LAMBDA=1.87M RD=21.2 RS=62.2 IS=31.2F PB=.8 MJ=.46
+ CBD=63.5P CBS=76.2P CGSO=93.6N CGDO=78N CGBO=128N)
.ENDS
.SUBCKT INVERT 1 2 3 4
* Inverter In Out Vcc Vss
M1 2 1 3 3 CD4049P
M2 2 1 4 4 CD4049N
.MODEL CD4049P PMOS (LEVEL=1 VTO=-2.9 KP=2M GAMMA=3.97U
+ PHI=.75 LAMBDA=1.87M RD=28.2 RS=45.2 IS=31.2F PB=.8 MJ=.46
+ CBD=21.2P CBS=25.4P CGSO=31.2N CGDO=26N CGBO=42.8N)
.MODEL CD4049N NMOS (LEVEL=1 VTO=2.1 KP=5M GAMMA=3.97U
+ PHI=.75 LAMBDA=1.87M RD=4.2 RS=4.2 IS=31.2F PB=.8 MJ=.46
+ CBD=21.2P CBS=25.4P CGSO=31.2N CGDO=26N CGBO=42.8N)
.ENDS
**********