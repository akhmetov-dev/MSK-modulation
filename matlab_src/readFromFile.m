clc;
% clear;

fid = fopen('../ex.txt', 'r');

data = fscanf(fid, '%f');

figure;
plot(VarName1), grid on;

figure;
plot(VarName2), grid on;

figure;
plot(VarName3), grid on;

figure;
plot(VarName4), grid on;

figure;
plot(VarName5), grid on;

figure;
plot(VarName6), grid on;

figure;
plot(VarName7), grid on;

scatterplot ( hilbert (VarName7)), grid on;

fclose(fid);