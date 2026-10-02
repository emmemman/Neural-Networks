set terminal pngcairo size 900,900
set output "plot_M13.png"

set title "k-means best solution (M=13)"
set xlabel "x1"
set ylabel "x2"
set xrange [0:2]
set yrange [0:2]
set size square
set key outside

plot "sdo_data.txt" using 1:2 with points pointtype 1 title "data (+)", \
     "centers_M13.txt" using 1:2 with points pointtype 2 pointsize 2 title "centers (*)"
