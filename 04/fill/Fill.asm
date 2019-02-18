// "Paint the whole screen black" 
// 16384 is the beginning of the screens' memory address
//RAM[16384+r*32+c/16]  (r = row, c = column
// 256 rows 512px per row


//set up listener for keyboard

	@SCREEN
	D=A
	@addr
	M=D
	@8192		//Initialize counter
	D=A
	@counter
	M=D
	@addr		// Paint addr -1
	A=M
	M=-1	
	(LOOP)			//Paint left to right
		@counter	//Check counter for end
		D=M
		@END
		D;JEQ
		@addr		//Paint addr -1
		A=M
		M=-1	
		@addr		//Change addr loc
		D=M
		@1
		D=D+A
		@addr
		M=D
		@counter	//Decrement counter
		M=M-1
		@LOOP
		0;JMP		//Break 
	(END)
