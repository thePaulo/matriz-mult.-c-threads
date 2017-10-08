import csv
from matplotlib  import pyplot as plt

arquivo = open('tempos/1024x1024/1024x1024tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 1024 normal")

plt.plot(vector)
##############################################################
plt.figure()
#plt.axis([0,20,0,15]);

arquivo = open('tempos/512x512/512x512tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 512 normal")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tempos/256x256/256x256tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 256 normal")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tempos/128x128/128x128tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 128 normal")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tempos/64x64/64x64tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 64 normal")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tempos/32x32/32x32tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 32 normal")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tempos/16x16/16x16tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 16 normal")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tempos/8x8/8x8tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 8 normal")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tempos/4x4/4x4tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 4 normal")


plt.plot(vector)
##############################################################
plt.figure()

arquivo = open('tempos/2048x2048/2048x2048tempo.txt','r')
reader = csv.reader(arquivo	)
vector = []
for linha in reader:
	vector.append(linha)

plt.xlabel("samples")
plt.ylabel("time")
plt.title("tempo 2048 normal")


plt.plot(vector)
plt.show()