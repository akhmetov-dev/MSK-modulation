clc;
clear;

conn = sqlite('../ex.sqlite','readonly');
sqlquery = 'SELECT * FROM data';
results = fetch(conn,sqlquery);
close(conn);

figure;
plot(cell2mat(results(:, 2))), grid on;

figure;
plot(cell2mat(results(:, 3))), grid on;

figure;
plot(cell2mat(results(:, 4))), grid on;

figure;
plot(cell2mat(results(:, 5))), grid on;

figure;
plot(cell2mat(results(:, 6))), grid on;

figure;
plot(cell2mat(results(:, 7))), grid on;

figure;
plot(cell2mat(results(:, 8))), grid on;

scatterplot (cell2mat(results(:, 8))), grid on;