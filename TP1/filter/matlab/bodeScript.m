clear all;
% f = linspace(100,10e6,128);
% f = w/(2*pi);
s   = tf('s');

%%%%%%Funcion de transferencia%%%%%%%%%
H1 = (9.36e10)/(s^2+5.12e5*s+7.93e10);
H2 = (3.21E11)/(s^2+4.21E5*s+1.64E11);
H3 = (7.37E11)/(s^2+2.73E5*s+2.96E11);
H4 = (9.36e10)/(s^2+9.6e4*s+3.98e11);

H = H1*H2*H3*H4;

%%%%%%%%Cargar los csv%%%%%%%%
% DatosSimulados=csvread('RC.csv',2);
% DatosMedidos=csvread('bodeRC.csv',2);

% theoryBode(H);
close all
opt = bodeoptions();
opt.FreqUnits = 'Hz';
opt.PhaseVisible='off';

% %%%%%%%Bode phase%%%%%%%
[mag,pha,wout]=bode(H4, opt);
mag = squeeze(mag);
pha = squeeze(pha);
% semilogx(wout/(2*pi), pha,'LineWidth',1);
% hold on;
% 
% semilogx(DatosSimulados(:,1),DatosSimulados(:,3),'r','LineWidth',1);
% semilogx(DatosMedidos(:,1),DatosMedidos(:,3),'k','LineWidth',1);
% 
% xlabel('frecuencia [Hz]');
% ylabel('fase [grados]');
% title('Diagrama de fase');
% legend({'Teorico','Simulado','Experimental'});
% grid on
% hold off;
% 
%%%%%%%%%%Bode mag%%%%%%%%%%
figure;
semilogx(wout/(2*pi), 20*log10(mag),'LineWidth',1);
hold on;

%%%%%%%%%%Datos en dB%%%%%%%%
% semilogx(DatosSimulados(:,1),DatosSimulados(:,2),'r','LineWidth',1);
% semilogx(DatosMedidos(:,1),DatosMedidos(:,2),'k','LineWidth',1);
% 
% xlabel('frecuencia [Hz]');
% ylabel('magnitud [db]');
% title('Diagrama de magnitud');
% legend({'Teorico','Simulado','Experimental'});
grid on
hold off;



