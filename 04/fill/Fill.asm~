(INFINITE_LOOP)
	@SCREEN
	D=A
	@addr
	M=D
	(LOOP)		//Paint left to right
		@KBD
		D=A
		@addr		// Pull value of KBD (end) - address
		D=D-M
		@INFINITE_LOOP	// Skip painting
		D;JEQ
		@addr
		A=M
		@KBD		// Pull value saved @KBD
		D=M
		@PAINT		// Jump to PAINT if M@KBD > 0
		D;JGT
		@addr		// Paint screen white
		A=M
		M=0
		@addr
		M=M+1
		@INCREMENT	// Jump to increment (skip PAINT black)
		0;JMP
		(PAINT)		// Paint Screen Black
			@addr
			A=M
			M=-1
			@addr
			M=M+1
		(INCREMENT)		//Decrement counter
			@counter	
			M=M-1
			@LOOP		//Jump to loop
			0;JMP		
			@INFINITE_LOOP	// Continue to loop whole program
			0;JMP
