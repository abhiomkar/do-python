#Author: Abhinay Omkar
#Date: 13th Feb 2010
#Program: spiral-mat.py - Number Matrix in Spiral way
#

# for N in (3,5,7):
# 	for i in range(N):
			# 		for j in range(N	):
# 			print "(%s,%s)" % (i, j),
# 		print
# 		print
# 	print 15*'-'

def main():
"""	
	Spiral the numbers starting from center cell.

	Examples:
	Output:
	Enter matrix size (odd no.): 5
	21 22 23 24 25
	20  7  8  9 10
	19  6  1  2 11
	18  5  4  3 12
	17 16 15 14 13

	Enter matrix size (odd no.): 7
	43 44 45 46 47 48 49
	42 21 22 23 24 25 26
	41 20  7  8  9 10 27
	40 19  6  1  2 11 28
	39 18  5  4  3 12 29
	38 17 16 15 14 13 30
	37 36 35 34 33 32 31

	Enter matrix size (odd no.): 21
	421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441
	420 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362
	419 342 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 363
	418 341 272 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 291 364
	417 340 271 210 157 158 159 160 161 162 163 164 165 166 167 168 169 170 227 292 365
	416 339 270 209 156 111 112 113 114 115 116 117 118 119 120 121 122 171 228 293 366
	415 338 269 208 155 110  73  74  75  76  77  78  79  80  81  82 123 172 229 294 367
	414 337 268 207 154 109  72  43  44  45  46  47  48  49  50  83 124 173 230 295 368
	413 336 267 206 153 108  71  42  21  22  23  24  25  26  51  84 125 174 231 296 369
	412 335 266 205 152 107  70  41  20   7   8   9  10  27  52  85 126 175 232 297 370
	411 334 265 204 151 106  69  40  19   6   1   2  11  28  53  86 127 176 233 298 371
	410 333 264 203 150 105  68  39  18   5   4   3  12  29  54  87 128 177 234 299 372
	409 332 263 202 149 104  67  38  17  16  15  14  13  30  55  88 129 178 235 300 373
	408 331 262 201 148 103  66  37  36  35  34  33  32  31  56  89 130 179 236 301 374
	407 330 261 200 147 102  65  64  63  62  61  60  59  58  57  90 131 180 237 302 375
	406 329 260 199 146 101 100  99  98  97  96  95  94  93  92  91 132 181 238 303 376
	405 328 259 198 145 144 143 142 141 140 139 138 137 136 135 134 133 182 239 304 377
	404 327 258 197 196 195 194 193 192 191 190 189 188 187 186 185 184 183 240 305 378
	403 326 257 256 255 254 253 252 251 250 249 248 247 246 245 244 243 242 241 306 379
	402 325 324 323 322 321 320 319 318 317 316 315 314 313 312 311 310 309 308 307 380
	401 400 399 398 397 396 395 394 393 392 391 390 389 388 387 386 385 384 383 382 381

	3x3
	-----
	(0,0) (0,1) (0,2)

	(1,0) (1,1) (1,2)

	(2,0) (2,1) (2,2)

	5x5
	-----
	(0,0) (0,1) (0,2) (0,3) (0,4)

	(1,0) (1,1) (1,2) (1,3) (1,4)

	(2,0) (2,1) (2,2) (2,3) (2,4)

	(3,0) (3,1) (3,2) (3,3) (3,4)

	(4,0) (4,1) (4,2) (4,3) (4,4)

	7x7
	-----
	(0,0) (0,1) (0,2) (0,3) (0,4) (0,5) (0,6)

	(1,0) (1,1) (1,2) (1,3) (1,4) (1,5) (1,6)

	(2,0) (2,1) (2,2) (2,3) (2,4) (2,5) (2,6)

	(3,0) (3,1) (3,2) (3,3) (3,4) (3,5) (3,6)

	(4,0) (4,1) (4,2) (4,3) (4,4) (4,5) (4,6)

	(5,0) (5,1) (5,2) (5,3) (5,4) (5,5) (5,6)

	(6,0) (6,1) (6,2) (6,3) (6,4) (6,5) (6,6)


	LOGIC:
	Functions that Increments the indexes:
	start_right
	(0,1)		(0,1)		(0,1)

	down
	1		3		5
	(1,0)	(1,0)	(1,0)
			(1,0)	(1,0)
			(1,0)	(1,0)
					(1,0)
					(1,0)

	left
	2		4		6
	(0,-1)	(0,-1)	(0,-1)
	(0,-1)	(0,-1)	(0,-1)
			(0,-1)	(0,-1)
			(0,-1)	(0,-1)
					(0,-1)
					(0,-1)

	up
	2		4		6
	(-1,0)	(-1,0)	(-1,0)
	(-1,0)	(-1,0)	(-1,0)
			(-1,0)	(-1,0)
			(-1,0)	(-1,0)
					(-1,0)
					(-1,0)

	right
	2		4		6
	(0,1)	(0,1)	(0,1)		
	(0,1)	(0,1)	(0,1)
			(0,1)	(0,1)
			(0,1)	(0,1)
					(0,1)
					(0,1)

	i = j = len(S)/2
	C=2

	start_right()

		i , j = (0,1)
	down()
		for x in range(C-1):
			i, j = eval('(i + %s, j + %s)' % (1,0))
	left()
		for x in range(C):
			i, j = eval('(i + %s, j + %s)' % (0,-1))
	up()
		for x in range(C):
			i, j = eval('(i + %s, j + %s)' % (-1,0))
	right()
		for x in range(C):
			i, j = eval('(i + %s, j + %s)' % (0,1))

	C = C+2
"""
	# Start of Main
	# Get the Matrix size
	MAT_SIZE = int(raw_input("Enter matrix size (odd no.): "))

	if MAT_SIZE%2 == 0:
		print "Only odd numbers Plz!"
		exit()
		
	# Center cell's index
	i = j = MAT_SIZE/2
	# We'll use this when displaying final output - array
	disp = len(str(MAT_SIZE**2))

	# This array allocation doesn't work as expected, use .append() instead.
	# ar = [[0]*MAT_SIZE]*MAT_SIZE

	# Creating Blank Array (Our Output Array) 
	ar = []
	for z in range(MAT_SIZE):
	    ar.append([0]*MAT_SIZE)

	# Number of cells to traverse on each side, 
	# as we go away from the center cell the CURV value increases by 2
	CURV=2

	# Assigning the center cell first
	# 'n' starts from 1 to MAT_SIZE**2 (for 5x5 Matrix it is 1 to 25 )
	n = 1
	ar[i][j] = n
	n = n + 1

	# import pdb
	# pdb.set_trace()

	while True:
		if n >= MAT_SIZE**2:
			# when we reach the max 'n' value stop there
			break

		# Start Right
		i, j = start_right(i, j)
		ar[i][j] = n
		n = n + 1
		# print '(i, j): (%s, %s) ' % (i,j)

		# Go Down
		for x in range(CURV-1):
			i, j = go_down(i, j)
			ar[i][j] = n
			n = n + 1
			# print '(i, j): (%s, %s) ' % (i,j)
	
		# Go Left
		for x in range(CURV):
			i, j = go_left(i, j)
			ar[i][j] = n
			n = n + 1
			# print '(i, j): (%s, %s) ' % (i,j)

		# Go Up
		for x in range(CURV):
			i, j = go_up(i, j)
			ar[i][j] = n
			n = n + 1
			# print '(i, j): (%s, %s) ' % (i,j)

		# Go Right
		for x in range(CURV):
			i, j = go_right(i, j)
			ar[i][j] = n
			n = n + 1
			# print '(i, j): (%s, %s) ' % (i,j)
	
		CURV = CURV + 2

	#end-while
	
	# Print final output
	display_array(ar, disp)

def start_right(i, j):
	i, j = eval('(i + %s, j + %s)' % (0,1))
	return i, j
	
def go_down(i, j):
		i, j = eval('(i + %s, j + %s)' % (1,0))
		return i, j

def go_left(i, j):
		i, j = eval('(i + %s, j + %s)' % (0,-1))
		return i, j
		
def go_up(i, j):
		i, j = eval('(i + %s, j + %s)' % (-1,0))
		return i, j
		
def go_right(i, j):
		i, j = eval('(i + %s, j + %s)' % (0,1))	
		return i, j

def display_array(ar, disp):
	"""Display's Array"""
	from string import rjust
	for a in ar:
		for b in a:
			# print "%3s" % b,
			print rjust(str(b), disp),
		print
	
if __name__ == '__main__':
	main()
