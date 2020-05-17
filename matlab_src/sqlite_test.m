clc;
clear;

dbfile = '../ex.sqlite';

conn = sqlite(dbfile,'readonly');

sqlquery1 = 'SELECT msg FROM data';
sqlquery2 = 'SELECT mod_msg FROM data';
sqlquery3 = 'SELECT mul1 FROM data';
sqlquery4 = 'SELECT mul2 FROM data';
sqlquery5 = 'SELECT sub FROM data';
sqlquery6 = 'SELECT demod FROM data';
sqlquery7 = 'SELECT demod_msg FROM data';

results1 = fetch(conn,sqlquery1);
results2 = fetch(conn,sqlquery2);
results3 = fetch(conn,sqlquery3);
results4 = fetch(conn,sqlquery4);
results5 = fetch(conn,sqlquery5);
results6 = fetch(conn,sqlquery6);
results7 = fetch(conn,sqlquery7);


figure
plot(results1)

close(conn);