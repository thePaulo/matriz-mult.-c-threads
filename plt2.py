import csv
from matplotlib  import pyplot as plt

arquivo = open('tp2/1024x1024/1024x1024tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 1024 threaded")

plt.plot(vector)
##############################################################
plt.figure()
#plt.axis([0,20,0,15]);

arquivo = open('tp2/512x512/512x512tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 512 threaded")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tp2/256x256/256x256tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 256 threaded")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tp2/128x128/128x128tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 128 threaded")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tp2/64x64/64x64tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 64 threaded")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tp2/32x32/32x32tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 32 threaded")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tp2/16x16/16x16tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 16 threaded")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tp2/8x8/8x8tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 8 threaded")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tp2/4x4/4x4tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 4 threaded")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tp2/2048x2048/2048x2048tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 2048 threaded")


plt.plot(vector)
plt.show()