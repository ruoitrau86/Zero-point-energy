#Read input filename
inputname = raw_input("Input filename: ")
input = open(inputname,"r")
for line in input:
    if "/" in line:
        break
#Get number of q-points
for line in input:
    list = line.split()
    nq = int(list[0])
    break
#Get weights for each q-points
weights = []
for line in input:
    list = line.split()
    weights.append(float(list[3]))
#Get frequencies
freqs = []
for i in range(nq):
    qn = []
    filename = "dyn"+str(i+1)
    file = open(filename,"r")
    for line in file:
        if "freq" in line:
            list = line.split()
            qn.append(float(list[7]))
    freqs.append(qn)
    file.close()
#Calculate zero point energy
tsum = 0
wpeV = 8065.54429
for i in range(len(freqs)): #sum over q-points
    qsum = 0
    for j in range(len(qn)): #sum over frequencies
        qsum += freqs[i][j]
    qsum = 1/wpeV/2.0*qsum
    tsum += weights[i]*qsum
print tsum/sum(weights)