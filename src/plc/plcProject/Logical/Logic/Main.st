PROGRAM _CYCLIC
	
	IF (countUp) THEN
		countUp := FALSE;
		counter := counter + 1;
	END_IF
	
	IF (reset) THEN
		reset := FALSE;
		counter := 0;
	END_IF
	 
END_PROGRAM

