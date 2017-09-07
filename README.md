# Algorithm_Toolbox
--------------------------------------------------------------------------------
The numtop.py pseudocode:

NumberToPattern(index,k)

 if k = 1
 
   return NumberToSymbol(index)
   
 prefixIndex <- Quotient(index, 4)
 
 r <- Remainder(index,4)
 
 symbol <- NumberToSymbol(r)
 
 prefixpattern <- NumberToPattern(prefixIndex, k-1)
 
 return concatenation of prefixpattern with symbol
 
 --------------------------------------------------------------------------------
 
 The Ori_find.py script description:
 
 Purpose: Find a position in a genome wehre the skew diagram attains a minimum
 
 Input: A DNA string Genome
 
 Output: All integer(s) i iminimizing Skew_i(Genome) among all values of i (from 0 to |Genome|).
 
 ---------------------------------------------------------------------------------
  The motifs.py script description:
  
  Using the brute force approach solving the motif, based on the observation any (k,d) motif must be at most d mismatches apart from some k-mer
  
  appearing in on eof the strings of DNA. Therefore, we can generate all such k-mers and then check which of them are (k,d)-motifs.
  ---------------------------------------------------------------------------------
