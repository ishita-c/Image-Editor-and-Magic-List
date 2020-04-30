# name: File path of the pgm image file
# Output is a 2D list of integers
def readpgm(name):
	image = []
	with open(name) as f:
		lines = list(f.readlines())
		if len(lines) < 3:
			print("Wrong Image Format\n")
			exit(0)

		count = 0
		width = 0
		height = 0
		for line in lines:
			if line[0] == '#':
				continue

			if count == 0:
				if line.strip() != 'P2':
					print("Wrong Image Type\n")
					exit(0)
				count += 1
				continue

			if count == 1:
				dimensions = line.strip().split(' ')
				print(dimensions)
				width = dimensions[0]
				height = dimensions[1]
				count += 1
				continue

			if count == 2:	
				allowable_max = int(line.strip())
				if allowable_max != 255:
					print("Wrong max allowable value in the image\n")
					exit(0)
				count += 1
				continue

			data = line.strip().split()
			data = [int(d) for d in data]
			image.append(data)
	return image

def averagepgm(x):
	H=len(x)
	W=len(x[0])
	p=[[0 for col in range (W)]for row in range (H)]
	for i in range (1,H-1):
		for j in range (1,W-1):
			p[i][j]=(x[i-1][j-1]+x[i-1][j]+x[i-1][j+1]+x[i][j-1]+x[i][j]+x[i][j+1]+x[i+1][j-1]+ x[i+1][j]+x[i+1][j+1])/9
	#corner pixels to take average of three neighbouring pixels
	p[0][0]=(x[1][0]+x[0][1]+x[1][1])/3
	p[0][W-1]=(x[0][W-2]+x[1][W-1]+x[1][W-1])/3
	p[H-1][0]=(x[H-1][1]+x[H-2][0]+x[H-2][1])/3
	p[H-1][W-1]=(x[H-2][W-1]+x[H-1][W-2]+x[H-2][W-2])/3
	# for pixels at edge and not on corners to take avg of five neighbouring pixels
	for i in range (1,H-1):
		p[i][0]=(x[i-1][0]+x[i-1][1]+x[i][1]+x[i+1][1]+x[i+1][0])/5
	for i in range (1,H-1):
		p[i][W-1]=(x[i-1][W-1]+x[i-1][W-2]+x[i][W-2]+x[i+1][W-2]+x[i+1][W-1])/5
	for j in range (1,W-1):
	 	p[0][j]=(x[0][j+1]+x[1][j+1]+x[0][j-1]+x[1][j-1]+x[1][j])/5
	for j in range (1,W-1):
		p[H-1][j]=(x[H-1][j+1]+x[H-2][j+1]+x[H-1][j-1]+x[H-2][j-1]+x[H-1][j])/5
	return p

def edgepgm(x):
	H=len(x)
	W=len(x[0])
	p=[[0 for col in range (W)]for row in range(H)]
	maxgrad=0
	# wrapping at edges
	for i in range (0,H):
		for j in range (0,W):
			if i==H-1 and j!=0 and j!=W-1:
				hdif = (x[i-1][j-1]-x[i-1][j+1]) + 2*(x[i][j-1]-x[i][j+1]) + (x[0][j-1]-x[0][j+1])
				vdif = (x[i-1][j-1]-x[0][j-1]) + 2*(x[i-1][j]-x[0][j]) + (x[i-1][j+1]-x[0][j+1])
				grad=(hdif*hdif+vdif*vdif)**0.5
				if int(grad)>maxgrad:
					maxgrad=int(grad)
				p[i][j]=int(grad)
			if j==W-1 and i!=0 and i!=H-1:
				hdif = (x[i-1][j-1]-x[i-1][0]) + 2*(x[i][j-1]-x[i][0]) + (x[i+1][j-1]-x[i+1][0])
				vdif = (x[i-1][j-1]-x[i+1][j-1]) + 2*(x[i-1][j]-x[i+1][j]) + (x[i-1][0]-x[i+1][0])
				grad=(hdif*hdif+vdif*vdif)**0.5
				if int(grad)>maxgrad:
					maxgrad=int(grad)
				p[i][j]=int(grad)
			if i==0 and j!=0 and j!=W-1:
				hdif = (x[H-1][j-1]-x[H-1][j+1]) + 2*(x[i][j-1]-x[i][j+1]) + (x[i+1][j-1]-x[i+1][j+1])
				vdif = (x[H-1][j-1]-x[i+1][j-1]) + 2*(x[H-1][j]-x[i+1][j]) + (x[H-1][j+1]-x[i+1][j+1])
				grad=(hdif*hdif+vdif*vdif)**0.5
				if int(grad)>maxgrad:
					maxgrad=int(grad)
				p[i][j]=int(grad)
			if j==0 and i!=0 and i!=H-1:
				hdif = (x[i-1][W-1]-x[i-1][j+1]) + 2*(x[i][W-1]-x[i][j+1]) + (x[i+1][W-1]-x[i+1][j+1])
				vdif = (x[i-1][W-1]-x[i+1][W-1]) + 2*(x[i-1][j]-x[i+1][j]) + (x[i-1][j+1]-x[i+1][j+1])
				grad=(hdif*hdif+vdif*vdif)**0.5
				if int(grad)>maxgrad:
					maxgrad=int(grad)
				p[i][j]=int(grad)

			elif j!=0 and j!=W-1 and i!=0 and i!= H-1:
				hdif = (x[i-1][j-1]-x[i-1][j+1]) + 2*(x[i][j-1]-x[i][j+1]) + (x[i+1][j-1]-x[i+1][j+1])
				vdif = (x[i-1][j-1]-x[i+1][j-1]) + 2*(x[i-1][j]-x[i+1][j]) + (x[i-1][j+1]-x[i+1][j+1])
				grad=(hdif*hdif+vdif*vdif)**0.5
				if int(grad)>maxgrad:
					maxgrad=int(grad)
				p[i][j]=int(grad)
	# normalization
	for i in range (H):
		for j in range (W):
			p[i][j]=int(p[i][j]*(255/maxgrad))	
	return p

def energypgm(r):
	H=len(x)
	W=len(x[0])
	p=[[0 for col in range (W)]for row in range(H)]
	for i in range (H):
		for j in range (W):
			if i==0:
				p[i][j]=r[i][j]
			if j==0:
	 			p[i][j]=r[i][j]+min(p[i-1][j],p[i-1][j+1])
			if j==W-1:
				p[i][j]=r[i][j]+min(p[i-1][j],p[i-1][j-1])
			else:
				p[i][j] = r[i][j] + min(p[i-1][j-1], p[i-1][j], p[i-1][j+1])
	l=[]
	d=min(p[H-1])
	for h in range (0,W):
		if p[H-1][h]==d:
			k=h
			l.append(k)
			x[H-1][k]=255
	t=H-2
	for k in l:
		for t in range (H-2,-1,-1):
			if k==0:
				a=min(p[t][k],p[t][k+1])
				if p[t][k]==a:
					x[t][k]=255
					k=k
				if p[t][k+1]==a:
					x[t][k+1]=255
					k=k+1			
			elif k== W-1:
				a=min(p[t][k],p[t][k-1])
				if p[t][k]==a:
					x[t][k]=255
					k=k
				if p[t][k-1]==a:
					x[t][k-1]=255
					k=k-1				
			else:
				a=min(p[t][k],p[t][k-1],p[t][k+1])
				if p[t][k]==a:
					x[t][k]=255
					k=k
				if p[t][k-1]==a:
					x[t][k-1]=255
					k=k-1
				if p[t][k+1]==a:
					x[t][k+1]=255
					k=k+1
	return x
# img is the 2D list of integers
# file is the output file path
def writepgm(img, file):
	with open(file, 'w') as fout:
		if len(img) == 0:
			pgmHeader = 'p2\n0 0\n255\n'
		else:
			pgmHeader = 'P2\n' + str(len(img[0])) + ' ' + str(len(img)) + '\n255\n'
			fout.write(pgmHeader)
			line = ''
			for i in img:
				for j in i:
					line += str(j) + ' '
			line += '\n'
			fout.write(line)

########## Function Calls ##########
x = readpgm('monalisa.pgm')	
q= averagepgm(x)# test.pgm is the image present in the same working directory
r=edgepgm(x)
s=energypgm(r)
writepgm(s,'energy.pgm')
writepgm(r,'edge.pgm')
writepgm(q,'average.pgm')
writepgm(x, 'monalisa_o.pgm')		# x is the image to output and monalisa_o.pgm is the image output in the same working directory
###################################