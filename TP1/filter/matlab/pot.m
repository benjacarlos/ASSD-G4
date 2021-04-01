clear all;
clearvars
clc
%%%%%%%%%%%%%%%%%%%%%%%%%%%Diente de Sierra%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
m_limit = 20;
fo = 23e3;
fos = (1:m_limit);
Ao = 1/2;
relacion = [];

syms k
for m = 1:m_limit
	S_symsum = Ao^2 + symsum(1/(2*pi*k)^2, k, 1, m);
	relacion = [relacion S_symsum/(1/24 + Ao^2)];
end 



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Sin%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% m_limit = 10;
% fo = 23e3;
% fos = (1:m_limit);
% relacion = [];
% 
% syms k
% for m = 1:m_limit
% 	S_symsum = symsum(1/(4*k^2-9)^2, k, -m, m);
% 	relacion = [relacion S_symsum/(pi^2/72)];
% end 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%PLOT%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
plot(fos, relacion);
grid on
xlabel('m Armonicos');
ylabel('Pm/P');
title('Relacion de Potencia');

