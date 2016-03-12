#--------------------------------------------
#	LEGASPI, ALELI S.
#	2013-06797
#	CMSC128 : Programming Assignment
#--------------------------------------------


#	01 Function: int getHammingDistance(string str1, string str2)
def getHammingDistance(str1,str2):
	print "String1: ",str1,"	","String2: ",str2;
	count = 0;
	str1len = len(str1);
	str2len = len(str2);
	if(str1len!=str2len):					#if not of equal sizes
		print "NOT EQUAL SIZE OF STRINGS!\n";
	else:							#valid
		x=0;					#counts how many character differs between the string
		while(x<str1len):
			if(str1[x]!=str2[x]): 
				count=count+1;
			x=x+1;					
	return count;



#	02 Function: int countSubstrPattern(string original, string pattern)
def countSubstrPattern(origstr,patternstr):
	print "String: ",origstr,"	","Pattern: ",patternstr;
	matchcnt = 0;
	olen=len(origstr);
	plen=len(patternstr);
	
	xx=0;						#counts the occurence of the pattern in the string
	while(xx<olen):					#starting at each index xx, check if the next sequence of char is equal to pattern ]
		if(origstr.find(patternstr,xx,xx+plen)!=-1):
			matchcnt = matchcnt +1;
		xx=xx+1;
		
	return matchcnt;
	
	
	
#	03 Function: bool isValidString(string str, string alphabet)
def isValidString(samplestr,alphabet):
	print "String: ",samplestr,"	","Alphabet: ",alphabet;
	slen=len(samplestr);
	alen = len(alphabet);
	if(slen==0):
		print "Provide sample string!";
		return;
	elif(alen==0):
		print "Provide at least one letter in the alphabet!";
		return;
	else :
		flag=1;
		xx=0;
		while(xx<slen):				#checks if each char in sample string exists in alphabet
			if(alphabet.find(samplestr[xx])==-1):
				flag=0;			#if char is not found in alphabet, becomes invalid
				break;
			xx=xx+1;
		
		if(flag==0) : return "false";
		else : return "true";
	
	
	
#	04 Function: int getSkew(string str, int n)
def getSkew(mystr,n):	
	print "String: ",mystr,"	","n: ",n;
	if(len(mystr)==0):
		print "Invalid input string!";
		return;
	elif(n<=0):
		print "\'n\' must be greater than 0!";
		return;
	elif(n>len(mystr)):
		print "n should not be greater than the string length!";
		return;
	else:
		Gcnt=mystr.count("G",0,n);		#counts G and C
		Ccnt=mystr.count("C",0,n);
		return Gcnt-Ccnt;			#subtract G and C

	
	
#05 Function: int getMaxSkewN(string str, int n)			
def getMaxSkewN(mystr,n):
	print "String: ",mystr,"	","n: ",n;	
	if(len(mystr)==0):
		print "Invalid input string!";
		return;
	elif(n<=0):
		print "\'n\' must be greater than 0!";
		return;
	elif(n>len(mystr)):
		print "n should not be greater than the string length!";
		return;
	else:
		Gcnt=mystr.count("G",0,n);		#simply returns the number of G in the string
		return Gcnt;
	
		
		
#06 Function: int getMinSkewN(string str, int n)
def getMinSkewN(mystr,n):
	print "String: ",mystr,"	","n: ",n;	
	if(len(mystr)==0):
		print "Invalid input string!";
		return;
	elif(n<=0):
		print "\'n\' must be greater than 0!";
		return;
	elif(n>len(mystr)):
		print "n should not be greater than the string length!";
		return;
	else:
		Gcnt=mystr.count("G",0,n);	#count G and C
		Ccnt=mystr.count("C",0,n);
		diff=Gcnt-Ccnt;
		if(diff>1): return 1;		#G-C must not be greater than 1 since it just returns the minimum number
		else : return diff;


#---------------------------MAIN----------------------------------#
print "\n[FUNCTION1]";
f1 = getHammingDistance("aaa","aba");
print ">> Hamming Distance : ", f1;

print "\n[FUNCTION2]";
f2 = countSubstrPattern("atatata","ata");
print ">> Count of Pattern Matches :", f2;

print "\n[FUNCTION3]";
f3 = isValidString("abcdefj","abcdefghi");
print ">> Is Valid String ?: ",f3;

print "\n[FUNCTION4]";
f4 = getSkew("GGCCCAAA",5);
print ">> Skew : ",f4;

print "\n[FUNCTION5]";	
f5 = getMaxSkewN("GGCCCAAA",5);
print ">> MaxSkew : ",f5;

print "\n[FUNCTION6]";
f6 = getMinSkewN("GGGGCCCAAA",5);
print ">> MinSkew : ",f6;

