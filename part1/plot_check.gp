set title 'Check set: correct vs wrong'
set xlabel 'X1'
set ylabel 'X2'
set grid
set key left top
plot 'check_correct.dat' using 1:2 with points pt 7 ps 0.7 title 'Correct', 'check_wrong.dat'   using 1:2 with points pt 5 ps 0.9 title 'Wrong'
pause -1
