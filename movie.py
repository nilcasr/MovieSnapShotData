import math
import sys

sys.stdout=open("movie.gnu","w")


print("reset")
print("set key noautotitle")


print("set terminal pngcairo truecolor nocrop font 'arial 14' size 16 inches,9 inches")


print("set style line 2  linetype 1 linecolor rgb '#800080'  linewidth 2.000 pointtype 2 pointsize 0.3")
print("set style line 1  linetype 1 linecolor rgb '#FF0000'  linewidth 2.000 pointtype 2 pointsize 0.3")



print("set ylabel \"Semimajor axis (km)\"") 
print("set xlabel \"Mean Longitude (degree)\"")

print("set xrange[0:360]")
print("set xtics 30")
print("#set yrange[136700:]")

letra="%d"
n=501
arco="G"
for i in range(n):
	print("unset label")
	print("set label \"Snapshot-%4.1f years\" at graph 0.5, graph 0.95 center" %(i))
	print("set output \"movieArc%s/imagem%0.4d.png\"" % (arco,i+1))
	print("plot \"OutSnapArc%s/OutSnapArc%s%d.ae\"u 5:($3!=0?$3:1/0) pt 7 ps 0.2 lc 1,\"\" u ($9==1?$5:1/0):($3!=0?$3:1/0) pt 7 ps 0.7 lc 2, \"\" u 5:($7!=0?$7:1/0) w l"% (arco,arco,i+1))



	

sys.stdout.close()


